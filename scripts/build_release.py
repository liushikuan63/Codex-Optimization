"""Build a ZIP of the reviewed commit and compare it with the release checkout."""
import argparse
import hashlib
import shutil
from pathlib import Path
import subprocess
import tempfile

from check_coverage import ROOT, check_tree, check_zip


def git(*args):
    return subprocess.check_output(["git", "-C", str(ROOT), *args])


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    output = args.output.resolve()
    if output.exists():
        parser.exit(1, f"Output already exists: {output}\n")
    if git("status", "--porcelain", "--untracked-files=no").strip():
        parser.exit(1, "Commit the reviewed tracked files before building the release.\n")
    check_tree(ROOT)
    version = (ROOT / "VERSION").read_text("utf8").strip()
    with tempfile.TemporaryDirectory(dir=output.parent) as temp:
        archive = Path(temp) / "package.zip"
        git("archive", "--format=zip", f"--prefix=Codex-Optimization-{version}/",
            f"--output={archive}", "HEAD")
        check_zip(archive, ROOT)
        # Publish only after all checks have succeeded; an existing output belongs to its owner.
        with archive.open("rb") as read, output.open("xb") as write:
            shutil.copyfileobj(read, write)
    with output.open("rb") as result:
        print(f"{hashlib.file_digest(result, 'sha256').hexdigest()}  {output.name}")


if __name__ == "__main__":
    main()
