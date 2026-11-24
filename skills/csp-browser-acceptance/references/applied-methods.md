# 任务示例 | Worked examples

下表按来源列出本技能吸纳的具体做法。每项用目标项目自己的数据验证。
Each row identifies a method retained from its source. Use representative data from the target project.

| 来源技能 / Source | 中文操作示例 | Worked example |
| --- | --- | --- |
| `electron-app-stuck-spinner-triage`, `spa-loading-hang-triage` | 保存一次卡住的导航：依次检查入口文档、模块响应类型和首个业务请求，再观察加载状态是否退出。用正常导航作对照。 | Capture one stuck navigation. Check the entry document, module response type, first business request and loading-state reset in order. Compare with a working navigation. |
| `local-browser-e2e`, `verify-ui-in-browser` | 从真实页面操作按钮并验证结果；固定宽度改变高度，量控件遮挡、四向内缩及实际滚动区。用旧版或夹具里的已知缺陷证明同一判据会报错。 | Operate the real control and verify its result. Hold width fixed and change height. Measure occlusion, insets and the actual scroll container; use a known defect to make the same check fail. |
