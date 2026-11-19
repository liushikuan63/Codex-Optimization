---
name: csp-windows-workflow
description: 处理 Windows 项目的工具链与跨 Shell 问题、批量文本改写或间歇套件失败；用于构建验证和已出现的差异，不替换仓库自带的标准流程。
---

# Windows 项目验证

- 定位实际项目和模块，检查项目指令、工作树、锁文件和 CI。使用仓库声明的 wrapper 和包管理器，确认当前进程使用的实际解释器；不要为单个仓库改全机版本。
- PowerShell/Git Bash 的参数、编码或退出码异常，按 [跨 Shell 诊断](references/windows-shell-boundaries.md) 对照实际解释器、argv、原始字节和退出码。
- 同构批量替换和固定列编辑先做 [批量改写预检](references/structured-edit-preflight.md)，核对锚点、当前快照和编码。
- 仅聚合或并行套件偶发失败时按 [间歇失败诊断](references/intermittent-suite-failures.md) 保留首红、复制同一运行条件并逐项排查；单独执行通过只用于定位。
- 实际报告执行、失败和跳过数量。当运行替身或只编译时保留边界。

按场景查找：[任务示例 / Worked examples](references/applied-methods.md)。

## English

Locate the checkout, required versions and actual shell. Distinguish PowerShell, cmd, Git Bash and WSL. Preserve paths, encoding and line endings. Before bulk edits check anchor counts and existing changes. For intermittent tests keep the first failure, match the runner and vary one factor at a time.
