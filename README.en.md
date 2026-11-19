# Codex-Optimization

**An opt-in toolkit for working with Codex.** Project rules describe how a team works, skills guide a specific task, and optional MCP connections provide current public documentation.

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.12%2B-blue.svg)](docs/install.en.md)

English | [简体中文](README.md) · [Install guide](docs/install.en.md) · [Skill catalog](docs/skills.en.md) · [Source index](inventory.json)

## Download

No clone required. Download the ZIP and its matching `.sha256` file from the [latest release](https://github.com/liushikuan63/Codex-Optimization/releases/latest), then extract the ZIP. See [all releases](https://github.com/liushikuan63/Codex-Optimization/releases) for older versions.

| Version | Highlights | Download |
| --- | --- | --- |
| 0.3.0 | 32 bilingual skills, 22 project rules, and checks that compare the source inventory with the release ZIP | [ZIP](https://github.com/liushikuan63/Codex-Optimization/releases/download/v0.3.0/Codex-Optimization-v0.3.0.zip) · [Release notes](https://github.com/liushikuan63/Codex-Optimization/releases/tag/v0.3.0) |
| 0.2.0 | First bilingual guides, project rule examples and MCP examples | [Release notes](https://github.com/liushikuan63/Codex-Optimization/releases/tag/v0.2.0) |

## What's included

| Component | Count | When to use it |
| --- | ---: | --- |
| [Skills](docs/skills.en.md) | 32 | Choose a workflow for a task, such as reviewing a migration, diagnosing a loading page or testing a release |
| [Project rules](rules/README.en.md) | 22, in both languages | Choose standing team agreements for the project's `AGENTS.md` |
| [MCP examples](mcp/README.en.md) | 2 | Look up current OpenAI or third-party library documentation |

The three parts work independently. The installer adds skills. Each project chooses its rules, and each user configures the MCP connections they want.

## Get started

Open a terminal in the extracted folder. Replace `<project-folder>` with an existing project directory. Preview the installation, then install:

```text
python scripts/manage_skills.py plan --project "<project-folder>"
python scripts/manage_skills.py install --project "<project-folder>"
```

Open a new Codex session in that project and try: “Use $csp-plan-review to find a way this migration could pass its tests while an old client can no longer read its data.” Project skills live in `.agents/skills`.

## Requirements and limits

The installer needs Python 3.12 or later. Only the screenshot crop tool needs Pillow. The [install guide](docs/install.en.md) covers account-wide installation, upgrades, conflicts and removal. See [sources and scope](docs/provenance.en.md) for what was adapted from Qoder and what still needs the original tool.

[Development and testing](docs/development.en.md) · [Changelog](CHANGELOG.md) · [MIT License](LICENSE). This is an independent project, not an official OpenAI distribution.
