# 任务示例 | Worked examples

下表按来源列出本技能吸纳的具体做法。每项用目标项目自己的数据验证。
Each row identifies a method retained from its source. Use representative data from the target project.

| 来源技能 / Source | 中文操作示例 | Worked example |
| --- | --- | --- |
| `mechanize-rule-into-hook-guard`, `rules-conflict-audit` | 先说明规则的适用条件、优先级和例外，再决定是否要机器检查。准备一条应放行和一条应拦截的输入；宿主不支持时说明局限。 | Define applicability, precedence and exceptions before automating a rule. Try one case that should pass and one that should be stopped. State host limitations. |
| `merge-inbound-qoder-package`, `skill-authoring-closure` | 对照来源、实际目录、安装收据与宿主技能列表；只更新能证明来自旧版且未被改动的内容，记录新条目和冲突。 | Reconcile sources, actual folders, install receipts and host discovery. Update only contents known to be unmodified copies of an old version; record additions and conflicts. |
| `skill-description-route-cue-rewrite`, `skill-tiering-lazy-load`, `skills-router` | 为技能写一个应该调用和一个不应调用的例子；把细节移到按需参考，检查入口仍可发现。区分人工核对、宿主发现和真实触发。 | Write one prompt that should use the skill and one that should not. Move detail into on-demand references and confirm discovery. Distinguish editorial review, discovery and actual routing. |
| `skill-reference-integrity-audit`, `skill-trim-with-capability-transfer` | 精简前列出独有能力及其调用者；迁移到保留的入口后，从安装目录检查引用并执行一条代表性用例，再移除旧入口。 | List unique capabilities and callers before consolidation. After moving them into a retained entry, check links from the installation and exercise one representative case before retiring the old entry. |
