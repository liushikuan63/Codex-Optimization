---
name: csp-ci-evidence
description: 用于 GitHub Actions 失败、排队或重复构建。 Use for failing jobs, stalled runners and CI cost investigations.
---

# CI 失败与成本 | CI failures and cost

记下提交、run、attempt、工作流、runner 和首个失败步骤。若没有步骤启动，查看检查注释、权限和 runner 状态，与一次可比的成功运行对照；没有日志不能证明配额用尽。

改缓存或路径过滤前，从工作流追到脚本和实际输入。分别验证命中和未命中的情况，确认测试确实执行。区分运行时间、计费分钟和实付费用。

按场景查找：[任务示例 / Worked examples](references/applied-methods.md)。

## English

Record the commit, run, attempt, workflow, runner and first failing step. If no step started, inspect check annotations, permissions and runner availability; compare a similar successful run. Missing logs alone do not establish a quota problem.

Trace scripts and build inputs before changing cache keys or path filters. Exercise both a hit and a miss and confirm tests actually ran. Separate runtime, billed minutes and actual charges.
