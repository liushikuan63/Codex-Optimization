# 任务示例 | Worked examples

下表按来源列出本技能吸纳的具体做法。每项用目标项目自己的数据验证。
Each row identifies a method retained from its source. Use representative data from the target project.

| 来源技能 / Source | 中文操作示例 | Worked example |
| --- | --- | --- |
| `java-architect`, `java-quality` | 从对外请求追到实际事务、线程池和下游调用。用依赖变慢、异常退出的请求检查资源释放与错误传播是否符合契约。 | Trace a real request to its transaction, worker pool and downstream calls. Use slow-dependency and error-exit cases to verify cleanup and error propagation. |
| `nodejs-backend-patterns` | 让一次下游请求超时或被调用者取消，确认请求上下文、监听器与连接清理完毕；检查关闭时是否等待在途请求。 | Time out or cancel a downstream request. Check cleanup of request context, listeners and connections, and whether shutdown drains active requests. |
| `spring-aop`, `spring-boot-actuator`, `spring-boot-cache`, `spring-boot-resilience4j` | 通过真实代理或应用请求验证切面和缓存是否生效；在依赖变慢时核对超时、重试和熔断的责任层，分别读取存活与就绪状态。 | Verify aspects and caching through a real proxy or application request. With a slow dependency check which layer owns timeouts, retries and circuit breaking, and read liveness and readiness separately. |
