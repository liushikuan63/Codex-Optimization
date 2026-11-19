# 任务示例 | Worked examples

下表按来源列出本技能吸纳的具体做法。每项用目标项目自己的数据验证。
Each row identifies a method retained from its source. Use representative data from the target project.

| 来源技能 / Source | 中文操作示例 | Worked example |
| --- | --- | --- |
| `async-python-patterns` | 取消正在等待的任务，检查超时由哪一层处理、子任务是否退出、连接是否归还，再运行下一次请求。 | Cancel a waiting task. Check timeout ownership, child task exit and connection release before sending a second request. |
| `python-anti-patterns`, `python-error-handling`, `python-type-safety` | 把外部输入先当作未知值校验；测试缺字段、类型不符和异常清理。让错误带着可定位的上下文返回，避免吞异常后返回正常值。 | Validate external input as unknown. Exercise missing fields, invalid types and cleanup after exceptions. Return errors with useful context rather than swallowing them as normal values. |
| `python-backend-guidelines`, `python-programmer`, `python-project-structure`, `python-testing-patterns` | 从干净环境安装产物并通过公开入口调用；区分可编辑安装与发行包，再隔离时间、临时文件和测试间共享状态。 | Install the built artifact into a clean environment and call its public entry point. Distinguish editable from packaged installs and isolate time, temporary files and shared test state. |
