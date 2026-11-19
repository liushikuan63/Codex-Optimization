# 任务示例 | Worked examples

下表按来源列出本技能吸纳的具体做法。每项用目标项目自己的数据验证。
Each row identifies a method retained from its source. Use representative data from the target project.

| 来源技能 / Source | 中文操作示例 | Worked example |
| --- | --- | --- |
| `production-readiness-audit`, `verify-before-claim` | 逐项写明通过、失败、不适用或未验证，附最终版本证据；用会失败的反例检查验收是否真的区分了行为。 | Mark each requirement passed, failed, not applicable or unverified with evidence from the final version. Try a failing control to see whether the check distinguishes behavior. |
| `share-package-release`, `ship-clean-pr` | 逐项核对提交、最终差异、归档内容和目标产物的摘要；PR 说明给出实际结果、验证和剩余边界，不把工作区文件当作已发行。 | Compare the commit, final diff, archive contents and artifact digest. Describe actual behavior, validation and limits in the PR; a local workspace file is not release evidence. |
