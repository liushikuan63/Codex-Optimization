# 任务示例 | Worked examples

下表按来源列出本技能吸纳的具体做法。每项用目标项目自己的数据验证。
Each row identifies a method retained from its source. Use representative data from the target project.

| 来源技能 / Source | 中文操作示例 | Worked example |
| --- | --- | --- |
| `audit-ci-cost-levers` | 选一段可比的运行历史，按事件、矩阵、重试和实际 runner 分钟汇总；分别估算取消重复运行或复用缓存节省的时间。 | Group comparable runs by event, matrix, retries and actual runner minutes. Estimate savings from deduplication and cache reuse separately. |
| `diagnose-github-actions-quota` | 在一次失败运行里分别看创建、排队、runner 分配和首个 step；没有日志时标明证据不足，再看账户用量或服务状态。 | Separate run creation, queueing, runner assignment and the first step. If there are no logs, report the uncertainty and check account usage or service status. |
| `setup-windows-selfhosted-runner` | 核对 runner 标签、服务身份、工作目录和任务实际使用的解释器，先运行不含凭据的最小构建；区分注册成功和实际接单执行。 | Check runner labels, service identity, work directory and the interpreter used by a job. Run a minimal credential-free build; registration alone does not prove a runner can accept and execute it. |
