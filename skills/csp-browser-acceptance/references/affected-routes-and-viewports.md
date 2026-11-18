# 受影响入口与宽高验收

按影响列出「入口 × 状态 × 视口 × 预期」，保留通过、失败或未验证的证据。优先覆盖改动页面和共用同一组件的入口；有原缺陷时保留其复现路径，验证修复后在同一路径通过。涉及状态或持久化时，沿真实操作验证请求、反馈和读回；首页通过不能替代子路由、直接访问或刷新。

## 同时改变宽和高

- 从用户设备或宿主的实际内容区取宽高；视情况补一个同宽更高的对照、横屏手机或窄高窗口。浏览器窗口尺寸不等于页面视口，嵌入页记录内外两层实际尺寸。
- 判断横向溢出、内外两层是否都在垂直滚动、粘滞区是否遮住控件。滚动列表、长文表格等允许按设计滚动；只有设计要求首屏可用的关键控件才断言初始可见。对必须在滚动后可用的控件实际滚动、聚焦或点击，确认可达及无遮挡。
- 结合截图和可观察的几何/交互判据。CSS 的 `overflow-y: auto` 只表示允许滚动，要结合 `scrollHeight` 和 `clientHeight`；在已知有设计内滚动的页面不要直接把差值判为缺陷。
- 对主题滚动条或细字，比较同主题、缩放、像素比和位置下的同一区域；用局部截图和真实计算样式定位，多考虑浏览器/系统覆盖式滚动条及高对比度模式。改布局断言时可在独立夹具制造要抓住的遮挡或溢出，确认正确与错误样本能被区分。

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

来源：Qoder-Optimization [verify-ui-in-browser](https://github.com/liushikuan63/Qoder-Optimization/tree/fe929cf1de22d4312b9526536568161d2a674439/skills/verify-ui-in-browser)，MIT。
