# Installation guide

[简体中文](install.md) · [Home](../README.en.md) · [Skill catalog](skills.en.md)

## Download and verify

Download the ZIP and its `.sha256` file from the [same release](https://github.com/liushikuan63/Codex-Optimization/releases/latest). On Windows, run `Get-FileHash -Algorithm SHA256 -LiteralPath 'Codex-Optimization-v0.3.0.zip'` and compare the result with the checksum. On Linux, run `sha256sum -c Codex-Optimization-v0.3.0.zip.sha256` in the download directory. Substitute the filename for your version. Extract the verified archive, then open a terminal in the folder containing `VERSION` and `scripts`.

## Choose where to install

Run `python --version` and check that you have 3.12 or later. Start with one project. Preview the destination and any name conflicts, then install:

```text
python scripts/manage_skills.py plan --project "<project-folder>"
python scripts/manage_skills.py install --project "<project-folder>"
```

Use an existing project directory. This writes to its `.agents/skills`. To make the skills available across projects for your account, replace `--project "<project-folder>"` with `--user` in both commands. A conflicting directory or an existing receipt stops installation and preserves the existing files.

## Check that it works

Open a new Codex session in the project. Find `csp-plan-review` in the skill list and try it with a plan. To adopt rules, select the clauses you want from the [rules guide](../rules/README.en.md). For documentation lookup, choose a connection from the [MCP guide](../mcp/README.en.md) and try a query. Install Pillow with `python -m pip install -r requirements-visual.txt` only if you use the screenshot crop script.

## Update or remove

From the pack directory, run:

```text
python scripts/manage_skills.py uninstall --project "<project-folder>"
```

Use the same project path or `--user` as the original installation. To update from 0.2.0, uninstall the old version first. After removal succeeds, run `plan` and `install` from the new pack. Removal stops if a managed file was edited. Back up your edits outside the skill directory before choosing whether to keep the customized copy or restore the original and upgrade. For interrupted installations, see [troubleshooting](development.en.md#troubleshooting).
