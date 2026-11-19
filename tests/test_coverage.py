"""Exercise the omissions that made an earlier release look complete."""
import json
from pathlib import Path
import shutil
import subprocess
import tempfile
import unittest
import zipfile

from scripts.check_coverage import check_tree, check_zip, check_source, load_inventory

BASE = Path(__file__).resolve().parents[1]


class CoverageTest(unittest.TestCase):
    def setUp(self):
        tmp = tempfile.TemporaryDirectory(prefix="pack-coverage-")
        self.addCleanup(tmp.cleanup)
        self.root = Path(tmp.name) / "pack"
        self.root.mkdir()
        for name in ("skills", "rules", "docs"):
            shutil.copytree(BASE / name, self.root / name)
        shutil.copy2(BASE / "inventory.json", self.root / "inventory.json")

    def test_missing_skill_is_named(self):
        skill = "csp-api-contracts"
        shutil.rmtree(self.root / "skills" / skill)
        with self.assertRaisesRegex(ValueError, skill):
            check_tree(self.root)

    def test_missing_translated_rule_is_named(self):
        path = self.root / "rules/AGENTS.en.example.md"
        content = path.read_text("utf8")
        path.write_text(content.replace("## R13 ·", "## XXX ·", 1), encoding="utf8")
        with self.assertRaisesRegex(ValueError, "R13"):
            check_tree(self.root)

    def test_guide_must_link_to_every_skill(self):
        guide = self.root / "docs/skills.en.md"
        body = guide.read_text("utf8")
        guide.write_text(body.replace("../skills/csp-ci-evidence/SKILL.md", "#missing"), encoding="utf8")
        with self.assertRaisesRegex(ValueError, "csp-ci-evidence"):
            check_tree(self.root)

    def test_zip_missing_reference_is_named(self):
        repo = self.root.parent / "zip-source"
        repo.mkdir()
        ref = "skills/example/references/acceptance.md"
        (repo / ref).parent.mkdir(parents=True)
        (repo / ref).write_bytes(b"procedure\n")
        (repo / "inventory.json").write_bytes(b"{}\n")
        subprocess.run(["git", "init", "-q", str(repo)], check=True)
        subprocess.run(["git", "-C", str(repo), "add", "--", ref, "inventory.json"], check=True)
        archive = self.root.parent / "incomplete.zip"
        with zipfile.ZipFile(archive, "w") as zf:
            zf.write(repo / "inventory.json", "inventory.json")
        with self.assertRaisesRegex(ValueError, "acceptance[.]md"):
            check_zip(archive, repo)

    def test_method_missing_inside_existing_skill_is_named(self):
        path = self.root / "skills/csp-event-delivery/references/applied-methods.md"
        page = path.read_text("utf8")
        self.assertIn("`rabbitmq-expert`", page)
        path.write_text(page.replace(", `rabbitmq-expert`", ""), encoding="utf8")
        with self.assertRaisesRegex(ValueError, "rabbitmq-expert"):
            check_tree(self.root)
