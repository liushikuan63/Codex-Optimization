# Installation guide

[简体中文](install.md) · [Home](../README.en.md) · [Skill catalog](skills.en.md)

## Download and verify

Download the ZIP and its `.sha256` file from the [same release](https://github.com/liushikuan63/Codex-Optimization/releases/latest). On Windows, run `Get-FileHash -Algorithm SHA256 -LiteralPath 'Codex-Optimization-v0.3.1.zip'` and compare the result with the checksum. On Linux, run `sha256sum -c Codex-Optimization-v0.3.1.zip.sha256` in the download directory. Substitute the filename for your version. Extract the verified archive, then open a terminal in the folder containing `VERSION` and `scripts`.

## Choose where to install

Run `python --version` and check that you have 3.12 or later. Start with one project. Preview the destination and any name conflicts, then install:

```text
python scripts/manage_skills.py plan --project "<project-folder>"
python scripts/manage_skills.py install --project "<project-folder>"
```

Use an existing project directory. This writes to its `.agents/skills`. To make the skills available across projects for your account, replace `--project "<project-folder>"` with `--user` in both commands. A conflicting directory or an existing receipt stops installation and preserves the existing files.

## Check that it works

Run `python scripts/manage_skills.py verify --project "<project-folder>"` or use `--user` to check your account installation. The command reads existing files and prints the checked directory, the pack and receipt versions, and conflicting paths. Exit codes:

| Exit code | Status | Meaning |
| --- | --- | --- |
| 0 | `VERIFIED` | The receipt and skill files in the selected scope match this pack |
| 2 | `NOT_INSTALLED`, `CONFLICT`, `DIFFERENT_VERSION` | Nothing installed here, a conflict, or a receipt from another version |
| 1 | `BLOCKED` or error | Invalid receipt, unsafe path, or a file read error |

Unrelated skills are ignored. A matching folder without a receipt does not count as an installation from this pack. `verify` does not repair edited files or confirm Codex has discovered the skills.

Open a new Codex session in the project. Find `csp-plan-review` in the skill list and try it with a plan. To adopt rules, select the clauses you want from the [rules guide](../rules/README.en.md). For documentation lookup, choose a connection from the [MCP guide](../mcp/README.en.md) and try a query. Install Pillow with `python -m pip install -r requirements-visual.txt` only if you use the screenshot crop script.

## Update or remove

From the pack directory, run:

```text
python scripts/manage_skills.py uninstall --project "<project-folder>"
```

Use the same project path or `--user` as the original installation. To update, uninstall the old version first. After removal succeeds, run `plan`, `install` and `verify` from the new pack. Removal stops if a managed file was edited. Back up your edits outside the skill directory before choosing whether to keep the customized copy or restore the original and upgrade. For interrupted installations, see [troubleshooting](development.en.md#troubleshooting).
