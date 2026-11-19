---
name: csp-api-contracts
description: 新增或修改有消费者的 HTTP API 时使用；不用于内部重构。 Use for public HTTP contracts, pagination or retry semantics.
---

# 接口契约 | API contracts

1. 找到实际客户端、服务路由和旧版响应。列出必填、可空、缺省和错误状态，区分新增可选字段与破坏性变化。
2. 列表采用稳定排序并用唯一键打破并列；用两页有相同排序值的数据检查丢失和重复。排序字段做服务端映射，租户身份来自认证上下文。
3. 可重试写入要把键绑定到调用者、操作及请求内容。验证并发首次请求、同键不同内容、提交后响应丢失、旧客户端和过期键。交付真实请求及消费者读回；使用替身时注明。

按场景查找：[任务示例 / Worked examples](references/applied-methods.md)。

## English

1. Trace the current client, route and response before changing nullability, defaults or errors. Tell consumers which changes require migration.
2. Use deterministic ordering with a unique tie breaker. Fetch two pages with tied sort values and check for gaps and duplicates. Map sort fields on the server and derive tenant scope from authentication.
3. Bind a retry key to the caller, operation and payload. Check simultaneous first requests, a reused key with a different body, lost responses after commit, older clients and expiry. Record a consumer readback and distinguish a live call from a mock.
