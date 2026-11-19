---
name: csp-miniapp-runtime
description: 修改小程序、小游戏生命周期、云函数或设备适配时使用。 Use for mini app lifecycle, device behavior and cloud function boundaries.
---

# 小程序与小游戏运行验证 | Mini app and game runtime

区分开发工具、模拟器、真机和已发布环境；先记下运行库、包版本、云环境及环境是否有权测试。用最小场景验证首次启动、退到后台再返回、弱网或离线和权限拒绝。检查事件订阅、计时器、音频或渲染循环在退出时释放。云端写入使用隔离数据，比较调用回执和应用读回。分开报告模拟器与具体真机上的结果。

按场景查找：[任务示例 / Worked examples](references/applied-methods.md)。

## English

Distinguish the development tool, emulator, device and release environment. Record runtime, package and authorized cloud environment. Exercise first launch, background/resume, weak connectivity and denial of a requested permission. Check subscriptions, timers, audio and render loops are released on exit. For a cloud write, use isolated data and verify application readback. Report simulator and device results separately.
