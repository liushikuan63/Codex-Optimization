---
name: csp-runtime-rollout
description: 服务配置、客户端升级、运行实例与构建版本不一致时使用。 Use for rollout, update and rollback diagnosis.
---

# 服务与客户端升级 | Service and client rollout

1. 记录正在服务的版本、工件校验值、启动入口、配置来源和回退点。通过应用自身读回运行版本，不从文件名推断。
2. 区分发现更新、下载、完整性检查、安装、重启和迁移。保留首次失败的阶段与退出状态；用已知正常版本作对照。
3. 沙箱中分别演练正常升级、中断、旧配置和回退，读取一条实际业务记录。若数据格式不可逆，先验证可恢复备份；切换生产流量按既有授权执行。

按场景查找：[任务示例 / Worked examples](references/applied-methods.md)。

## English

1. Record the running version, artifact hash, launch entry, config source and rollback point. Read the version from the running application.
2. Separate discovery, download, integrity check, install, restart and migration. Preserve the first failed stage and exit status. Compare with a known good release.
3. Exercise upgrade, interruption, old settings and rollback in a representative environment. Read a real application record. For an incompatible format, verify that a backup restores before switching versions.
