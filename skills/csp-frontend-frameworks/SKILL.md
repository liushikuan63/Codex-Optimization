---
name: csp-frontend-frameworks
description: 修改 React、Vue、Next.js、TypeScript 应用的状态、路由或升级框架时使用。 Use for component state, routing, hydration and framework upgrades.
---

# 前端框架变更 | Frontend framework changes

1. 读清单、锁文件、路由入口和现有测试。确定渲染发生在服务器、浏览器或两侧，以及数据缓存的所有者。
2. 在一个真实入口验证直接打开、刷新、返回、离开后再进入。异步请求慢于下一次导航时，旧结果不得覆盖新页面。
3. 框架升级先迁一个代表性页面。对比构建、服务端输出、客户端接管、事件清理和错误页面；记录可回退的依赖与配置组合。

按场景查找：[任务示例 / Worked examples](references/applied-methods.md)。

## English

1. Read the manifest, lockfile, route and tests. Identify the render boundary and who owns cached data.
2. Exercise direct navigation, refresh, back and re-entry. Delay a first response and confirm it cannot override a newer route.
3. Migrate one representative page first. Compare the build, server output, hydration, cleanup and error state. Record the dependency and configuration versions that allow rollback.
