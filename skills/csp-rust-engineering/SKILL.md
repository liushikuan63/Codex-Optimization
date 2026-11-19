---
name: csp-rust-engineering
description: 用于 Rust 所有权、库错误、异步并发和取消。 Use for ownership, fallible APIs or async tasks in Rust.
---

# Rust 错误与并发 | Rust errors and concurrency

从 Cargo.toml、锁文件、feature、目标平台和公开 API 确认约束。先解释谁拥有值、借用活到哪里，再决定移动或复制。库把可恢复错误交给调用者并保留错误源；避免用 panic 代替外部输入校验。

检查锁是否跨 await、阻塞工作是否在执行器线程、任务退出或取消后资源能否释放。用工作区约定的构建与测试检查相关 feature；加入一个错误或取消路径，注明未覆盖的平台。

按场景查找：[任务示例 / Worked examples](references/applied-methods.md)。

## English

Read the package manifest, lockfile, features, target and public API. Trace ownership and lifetimes before cloning or moving values. Preserve causes in recoverable library errors; validate input without panicking.

Check locks held across await, blocking work on executor threads and cleanup on cancellation. Build and test the relevant feature combinations using the project's commands, including an error or cancellation case. Identify target platforms that were not exercised.
