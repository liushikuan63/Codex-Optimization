---
name: csp-task-handoff
description: 用于中断、跨会话接续或写入者冲突。 Use to hand off interrupted work or resolve writer ownership.
---

# 长任务交接与恢复 | Task handoff and recovery

沿现有任务卡记录目标、授权、提交、脏文件、运行实例、首个失败、已验证和未验证，以及下一条具体操作。只留必要事实，避免完整聊天或凭据。

在接收会话中复核实际工作区、运行产物和写入者。释放旧写入者后，从新会话完成一个真实步骤并读回结果。不能确认归属时保留现场，创建会话不等于接管成功。

按场景查找：[任务示例 / Worked examples](references/applied-methods.md)。

## English

Use the existing task record for the goal, authorization, revision, dirty files, running instance, first failure, verified results and next executable step. Keep credentials and transcripts out of the handoff.

Recheck the checkout, running artifact and writer in the receiving session. Release the old writer before editing. Perform one real step from the new session and read back the result. A new chat ID does not prove takeover.
