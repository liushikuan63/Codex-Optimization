# 任务示例 | Worked examples

下表按来源列出本技能吸纳的具体做法。每项用目标项目自己的数据验证。
Each row identifies a method retained from its source. Use representative data from the target project.

| 来源技能 / Source | 中文操作示例 | Worked example |
| --- | --- | --- |
| `cloudbase-wechat-integration` | 将登录、云函数和回调分开验收。测试环境里对同一业务通知投递两次，再从应用读取结果；模拟授权失效后的恢复。 | Check sign-in, cloud function and callback separately. Replay the same business notification twice in a test environment and read the result through the app. Exercise expired authorization. |
| `minigame-dev-pro`, `miniprogram-development`, `wechat-miniprogram-dev` | 选首屏、切后台再返回、权限拒绝三条路径；同版本分别在开发工具与真机运行，记录系统、运行库、包体和首个差异。 | Exercise first launch, background/resume and denied permission. Compare dev tools with a physical device on the same build, recording OS, runtime, package and first differing step. |
