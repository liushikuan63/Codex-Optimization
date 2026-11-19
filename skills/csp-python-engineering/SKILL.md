---
name: csp-python-engineering
description: 在修改 Python 包、异步任务或测试时选择。 Use for Python packaging, cancellation, fixture isolation and tests.
---

# Python 工程与测试 | Python engineering and tests

1. 从项目清单和锁文件确定解释器、入口和测试命令。用项目的环境执行；从源码目录成功导入还不能证明发行包包含该模块。
2. 把网络、时钟和存储放在可替换的边界；测试正常、异常、取消以及资源释放。异步调用设置超时，并确认取消后没有遗留任务。
3. 对包结构的改动，从构建产物装入空环境，在仓库外导入并调用公开入口。性能改动使用代表性输入记录耗时、内存和结果一致性。

按场景查找：[任务示例 / Worked examples](references/applied-methods.md)。

## English

1. Read the interpreter constraint, lockfile and test command. A successful import from the checkout does not prove that the wheel contains the module.
2. Isolate clocks, storage and network calls. Exercise success, failure and cancellation; check that tasks and resources are released after a timeout.
3. For packaging changes install the built artifact in a clean environment and call its public entry point outside the checkout. For speed changes measure time and memory on representative data and compare the results.
