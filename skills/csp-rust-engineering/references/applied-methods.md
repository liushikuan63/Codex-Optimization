# 任务示例 | Worked examples

下表按来源列出本技能吸纳的具体做法。每项用目标项目自己的数据验证。
Each row identifies a method retained from its source. Use representative data from the target project.

| 来源技能 / Source | 中文操作示例 | Worked example |
| --- | --- | --- |
| `local-rust-engineering` | 跟踪一个错误或取消分支：核对调用者收到的错误、借用边界以及文件和任务是否释放。不要以正常路径代替失败验证。 | Follow one error or cancellation path. Check the caller's error, borrow boundaries and release of files and tasks. A happy path alone does not establish failure behavior. |
