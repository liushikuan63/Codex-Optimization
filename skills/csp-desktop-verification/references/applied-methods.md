# 任务示例 | Worked examples

下表按来源列出本技能吸纳的具体做法。每项用目标项目自己的数据验证。
Each row identifies a method retained from its source. Use representative data from the target project.

| 来源技能 / Source | 中文操作示例 | Worked example |
| --- | --- | --- |
| `diagnose-windows-webview2-blank-window`, `electron-tray-icon-diagnosis` | 白窗检查主窗口、渲染进程、导航和可见内容；托盘问题核对所属进程与菜单实际打开的窗口。记录客户端和运行时版本。 | For a blank window, distinguish window creation, renderer startup, navigation and visible content. For a tray icon, verify process ownership and the window opened by its menu. Record runtime versions. |
| `powershell-windows-display-interop`, `windows-desktop-keyboard-automation`, `windows-ui-forensics-powershell` | 记录目标窗口、缩放与坐标系；从只读状态定位控件，输入后检查窗口仍是原目标并读回变化。沙箱画面不作为宿主证明。 | Record the target window, scale and coordinate system. Locate a control with read-only state; after input confirm the same window and read back the change. Sandbox pixels do not prove host state. |
