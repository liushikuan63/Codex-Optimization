---
name: csp-parallel-write
description: 多个工作单元要写入同一仓库时使用。 Use when parallel work needs write ownership and integration.
---

# 并行修改仓库 | Parallel changes to a repository

固定基线提交，用 `git worktree list --porcelain` 确认工作树。每个单元列出可写路径、读取依赖及验收条件；共享接口、生成物和最终集成只安排一个写入者。

核对每个提交实际修改的路径，先预演合并，再逐个集成已核验的提交，在合并结果上跑项目测试。依赖上一批的工作从已集成的新基线开始。出现脏文件或归属变化时保留现场。

按场景查找：[任务示例 / Worked examples](references/applied-methods.md)。

## English

Pin a base commit and inspect `git worktree list --porcelain`. Assign owned paths, read dependencies and acceptance criteria to each unit. Give shared contracts, generated files and final integration one writer.

Compare each commit’s changed paths with its assignment. Rehearse the merge, integrate the reviewed commits and test the resulting tree. Start dependent work at the integrated revision. Preserve dirty work or changed ownership for review.
