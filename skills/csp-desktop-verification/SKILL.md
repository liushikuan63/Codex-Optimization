---
name: csp-desktop-verification
description: 用于在实际应用窗口核验用户授权的操作。 Use for desktop interactions that require an observable result.
---

# 桌面操作与结果核验 | Desktop interaction and readback

优先使用已有应用接口、文件或后台控件。需要输入时，核对应用、窗口和文档身份，用当前截图或辅助功能树定位控件。截图与目标不符时重新识别。

一次输入后观察预期状态，分别报告派发、实际效果及未知项。后台工具保持其支持的操作模式；前台输入串行，先说明焦点影响。超时先读回，不盲目重发。

按场景查找：[任务示例 / Worked examples](references/applied-methods.md)。

## English

Start with an existing application API, file or background control. Before input, identify the app, window and document using a fresh capture or accessibility tree. Reidentify the target when a capture does not match.

Inspect the expected state after each action. Report dispatch, observed effect and uncertainty separately. Use only modes supported by the tool. Serialize foreground input and announce focus changes. Read state before replaying a timed-out action.
