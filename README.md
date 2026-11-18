# Codex-Optimization

一组面向 Codex 的中文开发技能。把方案、浏览器、测试和交付中的常见误判，变成按需调用的检查流程。每项技能可以单独阅读；整包也可以装在单个项目中试用。

| 技能 | 适用场景 |
| --- | --- |
| [csp-plan-review](skills/csp-plan-review/SKILL.md) | 用反例评审开发方案、迁移顺序和验收条件 |
| [csp-browser-acceptance](skills/csp-browser-acceptance/SKILL.md) | 受影响入口、宽高布局、真实交互、SPA 白屏和持续加载 |
| [csp-visual-detail](skills/csp-visual-detail/SKILL.md) | 从截图原像素裁切并放大细字、边线和局部差异 |
| [csp-delivery-evidence](skills/csp-delivery-evidence/SKILL.md) | 对齐需求和最终证据，审查上线、安装及生成物 |
| [csp-windows-workflow](skills/csp-windows-workflow/SKILL.md) | Windows 工具链、批量文本预检、间歇套件失败 |
| [csp-vibecoding-batch](skills/csp-vibecoding-batch/SKILL.md) | 给现有 VibeCoding 批次追加任务设计、依赖和验收 |
| [csp-skill-adoption](skills/csp-skill-adoption/SKILL.md) | 审查和移植技能集合，检查本地引用与发现路径 |

## 安装与使用

需要 Python 3.12 或更新版本。以项目内安装为例，从发布源码目录运行：

```text
python scripts/manage_skills.py plan --project "<项目目录>"
python scripts/manage_skills.py install --project "<项目目录>"
```

目标是该项目的 `.agents/skills`。需要用户级安装时，将 `--project "<项目目录>"` 改为 `--user`，目标是 `~/.agents/skills`。不指定时使用执行命令的当前目录。安装器使用 Python 标准库，不写 Codex 配置、不注册 hook 或 MCP，也不读取账户、聊天或记忆。

在以目标项目为工作目录的 Codex 中刷新技能列表或开启新会话，通过技能选择器或 `$csp-plan-review` 等技能名显式调用。比如让它审查迁移方案中“即使有缺陷也能通过验收”的路径。自动选用取决于当前宿主和对话，安装成功不证明自动触发。

只有调用图片裁切脚本才需要 Pillow；可以在现有隔离环境安装 `requirements-visual.txt`。浏览器验收使用目标项目已有的浏览器能力。

## 卸载与更新

```text
python scripts/manage_skills.py uninstall --project "<项目目录>"
```

使用安装时的同一作用域。卸载只处理安装收据中登记且完整匹配的文件；如有修改或额外文件，先自行保留这些变更再决定如何处理。更新前卸载旧包再安装新包。不要对同一目标并行运行安装、卸载或手动编辑。若操作中断，先检查目标的 `.codex-optimization-install.json` 及技能目录；不确定归属时不要删除或重跑。

运行 `python -m unittest discover -s tests -v` 验证安装生命周期和技能引用。贡献方法见 [开发说明](docs/development.md)，来源与取舍见 [来源说明](docs/provenance.md)。本项目以 [MIT](LICENSE) 发布，与 OpenAI 官方 Codex 项目独立。
