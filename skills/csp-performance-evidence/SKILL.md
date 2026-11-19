---
name: csp-performance-evidence
description: 用于已有指标的性能或成本优化。 Use for measured latency, throughput, memory or cost changes.
---

# 性能与成本测量 | Performance and cost measurement

固定工作负载、提交、硬件、并发和冷暖缓存条件。保留基线原始样本、分位数和结果正确性；从查询次数、阶段耗时或剖析结果找瓶颈。

一次只改变一个因素。同一输入做前后对照，包括错误路径、资源消耗和输出语义。差异没有超过噪声就报告收益未确认。请求数是成本代理指标；实际费用需要账单依据。达到目标或没有新假设时结束。

按场景查找：[任务示例 / Worked examples](references/applied-methods.md)。

## English

Fix the workload, revision, hardware, concurrency and cache state. Keep raw baseline samples, relevant percentiles and output checks. Locate the bottleneck using query counts, stage timings or a profile.

Change one factor per comparison. Use identical inputs and verify error behavior, resources and output semantics. A difference within the noise is inconclusive. Request volume is a proxy for cost; actual savings need billing evidence. Stop on target or when no testable hypothesis remains.
