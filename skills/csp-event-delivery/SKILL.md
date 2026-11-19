---
name: csp-event-delivery
description: 变更消息生产、消费、确认或重放时使用。 Use for queues, consumers and outbox delivery; skip ordinary synchronous calls.
---

# 消息投递与重试 | Message delivery and retries

1. 画出生产、持久化、业务提交、确认四个时刻，标出哪个组件负责重试。按实体选择顺序键；并行消费者不保证全局顺序。
2. 明确幂等键、去重范围和保留期限。数据库提交成功但确认失败时重投同一消息，验证只出现一次业务效果。
3. 校验坏消息进入隔离队列、重试有上限、消费者重启能从正确位置恢复。用积压年龄、处理速率和重复数判断恢复，不只看队列长度。

按场景查找：[任务示例 / Worked examples](references/applied-methods.md)。

## English

1. Trace publish, persistence, business commit and acknowledgement. Name the retry owner. Define ordering per entity; multiple consumers do not imply global order.
2. Specify the idempotency key, its scope and retention. Deliver the same message after a successful commit but before acknowledgement and check for one business effect.
3. Verify a poison message is isolated, retries are bounded and restart resumes at the intended position. Measure oldest-message age, throughput and duplicates alongside queue depth.
