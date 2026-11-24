# 受影响入口与宽高验收

按影响列出「入口 × 状态 × 视口 × 预期」，保留通过、失败或未验证的证据。优先覆盖改动页面和共用同一组件的入口；有原缺陷时保留其复现路径，验证修复后在同一路径通过。涉及状态或持久化时，沿真实操作验证请求、反馈和读回；首页通过不能替代子路由、直接访问或刷新。

## 同时改变宽和高

- 从用户设备或宿主的实际内容区取宽高；视情况补一个同宽更高的对照、横屏手机或窄高窗口。浏览器窗口尺寸不等于页面视口，嵌入页记录内外两层实际尺寸。
- 判断横向溢出、内外两层是否都在垂直滚动、粘滞区是否遮住控件。滚动列表、长文表格等允许按设计滚动；只有设计要求首屏可用的关键控件才断言初始可见。对必须在滚动后可用的控件实际滚动、聚焦或点击，确认可达及无遮挡。
- 结合截图和可观察的几何/交互判据。CSS 的 `overflow-y: auto` 只表示允许滚动，要结合 `scrollHeight` 和 `clientHeight`；在已知有设计内滚动的页面不要直接把差值判为缺陷。
- 对主题滚动条或细字，比较同主题、缩放、像素比和位置下的同一区域；用局部截图和真实计算样式定位，多考虑浏览器/系统覆盖式滚动条及高对比度模式。改布局断言时可在独立夹具制造要抓住的遮挡或溢出，确认正确与错误样本能被区分。

## 把布局问题变成可失败的检查 | Make layout checks fail on known defects

- 根据项目设计为四向内缩、列表可用高度和分页空隙定判据。分别测内容块和文字，区分本来要铺满的布局壳。到实际可横向滚动的元素上读 `scrollWidth - clientWidth`，确认其 `overflow-x`；外层恰好为 0 不能代替内层读数。
- 从路由表列出受影响入口，写清未测项。确认加载和过渡都已结束再取稳定读数；超时、缺元素或隐藏标签页中的残留动画要另行标记。用旧版或隔离夹具中的已知缺陷跑一次，证明同一判据会报错；阈值由项目设计决定。
- Set project-specific limits for insets on all four sides, usable list height and pagination gaps. Measure both content blocks and text; an intentionally full-width shell is a separate case. Measure horizontal overflow on the element that actually scrolls and check its computed `overflow-x`.
- Derive the affected route list from the router and report omissions. Check that loading and transitions settle before recording geometry. Mark timeouts, missing elements and stale animations in hidden tabs separately. Run the same check against a known defect from the previous build or an isolated fixture.

以下读数用于定位视口和滚动归属，可在当前页面执行。用项目真实定位器选取实际的滚动面板和关键控件；数值只是证据，结合产品约束及交互判断。

```js
function readLayout(panel, control) {
  const root = document.scrollingElement;
  const box = control?.getBoundingClientRect();
  const metrics = element => element && ({
    width: element.clientWidth,
    contentWidth: element.scrollWidth,
    height: element.clientHeight,
    contentHeight: element.scrollHeight,
    overflowY: getComputedStyle(element).overflowY,
  });
  return {
    viewport: { width: innerWidth, height: innerHeight },
    root: metrics(root),
    panel: metrics(panel),
    control: box && { top: box.top, bottom: box.bottom },
  };
}
```

来源：Qoder-Optimization [verify-ui-in-browser](https://github.com/liushikuan63/Qoder-Optimization/tree/9f39002a6e6713f1eb5c868ab61ad8608a1771a5/skills/verify-ui-in-browser)，MIT。
