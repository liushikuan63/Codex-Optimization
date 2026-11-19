# 安装说明

[English](install.en.md) · [返回首页](../README.md) · [技能清单](skills.md)

## 下载并校验

从[同一版本的发布页](https://github.com/liushikuan63/Codex-Optimization/releases/latest)下载 ZIP 和 `.sha256` 文件。Windows 可用 `Get-FileHash -Algorithm SHA256 -LiteralPath 'Codex-Optimization-v0.3.0.zip'`；Linux 可在下载目录运行 `sha256sum -c Codex-Optimization-v0.3.0.zip.sha256`。校验一致后解压，在包含 `VERSION` 和 `scripts` 的目录运行下面的命令。其他版本请替换文件名。

## 选择安装位置

先运行 `python --version`，确认版本至少为 3.12。试用时建议装进单个项目：先用 `plan` 检查路径和同名冲突，再用 `install` 写入。

```text
python scripts/manage_skills.py plan --project "<项目目录>"
python scripts/manage_skills.py install --project "<项目目录>"
```

项目目录须已存在。项目安装写入 `.agents/skills`；希望当前账号的所有项目都能用时，将两条命令里的 `--project "<项目目录>"` 都换成 `--user`。同名目录或旧收据会使安装停止，已有文件保留。

## 确认能用

在目标项目新开 Codex 会话，从技能列表找 `csp-plan-review`，再给它一份方案试用。想采用规则，按[规则说明](../rules/README.md)合并适用条款；想接入文档查询，按 [MCP 说明](../mcp/README.md)选择连接并实际查一次。仅运行截图裁切脚本时，才需要 `python -m pip install -r requirements-visual.txt`。

## 升级与卸载

从分享包目录运行：

```text
python scripts/manage_skills.py uninstall --project "<项目目录>"
```

使用与原安装相同的项目路径或 `--user`。从 0.2.0 升级时，先卸载旧版，确认卸载成功，再从新版目录运行 `plan` 和 `install`。卸载发现被修改的文件就会停止。先把自己的改动备份到技能目录外，再决定保留定制版还是恢复原版后升级。若安装被中断，见[问题排查](development.md#问题排查)。
