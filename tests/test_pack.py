import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

from PIL import Image

BASE = Path(__file__).resolve().parents[1]
RUN = BASE / "scripts/manage_skills.py"
SKILLS = BASE / "skills"


def snapshot(root):
    return {p.relative_to(root): hashlib.sha256(p.read_bytes()).hexdigest()
            for p in root.rglob("*") if p.is_file()}


class PackTest(unittest.TestCase):
    def setUp(self):
        temp = tempfile.TemporaryDirectory(prefix="codex-pack-")
        self.addCleanup(temp.cleanup)
        self.project = Path(temp.name) / "项目 with spaces"
        self.project.mkdir()
        self.target = self.project / ".agents/skills"

    def command(self, action, exit_code=0):
        result = subprocess.run([sys.executable, str(RUN), action, "--project", str(self.project)],
                                capture_output=True, text=True, encoding="utf8",
                                env={**os.environ, "PYTHONUTF8": "1"})
        self.assertEqual(result.returncode, exit_code, result.stdout + result.stderr)
        return result

    def test_actual_install_and_uninstall_in_isolated_project(self):
        self.command("plan")
        self.assertFalse(self.target.exists())
        self.command("install")
        receipt = self.target / ".codex-optimization-install.json"
        self.assertEqual(len(json.loads(receipt.read_text("utf8"))["files"]), 7)
        actual = snapshot(self.target)
        self.assertEqual({k: v for k, v in actual.items() if k != Path(receipt.name)}, snapshot(SKILLS))
        self.command("install", 1)
        self.assertEqual(actual, snapshot(self.target))
        outside = self.target / "unmanaged" / "SKILL.md"
        outside.parent.mkdir()
        outside.write_text("user data", encoding="utf8")
        self.command("uninstall")
        self.assertEqual(list(snapshot(self.target)), [Path("unmanaged/SKILL.md")])

    def test_conflict_does_not_create_any_part_of_pack(self):
        occupied = self.target / "csp-windows-workflow" / "SKILL.md"
        occupied.parent.mkdir(parents=True)
        occupied.write_text("user data", encoding="utf8")
        before = snapshot(self.target)
        self.command("plan", 1)
        self.command("install", 1)
        self.assertEqual(before, snapshot(self.target))

    def test_uninstall_preserves_changed_skills_and_other_entries(self):
        self.command("install")
        changed = self.target / "csp-plan-review" / "SKILL.md"
        changed.write_bytes(changed.read_bytes() + b"\nUser note\n")
        before = snapshot(self.target)
        self.command("uninstall", 1)
        self.assertEqual(before, snapshot(self.target))

    def test_pack_links_and_entry_names(self):
        auditor = SKILLS / "csp-skill-adoption/scripts/audit_references.py"
        skills = sorted(SKILLS.iterdir())
        self.assertEqual(len(skills), 7)
        for folder in skills:
            body = (folder / "SKILL.md").read_text("utf8").splitlines()
            self.assertEqual(body[:2], ["---", f"name: {folder.name}"])
            self.assertTrue(any(line.startswith("description: ") for line in body[2:5]))
        completed = subprocess.run([sys.executable, "-X", "utf8", str(auditor), *map(str, skills)],
                                   capture_output=True, encoding="utf8")
        self.assertEqual(completed.returncode, 0, completed.stdout + completed.stderr)

    def test_installed_visual_script_preserves_pixels_and_rejects_overwrite(self):
        self.command("install")
        script = self.target / "csp-visual-detail/scripts/crop_detail.py"
        src, dst = self.project / "样本.png", self.project / "裁切.png"
        with Image.new("RGBA", (2, 2)) as image:
            image.putpixel((1, 0), (19, 79, 27, 180))
            image.save(src)
        args = [sys.executable, str(script), str(src), str(dst), "--box", "1", "0", "2", "1", "--scale", "3"]
        self.assertEqual(subprocess.run(args, capture_output=True).returncode, 0)
        with Image.open(dst) as image:
            self.assertEqual(image.size, (3, 3))
            self.assertEqual(image.getpixel((2, 2)), (19, 79, 27, 180))
        frozen = dst.read_bytes()
        self.assertEqual(subprocess.run(args, capture_output=True).returncode, 1)
        self.assertEqual(dst.read_bytes(), frozen)


if __name__ == "__main__":
    unittest.main()
