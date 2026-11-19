"""Verify the public inventory against independent sources and the actual release ZIP."""
import argparse
import hashlib
import json
from pathlib import Path
import re
import subprocess
import zipfile

ROOT = Path(__file__).resolve().parents[1]
RULE_FILES = ("rules/AGENTS.en.example.md", "rules/AGENTS.zh-CN.example.md")


def compare(label, expected, actual):
    missing, extra = sorted(set(expected) - set(actual)), sorted(set(actual) - set(expected))
    if missing or extra:
        raise ValueError(f"{label}: missing={missing}, unexpected={extra}")


def rule_ids(text):
    return re.findall(r"^## (R[0-9]+) · .+$", text, flags=re.M)


def load_inventory(root):
    return json.loads((root / "inventory.json").read_text("utf8"))


def check_tree(root):
    data = load_inventory(root)
    names = set(data["skills"])
    folders = {p.name for p in (root / "skills").iterdir() if p.is_dir()}
    compare("skill directories", names, folders)
    for name, info in data["skills"].items():
        page = (root / "skills" / name / "SKILL.md").read_text("utf8")
        if not re.search(r"^name: " + re.escape(name) + r"$", page, re.M):
            raise ValueError(f"skill entry name: {name}")
        if "## English" not in page or not re.search(r"[\u3400-\u9fff]", page):
            raise ValueError(f"bilingual skill entry: {name}")
        if not info["zh"] or not info["en"]:
            raise ValueError(f"missing guide title: {name}")
    for guide in ("docs/skills.md", "docs/skills.en.md"):
        text = (root / guide).read_text("utf8")
        listed = re.findall(r"\(\.\./skills/(csp-[a-z0-9-]+)/SKILL\.md\)", text)
        compare(guide, names, listed)
        if len(listed) != len(names):
            raise ValueError(f"duplicate guide entry: {guide}")
    for path in RULE_FILES:
        ids = rule_ids((root / path).read_text("utf8"))
        if ids != data["rule_ids"]:
            compare(path, data["rule_ids"], ids)
            raise ValueError(f"{path}: duplicate or reordered rule")
    for source, target in data["personal_skills"].items():
        if target not in names:
            raise ValueError(f"personal skill {source}: absent target {target}")
    for source, entry in data["upstream_skills"].items():
        if entry["kind"] == "adapted" and entry["target"] in names:
            continue
        if entry["kind"] == "upstream-only" and entry.get("reason_en") and entry.get("reason_zh"):
            continue
        raise ValueError(f"upstream skill {source}: missing target or specific exclusion")
    for name in sorted(names):
        folder = root / "skills" / name
        target = "references/applied-methods.md"
        if f"({target})" not in (folder / "SKILL.md").read_text("utf8"):
            raise ValueError(f"worked examples not linked: {name}")
        covered = []
        for row in (folder / target).read_text("utf8").splitlines():
            if not row.startswith("| `"):
                continue
            cells = [c.strip() for c in row.strip("|").split("|")]
            if (len(cells) != 3 or not re.search(r"[\u3400-\u9fff]", cells[1])
                    or not re.search(r"[a-zA-Z]{3}", cells[2])):
                raise ValueError(f"bilingual worked example: {name}: {row}")
            covered.extend(re.findall(r"`([a-z0-9-]+)`", cells[0]))
        expected = [s for s, e in data["upstream_skills"].items() if e.get("target") == name]
        compare(f"worked examples in {name}", expected, covered)
        if len(covered) != len(set(covered)):
            raise ValueError(f"duplicate source in worked examples: {name}")
    for field in ("rule_sections", "personal_rule_sections"):
        for src, ids in data[field].items():
            if not ids or set(ids) - set(data["rule_ids"]):
                raise ValueError(f"unmapped rule section: {src}")
    return data


