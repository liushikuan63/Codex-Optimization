---
name: csp-db-migrations
description: 用于表结构、回填或数据迁移评审。 Use for schema changes and backfills, not routine queries.
---

# 数据库迁移 | Database migrations

1. 确认引擎、版本、迁移工具、已执行版本、表量级与旧客户端。不改已经应用的迁移；新增修正步骤。
2. 先加兼容结构，再回填、核验、切换读写，最后移除旧字段。按稳定键分批，保存进度；让旧客户端在中断时继续写，然后重跑，检查有没有覆盖新数据。
3. 按目标引擎检查 DDL 锁及事务限制。在隔离库从旧版升级，检查约束、行数和业务样本，用恢复演练说明不可逆变化怎样修复。小样本不能证明生产锁时间。

按场景查找：[任务示例 / Worked examples](references/applied-methods.md)。

## English

1. Identify the engine and version, applied migrations, table size and old clients. Add a corrective migration instead of rewriting applied history.
2. Expand the schema, backfill, compare, switch readers and writers, then contract. Resume from a stable key in bounded batches. Interrupt a batch, let an old client write, and check that a rerun preserves the write.
3. Check DDL locks and transactional limits for that version. Upgrade a disposable old database and inspect constraints, counts and business samples. Rehearse recovery of lossy changes; a small fixture cannot establish production lock time.
