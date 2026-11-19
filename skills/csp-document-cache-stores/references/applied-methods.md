# 任务示例 | Worked examples

下表按来源列出本技能吸纳的具体做法。每项用目标项目自己的数据验证。
Each row identifies a method retained from its source. Use representative data from the target project.

| 来源技能 / Source | 中文操作示例 | Worked example |
| --- | --- | --- |
| `mongodb-connection`, `redis-connections` | 把建立连接和等待连接池分开计时。记录使用量、空闲量与等待时间，区分连不上、池满和命令执行慢。 | Time connection setup separately from waiting for a pooled connection. Compare in-use, idle and waiting metrics to separate connection failures, pool exhaustion and slow commands. |
| `mongodb-natural-language-querying` | 把用户问题先写成预期筛选条件，再与生成的只读查询比较；用缺字段、空值及跨租户样本检查范围，不执行未经核对的改写。 | Write down intended filters before reviewing a generated read-only query. Check missing fields, nulls and tenant boundaries against known samples before trusting the result. |
| `mongodb-query-optimizer`, `mongodb-schema-design` | 按实际查询与文档增长方式选择内嵌或引用；比较查询计划、检查文档数与返回数，验证建索引后仍能处理缺字段。 | Choose embedding or references from actual access patterns and growth. Compare plans and documents examined versus returned, including records with missing fields. |
| `mongodb-search-and-ai`, `redis-search`, `redis-semantic-cache` | 准备精确命中、同义表达和近似但答案不同的查询。逐项核对排序、阈值、过滤和租户隔离，避免只用命中率评估质量。 | Build exact hits, paraphrases and near matches with different answers. Check ranking, thresholds, filters and tenant isolation; hit rate alone is insufficient. |
| `redis-clustering`, `redis-core` | 注明键的类型、TTL、分片归属与原子操作边界；在缓存未命中、写后失效和节点切换后读回真实业务值。 | Describe key type, TTL, shard ownership and atomicity. Read the real business value after a miss, invalidation following a write and node failover. |
| `redis-observability`, `redis-security` | 为应用账号核对最小权限与租户键范围，记录慢命令、逐出、连接等待和延迟。用授权测试账号确认只允许业务所需读写。 | Check least privilege and tenant key scope for the application account. Track slow commands, eviction, connection waits and latency. Verify the authorized test account can perform only its required operations. |
