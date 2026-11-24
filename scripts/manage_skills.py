"""Install and verify the share pack's skills without overwriting existing skills."""

import argparse
import hashlib
import json
from pathlib import Path
import re
import stat
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


def read_receipt(marker, names):
    def unique_fields(pairs):
        fields = dict(pairs)
        if len(fields) != len(pairs):
            raise ValueError("Duplicate fields in install receipt")
        return fields

    try:
        entry = json.loads(marker.read_text("utf8"), object_pairs_hook=unique_fields)
    except (json.JSONDecodeError, UnicodeDecodeError):
        raise ValueError("Invalid install receipt JSON") from None
    if not isinstance(entry, dict):
        raise ValueError("Invalid install receipt")
    version, schema, files = entry.get("version"), entry.get("schema"), entry.get("files")
    if not isinstance(version, str) or not re.fullmatch(r"v?[0-9]+\.[0-9]+\.[0-9]+", version):
        raise ValueError("Invalid receipt version")
    if type(schema) is int and schema == 1 and version.removeprefix("v") in ("0.1.0", "0.2.0"):
        names = LEGACY_NAMES
    elif type(schema) is not int or schema != 2:
        raise ValueError("Unknown receipt; use the installer supplied with that release")
    if not isinstance(files, dict) or set(files) != set(names):
        raise ValueError("Unexpected receipt membership; use the installer supplied with that release")
    for hashes in files.values():
        if not isinstance(hashes, dict) or "SKILL.md" not in hashes:
            raise ValueError("Invalid receipt file inventory")
        for rel, want in hashes.items():
            if (re.search(r"[\\:\x00-\x1f\x7f]", rel)
                    or any(part in ("", ".", "..") for part in rel.split("/"))):
                raise ValueError("Invalid receipt file path")
            if not isinstance(want, str) or not re.fullmatch(r"[0-9a-f]{64}", want):
                raise ValueError("Invalid receipt file digest")
    return version, files


def entry_stat(path):
    try:
        return path.lstat()
    except FileNotFoundError:
        return None


def is_redirect(info):
    return (stat.S_ISLNK(info.st_mode)
            or getattr(info, "st_file_attributes", 0) & stat.FILE_ATTRIBUTE_REPARSE_POINT)


def inspect_skill(folder, expected):
    differences, seen = [], set()

    def visit(path):
        info = entry_stat(path)
        if info is None:
            return
        relative = path.relative_to(folder).as_posix()
        label = folder.name if path == folder else f"{folder.name}/{relative}"
        # Walk physical entries only. Receipt names are never opened as paths.
        if is_redirect(info) or (
                not stat.S_ISDIR(info.st_mode) and
                (path == folder or not stat.S_ISREG(info.st_mode))):
            differences.append(("BLOCKED", label))
        elif stat.S_ISDIR(info.st_mode):
            for child in sorted(path.iterdir()):
                visit(child)
        else:
            seen.add(relative)
            if relative not in expected:
                # A local extra file is a conflict; its contents are not needed.
                differences.append(("EXTRA", label))
            else:
                with path.open("rb") as stream:
                    if hashlib.file_digest(stream, "sha256").hexdigest() != expected[relative]:
                        differences.append(("CHANGED", label))

    if entry_stat(folder) is None:
        return [("MISSING", folder.name)]
    visit(folder)
    if not any(kind == "BLOCKED" for kind, _ in differences):
        differences.extend(("MISSING", f"{folder.name}/{rel}") for rel in expected.keys() - seen)
    return differences


def verify(root, scope):
    version = (REPO / "VERSION").read_text("utf8").strip()
    names = skill_names()
    print(f"Scope: {scope}\nSkills directory: {root}\nPack version: {version}")
    for directory in (root.parent, root):
        info = entry_stat(directory)
        if info is not None and (is_redirect(info) or not stat.S_ISDIR(info.st_mode)):
            raise ValueError(f"Unsafe skills directory: {directory}")
    marker = root / RECEIPT
    info = entry_stat(marker)
    if info is not None and (is_redirect(info) or not stat.S_ISREG(info.st_mode)):
        raise ValueError(f"Invalid receipt path: {marker}")
    if info is None:
        installed, recorded = None, {}
    else:
        installed, recorded = read_receipt(marker, names)
    print(f"Receipt version: {installed or 'none'}")

    conflicts = []
    expected_names = set(names) | set(recorded)
    for name in sorted(expected_names):
        if name in recorded:
            conflicts.extend(inspect_skill(root / name, recorded[name]))
        elif entry_stat(root / name) is not None:
            conflicts.append(("UNMANAGED", name))
    if installed == version:
        bundled = current(REPO / "skills", names)
        for name in names:
            for rel in bundled[name].keys() | recorded[name].keys():
                if bundled[name].get(rel) != recorded[name].get(rel):
                    conflicts.append(("RECEIPT_MISMATCH", f"{name}/{rel}"))

    for kind, path in sorted(conflicts, key=lambda item: (item[1], item[0])):
        # Keep local names on one line even if a POSIX filename contains control characters.
        label = path if path.isprintable() else json.dumps(path, ensure_ascii=True)
        print(f"{kind} {label}")
    if any(kind == "BLOCKED" for kind, _ in conflicts):
        status, code = "BLOCKED", 1
    elif conflicts:
        status, code = "CONFLICT", 2
    elif installed is None:
        status, code = "NOT_INSTALLED", 2
    elif installed != version:
        status, code = "DIFFERENT_VERSION", 2
    else:
        status, code = "VERIFIED", 0
    print(f"Status: {status}")
    return code


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
    parser.add_argument("action", choices=("plan", "install", "verify", "uninstall"))
    scope = parser.add_mutually_exclusive_group()
    scope.add_argument("--project", type=Path, default=Path.cwd(), help="project directory (default: cwd)")
    scope.add_argument("--user", action="store_true", help="use ~/.agents/skills")
    args = parser.parse_args()
    try:
        project = Path.home() if args.user else args.project
        if not args.user or args.action == "verify":
            project = project.resolve(strict=True)
        if not project.is_dir():
            raise ValueError(f"Missing project directory: {project}")
        root = project / ".agents/skills"
        if args.action == "verify":
            sys.exit(verify(root, "user" if args.user else "project"))
        print(run(args.action, root))
    except (OSError, ValueError, AttributeError, KeyError, RuntimeError) as error:
        parser.exit(1, f"{error}\n")


if __name__ == "__main__":
    main()
