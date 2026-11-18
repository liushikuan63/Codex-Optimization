# Codex-Optimization

[简体中文](README.md) · [Download](https://github.com/liushikuan63/Codex-Optimization/releases/latest)

Codex-Optimization helps Codex review plans, check changes, and show the evidence behind its work. For example, it can help spot a migration that passes its tests while skipping an old entry point, or a page that shows a spinner even though the server returns HTTP 200.

| Start here | What it does |
| --- | --- |
| [Skills](#skills) | Give Codex a workflow for a specific task, such as reviewing a plan or testing a page. |
| [MCP setup](mcp/README.en.md) | Let Codex look up public documentation when it needs current API details. |
| [Project rules](rules/README.en.md) | Tell Codex how to work in a repository through an `AGENTS.md` file. |

The three parts are independent. You can use one without installing the others.

## Install and try a skill

1. Download and extract the ZIP from [Releases](https://github.com/liushikuan63/Codex-Optimization/releases/latest). Open a terminal in the extracted folder. You need Python 3.12 or later.
2. Replace `<project-folder>` with the repository where you want to use the skills. Run the first command to see what will happen, then run the second to install.

   ```text
   python scripts/manage_skills.py plan --project "<project-folder>"
   python scripts/manage_skills.py install --project "<project-folder>"
   ```

3. Open a new Codex session in that project and try: **“Use $csp-plan-review to find a way this migration could pass its tests but still lose data.”**

Project installation writes to `.agents/skills` inside that project. For all projects on your account, use `--user` in place of `--project "<project-folder>"`. The installer leaves existing skills alone and does not enable MCP or install rules. To use the screenshot crop script, install Pillow in your existing Python environment with `python -m pip install -r requirements-visual.txt`.

## Skills

| Skill | When to use it |
| --- | --- |
| [Plan review](skills/csp-plan-review/SKILL.md) | Before a change: find gaps in the plan and tests that would miss them. |
| [Browser checks](skills/csp-browser-acceptance/SKILL.md) | After a UI change, or when a page stays blank or keeps loading. |
| [Screenshot details](skills/csp-visual-detail/SKILL.md) | Inspect small text, a one-pixel border, or a local change in an image. |
| [Delivery checks](skills/csp-delivery-evidence/SKILL.md) | Match requirements to evidence from the version you plan to ship. |
| [Windows workflow](skills/csp-windows-workflow/SKILL.md) | Diagnose shell, bulk text edit, or intermittent test failures. |
| [VibeCoding batches](skills/csp-vibecoding-batch/SKILL.md) | Add work to an existing VibeCoding plan without losing links or checks. |
| [Skill adoption](skills/csp-skill-adoption/SKILL.md) | Review a skill collection before bringing it into Codex. |

Skill instructions are currently in Chinese; Codex can report back in English.

## Remove or update

From the pack folder, run `python scripts/manage_skills.py uninstall --project "<project-folder>"` (or use the same `--user` option as before). Install the new version after removing the old one. If an installed file was edited, the command stops before removing the pack. Back up your edits before resolving the conflict. If an install was interrupted, check the skill folder for `.codex-optimization-install.json` and see [troubleshooting](docs/development.en.md#troubleshooting).

[Development](docs/development.en.md) · [Sources](docs/provenance.en.md) · [MIT License](LICENSE). An independent project, not an official OpenAI distribution.
