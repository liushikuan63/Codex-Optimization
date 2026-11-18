---
name: csp-browser-acceptance
description: 验收改动页面的真实交互、宽高布局和 SPA 启动，或排查浏览器 E2E 回归；用于受影响页面、白屏或持续加载，不用于纯后端改动。
---

# 浏览器验收

- 先确认改动、实际入口、受影响的共用组件和验收条件。核对 dev server、URL 和构建来自目标 checkout；使用项目已有的浏览器工具。
- 真实操作检查提交、反馈、请求及读回；使用语义定位、步骤结束条件和隔离数据。首个失败保留请求、控制台和截图。因重跑转绿单列，不能宣称已修。
- 布局和共用组件按 [受影响入口与宽高验收](references/affected-routes-and-viewports.md) 选择入口、状态和宽高；细边、小字号或细微差异可调用 `csp-visual-detail`。动画/SVG/主题按 [动效与主题](references/motion-and-theme.md) 验收。
- 白屏、持续转圈或刷新后卡住时按 [SPA 启动排查](references/spa-startup-triage.md) 检查文档版本、模块响应、初始化 API 和加载状态。
- 报告通过、失败、未验证及原因；替身数据不证明真实账号、外部交付或原生端通过。
