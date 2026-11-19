# 任务示例 | Worked examples

下表按来源列出本技能吸纳的具体做法。每项用目标项目自己的数据验证。
Each row identifies a method retained from its source. Use representative data from the target project.

| 来源技能 / Source | 中文操作示例 | Worked example |
| --- | --- | --- |
| `concurrent-edit-attribution-check`, `pause-writer-before-shared-file-edit` | 改共用文件前保存原始字节，写入前再比较。若另一写入者改变了文件，先协调归属，再以新版本重做窄范围差异。 | Capture original bytes and compare again immediately before writing a shared file. If another writer changed it, coordinate ownership and reapply only the intended change to the new version. |
| `open-code-review-delegate`, `parallel-orchestration` | 为并行工作指定文件归属、共用接口的负责人和集成顺序。独立审查读取实际差异和测试结果，最后在合并版本上验收。 | Assign file ownership, shared-interface owners and integration order. The independent reviewer reads the real diff and test results. Verify the merged version. |
