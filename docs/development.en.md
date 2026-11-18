# Development and testing

[简体中文](development.md) · [Home](../README.en.md)

Put each skill in its own folder and match that folder name in the `name` field of `SKILL.md`. Its description should say when it helps and when to skip it. Put detailed steps in `references/`.

For script changes, explain dependencies, arguments, what the script writes, and how it handles conflicts. Keep cases that distinguish expected behavior from failure. For example, installing over an existing skill should fail without changing its files. Update the Chinese and English guides together.

```text
python -m pip install -r requirements-visual.txt
python -m unittest discover -s tests -v
```

The tests run installs, removals, and link checks in temporary projects. Check skill discovery and project instructions separately in Codex. For MCP, make a real documentation query: appearing in the connection list only shows that the server is configured.

## Troubleshooting

If a skill with the same name is already installed, try the pack in another project or resolve the conflict first. After an interrupted install, inspect the receipt and files under the target `.agents/skills` folder. Back up your own files and confirm which files belong to the pack before removing any. Do not delete the whole skills folder.

Before publishing, inspect the commit and the ZIP for account data, secrets, or local workspace files. See `VERSION` for the current version.
