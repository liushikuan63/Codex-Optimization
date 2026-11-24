# Codex-Optimization

**一套按需使用的 Codex 开发工具包。** 用项目规则说明团队怎么工作，用技能引导一次具体任务，用可选的 MCP 连接查阅公开文档。

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.12%2B-blue.svg)](docs/install.md)

[English](README.en.md) | 简体中文 · [安装说明](docs/install.md) · [技能清单](docs/skills.md) · [来源索引](inventory.json)

## 下载

无需克隆仓库。在[发布页](https://github.com/liushikuan63/Codex-Optimization/releases/latest)下载 ZIP 和同名的 `.sha256` 校验文件，解压 ZIP 即可开始。历史版本见[全部发布](https://github.com/liushikuan63/Codex-Optimization/releases)。

| 版本 | 主要变化 | 下载 |
| --- | --- | --- |
| 0.3.2 | 只读核对技能安装位置、版本和冲突；补充双语交付与浏览器验收规则 | [发布包](https://github.com/liushikuan63/Codex-Optimization/releases/download/v0.3.2/Codex-Optimization-v0.3.2.zip) · [版本说明](https://github.com/liushikuan63/Codex-Optimization/releases/tag/v0.3.2) |
| 0.3.0 | 32 项双语技能、22 条项目规则；发布时核对来源清单和 ZIP 内容 | [发布包](https://github.com/liushikuan63/Codex-Optimization/releases/download/v0.3.0/Codex-Optimization-v0.3.0.zip) · [版本说明](https://github.com/liushikuan63/Codex-Optimization/releases/tag/v0.3.0) |
| 0.2.0 | 首次提供双语指南、项目规则示例和 MCP 示例 | [版本说明](https://github.com/liushikuan63/Codex-Optimization/releases/tag/v0.2.0) |

## 包里有什么

| 内容 | 数量 | 何时使用 |
| --- | ---: | --- |
| [技能](docs/skills.md) | 32 | 为一次任务选择做法，例如评审迁移、排查页面一直加载、验收发布包 |
| [项目规则](rules/README.md) | 22 条，中英文各一份 | 把团队长期遵守的条款放进项目的 `AGENTS.md` |
| [MCP 示例](mcp/README.md) | 2 | 需要当前的 OpenAI 或第三方库文档时，选择相应连接 |

三部分可以单独使用。安装器只安装技能；规则由项目选择，MCP 由使用者单独配置。

## 快速开始

在解压目录打开终端。把 `<项目目录>` 换成一个已经存在的项目路径，预览、安装并核对：

```text
python scripts/manage_skills.py plan --project "<项目目录>"
python scripts/manage_skills.py install --project "<项目目录>"
python scripts/manage_skills.py verify --project "<项目目录>"
```

在目标项目里打开新的 Codex 会话，试一句：“用 $csp-plan-review 看看这个迁移方案：有没有测试通过、旧客户端却读不到数据的情况？” 技能安装在该项目的 `.agents/skills`。

## 环境与使用范围

安装器需要 Python 3.12 或更高版本；只有截图裁切工具依赖 Pillow。面向所有项目的安装、旧版升级、修改冲突和卸载见[安装说明](docs/install.md)。哪些做法取自 Qoder，哪些只适用于原工具，见[来源与适用范围](docs/provenance.md)。

[开发与验证](docs/development.md) · [版本记录](CHANGELOG.md) · [MIT 许可证](LICENSE)。本项目独立维护，并非 OpenAI 官方发行版。
