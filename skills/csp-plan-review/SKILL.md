---
name: csp-plan-review
description: 对开发方案、迁移计划、规格或验收条款做反例评审，找出可能被假绿掩盖的需求、依赖、失败边界和回退缺口；用于实施前评审或补强复杂计划，不用于简单编辑、普通代码评审或替代执行。
---

# 用反例评审开发方案

1. 从当前需求、实际调用方、源代码和准入条件提取可观察结果。区分事实、假设、未知和待决定项。查当前所有者、工作区与依赖；发现冲突时说明哪项证据能决议。
2. 对每条高影响要求问：错的实现怎样也能通过？例如回退页面也返回 200、迁移覆盖已有扩展、一个旧入口未走新校验、自建 fixture 与实现共享同一个错误假设。为每个可行反例指定最小反制证据：实际入口、负例、独立数据、并发/恢复或旧客户端。不要要求所有方案都用同一批测试。
3. 检查执行顺序和失败窗口：前置条件、产生副作用的节点、可逆性、失败后的可识别状态和下一步。说明谁负责、检查何时发生、何种结果必须停止；验证过的证据与计划中的检查分开写。
4. 先列会改变执行或放行决定的问题，给具体反例、影响和收敛条件。必要信息查不到时保留未验证项，写出需要的数据或决策；用户只要求评审时仅审阅。没有高影响反例时结束，不设固定轮数或新审批。

来源：MIT 仓库 [反例方案复核](https://github.com/liushikuan63/Qoder-Optimization/blob/fe929cf1de22d4312b9526536568161d2a674439/skills/counterexample-driven-plan-review/SKILL.md)、[VibeCoding 文档](https://github.com/liushikuan63/Qoder-Optimization/blob/fe929cf1de22d4312b9526536568161d2a674439/skills/vibecoding-doc/SKILL.md)。按 Codex 现有授权和项目约定另写。

按场景查找：[任务示例 / Worked examples](references/applied-methods.md)。

## English

Construct a realistic case where the planned tests pass while the requirement fails. Ground it in actual callers, data owners and failure windows. Add the smallest observable check that catches it. Identify remaining assumptions and a recovery path. Return specific changes to the plan.
