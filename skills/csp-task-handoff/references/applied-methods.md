# 任务示例 | Worked examples

下表按来源列出本技能吸纳的具体做法。每项用目标项目自己的数据验证。
Each row identifies a method retained from its source. Use representative data from the target project.

| 来源技能 / Source | 中文操作示例 | Worked example |
| --- | --- | --- |
| `continuation-state-audit`, `long-task-merge-takeover` | 接手时读出当前分支、未提交文件、合并状态和仍在运行的测试；与交接记录核对后，只执行第一个未验证步骤。 | Read the current branch, uncommitted files, merge state and active tests. Reconcile them with the handoff before running the first unverified step. |
| `goal-driven-execution`, `injected-context-slimming` | 把长任务写成可失败的完成条件。交接只带仍有效的约束、证据位置和第一项未完成工作；后台进程必须读到退出结果才能解除后续依赖。 | Give a long task falsifiable completion criteria. Carry forward only active constraints, evidence locations and the first unfinished action. Wait for actual exit results before releasing dependent work. |
