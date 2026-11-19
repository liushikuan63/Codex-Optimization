# 任务示例 | Worked examples

下表按来源列出本技能吸纳的具体做法。每项用目标项目自己的数据验证。
Each row identifies a method retained from its source. Use representative data from the target project.

| 来源技能 / Source | 中文操作示例 | Worked example |
| --- | --- | --- |
| `frontend-development` | 从生产路由进入页面，分别走首次加载、刷新、返回与失败重试；记录数据、焦点和滚动位置是否按设计恢复。 | Exercise first load, refresh, back navigation and retry through the production route. Check whether data, focus and scroll position are restored as designed. |
| `nextjs-app-router-patterns`, `react-modernization`, `vue-expert`, `umi3-to-umi4-upgrade` | 在旧版和新版分别走直接访问、客户端跳转、刷新和返回；对比路由参数、数据加载、服务端与客户端渲染及状态清理。 | Exercise direct entry, client navigation, refresh and back on both versions. Compare route parameters, data loading, server/client rendering and state cleanup. |
| `typescript-pro` | 在外部 JSON 边界校验未知值，用有区别字段的联合类型覆盖所有状态。类型检查后，再用缺字段的输入核对运行时行为。 | Validate unknown JSON at the boundary and cover every state of a discriminated union. After type checking, supply missing fields to verify runtime behavior. |
