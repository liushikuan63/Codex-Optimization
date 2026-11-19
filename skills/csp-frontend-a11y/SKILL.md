---
name: csp-frontend-a11y
description: 用于表单、弹窗、菜单和标签页的焦点、语义与键盘验收。 Use for interactive controls, not blanket certification.
---

# 键盘与无障碍 | Keyboard and accessibility

从受影响的任务出发，仅用键盘完成一次。优先用原生控件，给按钮和输入可访问名称，错误信息关联到字段；颜色和占位符不能单独传递必要信息。

打开弹窗，观察初始焦点、Tab 顺序、背景是否仍可交互、Escape 和关闭后回焦。菜单与标签按各自键盘模式操作。检查辅助功能树中暴露的角色、名称、状态；自动扫描、键盘实测、屏幕阅读器评估分别记录。

按场景查找：[任务示例 / Worked examples](references/applied-methods.md)。

## English

Complete the affected task using only the keyboard. Prefer native controls; name inputs and icon buttons and associate errors with the relevant field. Do not depend on color or placeholders for essential information.

Open the dialog and inspect initial focus, Tab order, background interaction, Escape and the return of focus. Check menus and tabs against their own keyboard patterns. Record role, name and state in the accessibility tree. Report automated, keyboard and screen reader checks separately.
