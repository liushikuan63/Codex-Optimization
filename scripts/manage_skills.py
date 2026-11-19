"""Install the skills declared by the share pack without overwriting existing skills."""

import argparse
import hashlib
import json
from pathlib import Path
import re
import sys


REPO = Path(__file__).resolve().parents[1]
LEGACY_NAMES = (
    "csp-browser-acceptance", "csp-delivery-evidence", "csp-plan-review",
    "csp-skill-adoption", "csp-vibecoding-batch", "csp-visual-detail",
    "csp-windows-workflow",
)
RECEIPT = ".codex-optimization-install.json"


def skill_names():
    catalog = json.loads((REPO / "inventory.json").read_text("utf8"))
    names = tuple(catalog["skills"])
    if not names or any(not re.fullmatch(r"csp-[a-z0-9]+(?:-[a-z0-9]+)*", n) for n in names):
        raise ValueError("Invalid skill name in inventory")
    folders = {p.name for p in (REPO / "skills").iterdir() if p.is_dir()}
    if set(names) != folders:
        raise ValueError("Skill directories differ from the published inventory")
    return names


def digest(data):
    return hashlib.sha256(data).hexdigest()


def present(path):
    return path.exists() or path.is_symlink() or is_junction(path)


def is_junction(path):
    return getattr(path, "is_junction", lambda: False)()


def safe_directory(path):
    if path.is_symlink() or is_junction(path) or (path.exists() and not path.is_dir()):
        raise ValueError(f"Expected a directory without links: {path}")


def scan(folder):
    safe_directory(folder)
    if not folder.is_dir():
        raise ValueError(f"Missing skill directory: {folder}")
    files = {}
    for path in sorted(folder.rglob("*")):
        if path.is_symlink() or is_junction(path):
            raise ValueError(f"Unexpected link: {path}")
        if path.is_file():
            files[path.relative_to(folder).as_posix()] = path.read_bytes()
        elif not path.is_dir():
            raise ValueError(f"Unexpected entry: {path}")
    return files


def manifest(payload):
    return {name: {rel: digest(data) for rel, data in files.items()}
            for name, files in payload.items()}


def current(root, names):
    return manifest({name: scan(root / name) for name in names})


def parent_dirs(root, names):
    result = {root}
    for name in names:
        result.update(p for p in (root / name).parents if p.is_relative_to(root))
    return sorted(result, key=lambda p: len(p.parts), reverse=True)


def delete_exact(root, hashes):
    for rel, want in hashes.items():
        path = root / rel
        if path.is_symlink() or not path.is_file() or digest(path.read_bytes()) != want:
            raise ValueError(f"File changed; preserve it: {path}")
        path.unlink()
    for path in parent_dirs(root, hashes):
        if path.exists() and not any(path.iterdir()):
            path.rmdir()


def run(action, root):
    safe_directory(root.parent)
    safe_directory(root)
    marker = root / RECEIPT
    if marker.is_symlink() or is_junction(marker) or (marker.exists() and not marker.is_file()):
        raise ValueError(f"Invalid receipt path: {marker}")
    if action == "uninstall":
        if not marker.is_file():
            raise ValueError(f"No install receipt: {marker}")
        before = marker.read_bytes()
        entry = json.loads(before)
        if not isinstance(entry, dict) or not isinstance(entry.get("files"), dict):
            raise ValueError("Invalid receipt")
        names = skill_names()
        if entry.get("schema") == 1 and entry.get("version") in ("0.1.0", "0.2.0", "v0.1.0", "v0.2.0"):
            names = LEGACY_NAMES
        elif entry.get("schema") != 2:
            raise ValueError("Unknown receipt; use the installer supplied with that release")
        if set(entry["files"]) != set(names):
            raise ValueError("Unexpected receipt membership; no files removed")
        found = current(root, names)
        # The on-disk inventory supplies relative paths; receipt text never supplies paths to delete.
        if entry["files"] != found:
            raise ValueError("Installed files changed or receipt is invalid. No files removed.")
        for name in names:
            delete_exact(root / name, found[name])
        if marker.read_bytes() != before:
            raise ValueError("Receipt changed during uninstall")
        marker.unlink()
        return f"Uninstalled {len(names)} managed skills"

    if present(marker):
        raise ValueError(f"Existing install receipt: {marker}. Uninstall before reinstalling.")
    names = skill_names()
    conflicts = [str(root / name) for name in names if present(root / name)]
    if conflicts:
        raise ValueError("Existing skill directories; no files written:\n" + "\n".join(conflicts))
    payload = {name: scan(REPO / "skills" / name) for name in names}
    if any("SKILL.md" not in files for files in payload.values()):
        raise ValueError("Missing bundled SKILL.md")
    if action == "plan":
        return f"Ready: {len(payload)} skills to {root}; no files written"
    root.mkdir(parents=True, exist_ok=True)
    data = {"schema": 2, "version": (REPO / "VERSION").read_text("utf8").strip(),
            "files": manifest(payload)}
    created = {}
    # Exclusive receipt creation serializes repeated runs; existing skill dirs are claimed with mkdir.
    with marker.open("x", encoding="utf8") as record:
        try:
            for name, files in payload.items():
                dest = root / name
                dest.mkdir()
                created[name] = {}
                for rel, body in files.items():
                    path = dest / rel
                    path.parent.mkdir(parents=True, exist_ok=True)
                    with path.open("xb") as stream:
                        stream.write(body)
                    created[name][rel] = data["files"][name][rel]
            if current(root, names) != data["files"]:
                raise ValueError("Files changed during install")
            record.write(json.dumps(data, indent=2) + "\n")
            record.flush()
        except (OSError, ValueError):
            for name, files in reversed(list(created.items())):
                delete_exact(root / name, files)
            # Preserve the receipt on error: there may be an interrupted write to inspect.
            raise
    return f"Installed {len(names)} skills to {root}"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("action", choices=("plan", "install", "uninstall"))
    scope = parser.add_mutually_exclusive_group()
    scope.add_argument("--project", type=Path, default=Path.cwd(), help="project directory (default: cwd)")
    scope.add_argument("--user", action="store_true", help="use ~/.agents/skills")
    args = parser.parse_args()
    try:
        project = Path.home() if args.user else args.project.resolve(strict=True)
        if not project.is_dir():
            raise ValueError(f"Missing project directory: {project}")
        print(run(args.action, project / ".agents/skills"))
    except (OSError, ValueError, AttributeError) as error:
        parser.exit(1, f"{error}\n")


if __name__ == "__main__":
    main()
