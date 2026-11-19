# 任务示例 | Worked examples

下表按来源列出本技能吸纳的具体做法。每项用目标项目自己的数据验证。
Each row identifies a method retained from its source. Use representative data from the target project.

| 来源技能 / Source | 中文操作示例 | Worked example |
| --- | --- | --- |
| `desktop-update-push-triage` | 分开发现更新、下载、安装、重启四步记录版本。用运行中实例读回版本号，遇到失败时保存最早的不同结果。 | Record versions at update discovery, download, install and restart. Read back the version from the running instance and preserve the earliest point of divergence. |
| `global-config-smoke-runner` | 修改工具配置后，在隔离配置目录运行与变更相关的检查，保留各自退出状态；分清配置错误、检查器误判和平台差异。 | After changing tool configuration, run the relevant checks with an isolated configuration directory. Preserve individual outcomes and distinguish config defects, checker errors and platform differences. |
| `nginx-config-builder`, `systemd-java-service-centos7`, `senior-devops` | 在目标软件版本上检查配置语法、工作目录与启动身份。先在测试实例重载或重启，再用应用读请求检查服务和回退版本。 | Validate syntax, working directory and service identity against the deployed software version. Reload or restart a test instance, then check an application read and rollback version. |
| `user-side-deploy-verify` | 从用户拿到的包在干净环境安装，启动实际应用并检查运行版本；选一个经过真实入口的核心读写流程，记录未验证的平台。 | Install the user-facing artifact in a clean environment and check the running version. Exercise one core workflow through the real entry and identify platforms not tested. |
