# 任务示例 | Worked examples

下表按来源列出本技能吸纳的具体做法。每项用目标项目自己的数据验证。
Each row identifies a method retained from its source. Use representative data from the target project.

| 来源技能 / Source | 中文操作示例 | Worked example |
| --- | --- | --- |
| `disk-junction-migration`, `windows-relocated-install-path-repair` | 遇到应用搬盘后只剩外壳能启动，分别查服务、更新器和资源的实际路径。先用官方迁移或修复方式；涉及链接时核对链接与目标，保留可恢复副本。 | After moving an app, verify actual paths for services, updater and resources. Prefer a supported relocation or repair. Distinguish a link from its target and retain a recoverable copy. |
| `intermittent-test-red-triage` | 保留首红，固定版本、工作目录和 runner；从失败的聚合套件缩小到前序测试或负载。单跑通过只能缩小范围。 | Preserve the first failure, commit, working directory and runner. Reduce the suite to a predecessor test or load factor; passing in isolation only narrows the investigation. |
| `safe-text-editing`, `structured-edit-safety` | 写前断言锚点数量与版本，展示拟改差异；写后重新解析、检查编码与行尾，确认未匹配行和他人修改保留。 | Check anchor counts and the original version before writing and inspect the proposed diff. Reparse afterward and check encoding, line endings and preservation of nonmatching rows and others' edits. |
| `verify-windows-cmd-tool`, `windows-elevated-changes-from-git-bash`, `windows-gitbash-command-safety`, `windows-powershell-from-gitbash` | 查明实际解释器、权限、参数和退出码。先在临时目录用含空格及非 ASCII 的路径验证只读命令，再选择同一种 shell 完成文件操作。 | Identify the actual interpreter, privileges, arguments and exit code. Verify a read-only command on a temporary path with spaces and non-ASCII characters, then keep file operations within one shell. |
