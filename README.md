# Codex-Optimization

[English](README.en.md) · [下载最新版](https://github.com/liushikuan63/Codex-Optimization/releases/latest)

让 Codex 更扎实地做开发工作：评审方案时，找出“测试全过，但旧入口漏了”的情况；排查网页时，即使请求返回 HTTP 200，也继续判断为什么页面还在转圈。

| 你想做什么 | 从这里开始 |
| --- | --- |
| 让 Codex 按步骤评审、排查或验收 | [安装技能](#安装并试用) |
| 让 Codex 查公开的框架或 API 文档 | [接入 MCP](mcp/README.md) |
| 让 Codex 在项目中遵守团队约定 | [使用项目规则](rules/README.md) |

三部分可以分别使用。安装技能不会改变项目规则，也不会自动接入 MCP。

## 安装并试用

1. 从 [发布页](https://github.com/liushikuan63/Codex-Optimization/releases/latest) 下载并解压 ZIP，在解压目录打开终端。需要 Python 3.12 或更新版本。
2. 将下面的 `<项目目录>` 换成你要使用技能的仓库。第一条命令只检查，第二条才安装。

   ```text
   python scripts/manage_skills.py plan --project "<项目目录>"
   python scripts/manage_skills.py install --project "<项目目录>"
   ```

3. 在目标项目开启新 Codex 会话，试着说：**“用 $csp-plan-review 看看这个迁移方案：有没有测试全过，仍会丢数据的情况？”**

项目安装写入目标仓库的 `.agents/skills`。想在自己的所有项目里用，把 `--project "<项目目录>"` 换成 `--user`。安装会保留已有技能。只有运行截图裁切脚本才需要 Pillow，可在现有 Python 环境执行 `python -m pip install -r requirements-visual.txt`。

## 技能清单

| 技能 | 适用场景 |
| --- | --- |
| [方案评审](skills/csp-plan-review/SKILL.md) | 实施前找方案漏洞，补上能抓住问题的验收条件 |
| [浏览器验收](skills/csp-browser-acceptance/SKILL.md) | 验收页面改动，或排查白屏、一直加载 |
| [截图细查](skills/csp-visual-detail/SKILL.md) | 看清小字、单像素边线和前后差异 |
| [交付验收](skills/csp-delivery-evidence/SKILL.md) | 把需求与待交付版本的实际验证结果对应起来 |
| [Windows 工程验证](skills/csp-windows-workflow/SKILL.md) | 排查命令行差异、批量改写和偶发测试失败 |
| [VibeCoding 批次](skills/csp-vibecoding-batch/SKILL.md) | 给已有任务计划追加工作，补齐依赖和验收 |
| [技能吸纳](skills/csp-skill-adoption/SKILL.md) | 把外部技能带入 Codex 前，检查来源和用法 |

技能正文目前是中文，可以要求 Codex 用英文汇报。

## 卸载或升级

从解压目录运行 `python scripts/manage_skills.py uninstall --project "<项目目录>"`（若之前用的是 `--user`，这里也用它）。升级时先卸载旧版，再装新版。发现文件被修改时，卸载会先停止；请先备份自己的修改。若上次操作中断，可查看技能目录里的 `.codex-optimization-install.json`，按[排查说明](docs/development.md#问题排查)处理。

[开发与验证](docs/development.md) · [来源与说明](docs/provenance.md) · [MIT 许可证](LICENSE)。本项目独立维护，并非 OpenAI 官方发行版。
