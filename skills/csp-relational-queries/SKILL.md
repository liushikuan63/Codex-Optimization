---
name: csp-relational-queries
description: 排查 SQL 结果、排序、慢查询或索引选择时使用。 Use for SQL correctness, plans and indexes; use the migration skill for schema rollout.
---

# 关系数据库查询 | Relational queries

1. 记录数据库版本、库、schema、查询参数类型和返回行数。遇到同名表，先确认应用账号的搜索路径和实际连接；保留只读查询样本。
2. 用包含空值、重复键、时区边界的样本核对连接和分组。分页需要稳定且唯一的排序；单看第一页无法发现缺行或重行。
3. 先读估算执行计划；带执行的分析可能运行语句，只在允许的环境使用。比较扫描行数、排序、等待和延迟，核算新增索引的写入成本。

按场景查找：[任务示例 / Worked examples](references/applied-methods.md)。

## English

1. Record the engine version, database, schema, parameter types and result count. Resolve same-named tables using the application's connection and search path.
2. Check joins and groups with nulls, duplicate keys and time boundaries. Verify deterministic pagination across pages with a unique tie-breaker.
3. Read an estimated plan before running an analysis that executes the statement. Compare rows examined, sorting, waits and latency, and account for index write cost.
