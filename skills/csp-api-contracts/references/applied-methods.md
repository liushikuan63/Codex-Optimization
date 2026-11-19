# 任务示例 | Worked examples

下表按来源列出本技能吸纳的具体做法。每项用目标项目自己的数据验证。
Each row identifies a method retained from its source. Use representative data from the target project.

| 来源技能 / Source | 中文操作示例 | Worked example |
| --- | --- | --- |
| `local-api-contracts`, `spring-boot-rest-api-standards` | 旧客户端用原请求再调用一次；核对错误体、分页边界与重试幂等性。成功状态码之外还要检查持久化结果。 | Repeat the original request using an old client. Check error shape, page boundaries and idempotent retries. Read the persisted result as well as the response status. |
