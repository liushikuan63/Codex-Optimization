# 任务示例 | Worked examples

下表按来源列出本技能吸纳的具体做法。每项用目标项目自己的数据验证。
Each row identifies a method retained from its source. Use representative data from the target project.

| 来源技能 / Source | 中文操作示例 | Worked example |
| --- | --- | --- |
| `local-spring-mybatis`, `springboot-patterns`, `springboot-verification`, `spring-boot-test-patterns` | 先用窄测试定位映射问题，再经实际 Spring 代理和测试数据库验证事务回滚、参数绑定和结果字段；报告哪些依赖是替身。 | Use a focused test to isolate mapping issues, then exercise a real Spring proxy and test database for rollback, parameter binding and result fields. Identify mocked dependencies. |
