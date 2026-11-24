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
RECEIPT = ".codex-optimization-install.json"


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
        receipt = self.target / RECEIPT
        expected = {entry.parent.name for entry in SKILLS.glob("*/SKILL.md")}
        self.assertEqual(set(json.loads(receipt.read_text("utf8"))["files"]), expected)
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

    def test_verify_current_install_and_report_file_drift_without_changes(self):
        self.command("install")
        before = snapshot(self.target)
        result = self.command("verify")
        self.assertIn("Scope: project", result.stdout)
        # Windows may spell the temporary root as an 8.3 alias.
        expected_root = self.project.resolve(strict=True) / ".agents/skills"
        self.assertIn(f"Skills directory: {expected_root}", result.stdout)
        self.assertIn("Status: VERIFIED", result.stdout)
        self.assertEqual(before, snapshot(self.target))

        skill = self.target / "csp-visual-detail"
        (skill / "SKILL.md").write_text("local instructions", encoding="utf8")
        (skill / "scripts/crop_detail.py").unlink()
        (skill / "local.md").write_text("local notes", encoding="utf8")
        before = snapshot(self.target)
        result = self.command("verify", 2)
        self.assertIn("CHANGED csp-visual-detail/SKILL.md", result.stdout)
        self.assertIn("MISSING csp-visual-detail/scripts/crop_detail.py", result.stdout)
        self.assertIn("EXTRA csp-visual-detail/local.md", result.stdout)
        self.assertIn("Status: CONFLICT", result.stdout)
        self.assertEqual(before, snapshot(self.target))

    def test_verify_requires_receipt_even_for_matching_files(self):
        result = self.command("verify", 2)
        self.assertIn("Status: NOT_INSTALLED", result.stdout)
        self.assertFalse(self.target.exists())
        self.command("install")
        (self.target / RECEIPT).unlink()
        before = snapshot(self.target)
        result = self.command("verify", 2)
        self.assertIn("UNMANAGED csp-plan-review", result.stdout)
        self.assertIn("Status: CONFLICT", result.stdout)
        self.assertEqual(before, snapshot(self.target))

    def test_verify_distinguishes_older_receipt_from_current_release(self):
        self.command("install")
        receipt = self.target / RECEIPT
        entry = json.loads(receipt.read_text("utf8"))
        entry["version"] = "0.3.0"
        receipt.write_text(json.dumps(entry), encoding="utf8")
        before = snapshot(self.target)
        result = self.command("verify", 2)
        self.assertIn("Receipt version: 0.3.0", result.stdout)
        self.assertIn("Status: DIFFERENT_VERSION", result.stdout)
        self.assertEqual(before, snapshot(self.target))

    def test_verify_checks_only_the_selected_user_scope(self):
        self.command("install")
        fake_home = self.project / "separate user home"
        fake_home.mkdir()
        result = subprocess.run([sys.executable, str(RUN), "verify", "--user"],
                                capture_output=True, text=True, encoding="utf8",
                                env={**os.environ, "PYTHONUTF8": "1", "HOME": str(fake_home),
                                     "USERPROFILE": str(fake_home)})
        self.assertEqual(result.returncode, 2, result.stdout + result.stderr)
        self.assertIn("Scope: user", result.stdout)
        expected_root = fake_home.resolve(strict=True) / ".agents/skills"
        self.assertIn(f"Skills directory: {expected_root}", result.stdout)
        self.assertIn("Status: NOT_INSTALLED", result.stdout)
        self.assertFalse((fake_home / ".agents").exists())

    def test_verify_rejects_matching_local_edits_to_receipt_and_release_file(self):
        self.command("install")
        receipt = self.target / RECEIPT
        entry = json.loads(receipt.read_text("utf8"))
        data = b"local instructions"
        (self.target / "csp-plan-review/SKILL.md").write_bytes(data)
        entry["files"]["csp-plan-review"]["SKILL.md"] = hashlib.sha256(data).hexdigest()
        receipt.write_text(json.dumps(entry), encoding="utf8")
        before = snapshot(self.target)
        result = self.command("verify", 2)
        self.assertIn("RECEIPT_MISMATCH csp-plan-review/SKILL.md", result.stdout)
        self.assertIn("Status: CONFLICT", result.stdout)
        self.assertEqual(before, snapshot(self.target))

    def test_verify_rejects_invalid_receipt_without_changes(self):
        self.command("install")
        receipt = self.target / RECEIPT
        entry = json.loads(receipt.read_text("utf8"))
        entry["files"]["csp-plan-review"]["../unmanaged"] = "b" * 64
        receipt.write_text(json.dumps(entry), encoding="utf8")
        before = snapshot(self.target)
        result = self.command("verify", 1)
        self.assertIn("Invalid receipt file path", result.stderr)
        self.assertEqual(before, snapshot(self.target))

    def test_verify_blocks_linked_skill_entries(self):
        self.command("install")
        outside = self.project / "outside.txt"
        outside.write_bytes(b"untouched")
        linked = self.target / "csp-plan-review/user-link.md"
        try:
            linked.symlink_to(outside)
        except OSError:
            self.skipTest("This environment cannot create symlinks")
        result = self.command("verify", 1)
        self.assertIn("BLOCKED csp-plan-review/user-link.md", result.stdout)
        self.assertIn("Status: BLOCKED", result.stdout)
        self.assertEqual(outside.read_bytes(), b"untouched")
        self.assertTrue(linked.is_symlink())

    def test_pack_links_and_entry_names(self):
        auditor = SKILLS / "csp-skill-adoption/scripts/audit_references.py"
        skills = sorted(SKILLS.iterdir())
        declared = set(json.loads((BASE / "inventory.json").read_text("utf8"))["skills"])
        self.assertEqual({folder.name for folder in skills}, declared)
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
