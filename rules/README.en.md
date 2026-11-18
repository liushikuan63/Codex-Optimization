# Project rules: Tell Codex how to work in your repository

[简体中文](README.md) · [Home](../README.en.md)

Use `AGENTS.md` for instructions the team wants Codex to follow repeatedly. For example, tell it to check the working tree before editing and report which tests ran and what remains unverified. Project instructions do not enforce shell permissions or replace CI.

Choose the [English template](AGENTS.en.example.md) or [Chinese template](AGENTS.zh-CN.example.md). For a new file, put the chosen text in `AGENTS.md` at the repository root. If the repository already has one, merge only what you need and keep the team's build, test, and release instructions. Replace the comment with the real commands for your project.

Start a new session in the target repository. Ask Codex which project instructions it read, then check them on a small task. To undo the change, remove only the sections you added. See the [official AGENTS.md guide](https://developers.openai.com/codex/guides/agents-md).
