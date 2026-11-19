---
name: csp-backend-services
description: 审查 Java、Node 或 TypeScript 服务的生命周期、超时、缓存和可观察性时使用。 Use for service lifecycle, timeouts, caching and observability in a backend.
---

# 后端服务边界 | Backend service boundaries

从实际入口追踪配置、校验、服务、存储和对外调用。记录谁拥有事务、缓存失效、重试和超时预算，避免每一层同时重试。覆盖非法输入、依赖变慢、取消、重放和服务关闭；核验连接、线程或事件监听器释放。日志区分请求和尝试次数，健康检查区分进程存活与能接流量。变更后经真实入口读取业务结果。

按场景查找：[任务示例 / Worked examples](references/applied-methods.md)。

## English

Trace the entry point through validation, configuration, storage and downstream calls. Assign ownership for transactions, invalidation, retries and timeout budgets. Exercise invalid input, slow dependencies, cancellation, replay and shutdown. Verify release of connections, threads or listeners. Distinguish requests from attempts in logs and liveness from readiness in health checks. Read the business result through the actual entry point.
