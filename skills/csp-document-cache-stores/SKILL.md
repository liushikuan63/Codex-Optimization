---
name: csp-document-cache-stores
description: 针对 MongoDB 或 Redis 的模型、查询、缓存和连接问题使用。 Use for document models, indexes, connection pools, cache correctness or search.
---

# 文档库和缓存 | Document stores and caches

1. 列出实际读写形状、键空间、租户边界和数据量。文档是否内嵌按一起读取和增长上限决定；先用样本核对缺字段与空值的差别。
2. 用真实查询形状对比计划、扫描量与返回条数。连接问题区分池耗尽、拓扑变化和命令超时；只记录脱敏指标。
3. 缓存验收覆盖首次命中缺失、写后读、过期和服务降级。语义缓存用相似但答案不同的反例核验阈值和用户隔离；集群同时检查分片键分布。

按场景查找：[任务示例 / Worked examples](references/applied-methods.md)。

## English

1. List read/write shapes, key namespaces, tenant boundaries and growth. Embed documents based on access patterns and bounded size. Test missing fields separately from null values.
2. Compare plans, examined records and returned counts for the actual query. Distinguish pool exhaustion, topology changes and command timeout using redacted metrics.
3. Exercise a miss, read after write, expiry and degraded service. For a semantic cache test similar questions with different answers and tenant separation. Check shard distribution where relevant.
