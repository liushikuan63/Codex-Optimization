# 来源与适用范围

[English](provenance.en.md) · [返回首页](../README.md)

这一版对照了三类来源：维护者使用的可移植 Codex 技能、通用工作约定，以及 [Qoder 的固定版本](https://github.com/liushikuan63/Qoder-Optimization/tree/9f39002a6e6713f1eb5c868ab61ad8608a1771a5)。[来源清单](../inventory.json)逐项记录每个已审查技能源自哪里、对应哪个可安装技能，或为什么保留在上游。要找实际用法，先看[技能目录](skills.md)或[项目规则模板](../rules/AGENTS.zh-CN.example.md)。

相近的方法按任务合并。例如，“消息投递与重试”会让你模拟业务已提交、消息尚未确认的情况，重投后检查业务是否只执行一次；使用这项技能不需要安装上游整套 Kafka 或 RabbitMQ 工具。“浏览器验收”会检查启动脚本实际返回什么，避免把返回 HTML 的 HTTP 200 当成脚本加载成功。

清单中，`adapted` 表示抽取了可复用的方法，原技能、素材和脚本并未整套移植。`upstream-only` 表示包中没有该工具或流程，两种语言都给出原因。规则对照保留通用做法；机器路径、账号设置、宿主权限和 hook 仍属于原环境。两份可选的 [MCP 接入示例](../mcp/README.md) 独立于技能安装。

0.3.1 将 Qoder 的通俗交付说明、已有排障证据和布局负对照整理进双语规则与技能。安装后用收据核对文件的做法参考 [DSH-Optimization 的部署说明](https://github.com/liushikuan63/DSH-Optimization/blob/fa1a2c9246984cb226d54e9a0fde00fe140d7d03/docs/deployment.md)；核对由本包的 Python 安装器实现。

本工程和上述 Qoder 版本使用 [MIT 许可证](../LICENSE)。技能按 Codex 的用法编写。上游的部分工程技能还注明来自 ECC 和 Compound Engineering，两份许可分别保存在 [ECC](../notices/LICENSE-ECC.txt) 和 [Compound Engineering](../notices/LICENSE-CE.txt)。包内不再分发第三方设计素材库或上游的整套工具。
