# Development and testing

[简体中文](development.md) · [Home](../README.en.md)

Put each skill in its own folder and match that folder name in the `name` field of `SKILL.md`. Its description should say when it helps and when to skip it. Put detailed steps in `references/`.

For script changes, explain dependencies, arguments, what the script writes, and how it handles conflicts. Keep cases that distinguish expected behavior from failure. For example, installing over an existing skill should fail without changing its files. Update the Chinese and English guides together.

```text
python -m pip install -r requirements-visual.txt
python -m unittest discover -s tests -v
```

The tests run installs, removals, and link checks in temporary projects. Check skill discovery and project instructions separately in Codex. For MCP, make a real documentation query: appearing in the connection list only shows that the server is configured.

## Writing the guides

Follow the reading order used by Qoder: say what the pack is for, offer a download, list what is included, then show the first install commands. Keep upgrades, troubleshooting and sources in their own guides. Use the same order, version, counts and examples in both languages. When adding skills or rules, update both catalogs and the release notes. Examples should need only a project path and tell readers what to expect.

## Release checks

Compare the candidate with an independent checkout of the upstream repository. The release check takes a path, so it can also inspect an updated upstream before its revision is accepted. The optional `--personal-skills` argument takes one or more local skill roots; compare the maintainer's own sources before release without sharing personal files. Use `--personal-rules` for the local working agreement. Review changed sources before updating their recorded hashes. Once the changes have been committed, run:

```text
python -X utf8 scripts/check_coverage.py --upstream /path/to/Qoder-Optimization
python -X utf8 scripts/build_release.py --output Codex-Optimization.zip
```

Build into a new output path. The command checks the file list and contents inside the ZIP. CI runs the checks on Windows and Linux; the release workflow also compares the current upstream branch. Install the ZIP into a clean project and confirm Codex discovers its skills and reads each chosen rule template before publishing.

## Troubleshooting

If a skill with the same name is already installed, try the pack in another project or resolve the conflict first. After an interrupted install, inspect the receipt and files under the target `.agents/skills` folder. Back up your own files and confirm which files belong to the pack before removing any. Do not delete the whole skills folder.

Before publishing, inspect the commit and the ZIP for account data, secrets, or local workspace files. See `VERSION` for the current version.