def check_source(source, data):
    entries = json.loads((source / "catalog.json").read_text("utf8"))["entries"]
    catalog = {e["name"] for e in entries if e["category"] == "skill"}
    disk = {p.parent.name for p in (source / "skills").glob("*/SKILL.md")}
    compare("upstream catalog vs files", catalog, disk)
    compare("unreviewed or removed upstream skills", disk, data["upstream_skills"])
    rules = (source / data["upstream"]["rules_file"]).read_text("utf-8-sig")
    headings = {m.group(1).strip() for m in re.finditer(r"^#{1,3} (.+)$", rules, re.M)}
    compare("upstream rule sections", headings, data["rule_sections"])
    compare("upstream content hashes", {f"skills/{n}/SKILL.md" for n in disk}
            | {data["upstream"]["rules_file"]}, data["upstream_hashes"])
    trees = subprocess.check_output(["git", "-C", str(source), "ls-tree", "HEAD:skills"],
                                    encoding="utf8").splitlines()
    actual = {path: header.split()[2] for row in trees for header, path in [row.split("\t", 1)]
              if path in disk and header.startswith("040000 tree ")}
    compare("upstream skill tree inventory", disk, data["upstream_skill_trees"])
    changed = [n for n, digest in data["upstream_skill_trees"].items() if actual.get(n) != digest]
    if changed:
        raise ValueError("upstream skill files changed; review: " + ", ".join(sorted(changed)))
    for name, old in data["upstream_hashes"].items():
        body = (source / name).read_bytes().replace(b"\r\n", b"\n")
        if hashlib.sha256(body).hexdigest() != old:
            raise ValueError(f"source changed; review portable behavior: {name}")


def check_personal(roots, data):
    actual = {page.parent.name for root in roots for page in root.glob("*/SKILL.md")
              if not page.parent.name.startswith(".")}
    compare("personal skills", actual, data["personal_skills"])


def check_personal_rules(path, data):
    page = path.read_text("utf-8-sig")
    headings = {h.strip() for h in re.findall(r"^#{1,2} (.+)$", page, re.M)}
    compare("personal rule sections", headings, data["personal_rule_sections"])


def check_zip(path, root):
    out = subprocess.run(["git", "-C", str(root), "ls-files", "-z"], check=True, capture_output=True)
    tracked = {s for s in out.stdout.decode("utf8").split("\0") if s}
    with zipfile.ZipFile(path) as zf:
        members = [i.filename for i in zf.infolist() if not i.is_dir()]
        if len(set(members)) != len(members):
            raise ValueError("ZIP has duplicate members")
        prefix = ""
        if "inventory.json" not in members:
            prefixes = {n.split("/", 1)[0] for n in members}
            if len(prefixes) != 1:
                raise ValueError("ZIP needs one release root")
            prefix = next(iter(prefixes)) + "/"
        paths = {n.removeprefix(prefix) for n in members}
        compare("release ZIP", tracked, paths)
        for rel in sorted(tracked):
            want = (root / rel).read_bytes()
            if zf.read(prefix + rel) != want:
                raise ValueError(f"release ZIP bytes differ: {rel}")


def main():
    cli = argparse.ArgumentParser(description=__doc__)
    cli.add_argument("--root", type=Path, default=ROOT)
    cli.add_argument("--upstream", type=Path)
    cli.add_argument("--personal-skills", type=Path, nargs="+")
    cli.add_argument("--personal-rules", type=Path)
    cli.add_argument("--zip", type=Path)
    args = cli.parse_args()
    try:
        data = check_tree(args.root)
        if args.upstream:
            check_source(args.upstream, data)
        if args.personal_skills:
            check_personal(args.personal_skills, data)
        if args.personal_rules:
            check_personal_rules(args.personal_rules, data)
        if args.zip:
            check_zip(args.zip, args.root)
        print(f"Verified {len(data['skills'])} skill entries and {len(data['rule_ids'])} rules in both languages.")
    except (ValueError, KeyError, OSError, subprocess.CalledProcessError, zipfile.BadZipFile) as exc:
        cli.exit(1, str(exc) + "\n")


if __name__ == "__main__":
    main()
