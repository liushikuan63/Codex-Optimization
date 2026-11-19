# 任务示例 | Worked examples

下表按来源列出本技能吸纳的具体做法。每项用目标项目自己的数据验证。
Each row identifies a method retained from its source. Use representative data from the target project.

| 来源技能 / Source | 中文操作示例 | Worked example |
| --- | --- | --- |
| `kafka-best-practices`, `rabbitmq-expert` | 明确分区或队列的顺序范围、确认点和重投责任。让业务提交后、确认前中断，再次投递，检查业务只生效一次。 | Define ordering scope, acknowledgement point and redelivery ownership. Interrupt after the business commit but before acknowledgement and verify a single effect after redelivery. |
| `mongodb-atlas-stream-processing`, `spring-boot-event-driven-patterns`, `spring-events` | 画出事件与源事务的先后关系；模拟事务回滚和消费者重启，核验下游没有已回滚或重复的效果，水位能从持久化位置恢复。 | Map event publication against the source transaction. Exercise rollback and consumer restart; check no rolled-back or duplicate effects reach the destination and the checkpoint resumes correctly. |
