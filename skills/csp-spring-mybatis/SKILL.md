---
name: csp-spring-mybatis
description: 用于 Spring 事务、Mapper 绑定和数据库调用路径。 Use for Spring transactions or MyBatis mapping, not unrelated Java edits.
---

# Spring 与 MyBatis | Spring and MyBatis

沿 controller 或 job → service → mapper 找到真实调用；核对 JDK、框架版本和命名空间。事务按代理入口、自调用、线程、异常传播和数据源验证。让第二次写入失败，读回第一次写入是否也回滚。

值使用绑定参数，动态列名通过固定映射；检查空列表、缺少过滤条件、XML namespace、参数名和结果映射。用数据样本核对连接放大、嵌套查询次数和分页总数。

按场景查找：[任务示例 / Worked examples](references/applied-methods.md)。

## English

Follow the controller or job through the service to the real mapper. Pin the JDK, framework and namespace. Verify proxy entry, self-invocation, thread, exceptions and data source. Fail a second write and read back whether the first rolled back.

Bind values and map dynamic identifiers to fixed columns. Inspect empty lists, missing filters, XML namespaces, parameter names and result mappings. Use data that reveals join multiplication, nested queries and incorrect page totals.
