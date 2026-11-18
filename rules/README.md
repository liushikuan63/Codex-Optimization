# 项目规则：告诉 Codex 在这个仓库怎么工作

[English](README.en.md) · [返回首页](../README.md)

`AGENTS.md` 适合放团队希望反复遵守的工作约定，例如改动前先查清当前状态，报告测试时写清分支、运行范围，以及哪些步骤没验证。它是给 Codex 的项目说明，不能代替 CI 或命令权限控制。

选一份模板：[中文版](AGENTS.zh-CN.example.md) 或 [英文版](AGENTS.en.example.md)。新项目可以把模板内容放入仓库根目录的 `AGENTS.md`；已有文件时，把需要的段落合并进去，并保留项目自己的构建、测试和发布约定。模板中的提示注释可以换成仓库的真实命令。

在目标仓库开启新 Codex 会话。让它说明读到的项目约定，再用一件小任务检查它是否遵守。取消时移除本次加入的段落即可。[Codex 官方 AGENTS.md 指南](https://developers.openai.com/codex/guides/agents-md)
