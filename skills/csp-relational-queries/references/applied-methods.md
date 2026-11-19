# 任务示例 | Worked examples

下表按来源列出本技能吸纳的具体做法。每项用目标项目自己的数据验证。
Each row identifies a method retained from its source. Use representative data from the target project.

| 来源技能 / Source | 中文操作示例 | Worked example |
| --- | --- | --- |
| `large-sqlite-text-extraction` | 读取大文本时确认选中的行和排序，用分块读取后的字符数或摘要与原值比较；命令行预览截断不等于数据丢失。 | For large text, select the intended row in a stable order. Compare the length or digest of chunked output with the stored value; a truncated console preview is not data loss. |
| `mysql`, `oracledb`, `postgresql-optimization` | 用目标引擎和代表性数据检查空值、排序、分页与执行计划。记录估算行数和实测行数差异；不同引擎分别验证，不照抄计划。 | On the target engine and representative data check nulls, ordering, pagination and plans. Compare estimated with actual rows. Verify each engine separately. |
