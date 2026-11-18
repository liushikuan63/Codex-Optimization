# 批量文本改写预检

适用于同构替换、台账状态、固定列数据及曾被编码或转义破坏的文件。改个普通单点时用现有编辑工具和正常差异检查即可。

- 取得实际文件路径、范围和当前字节；对并发写入先核对占用、约定唯一写入者。内容或哈希变化说明发生变化；时间戳、陌生备份和未见记录都不能证明是谁写的。
- 优先语法解析器或项目生成器。仅在允许字面量改写时用完整语义上下文或唯一锚点。每条改写在原始快照验证命中数；0 次或多次先解决歧义。依赖上一条产物的替换应拆分验证，避免同一轮误改新增内容。
- 写盘前准备完整候选差异，检查每项前置条件、未触及行和原编码/BOM/换行。多文件时先全部预检；不能原子提交则明确部分失败后的识别和恢复办法。写前按字节或哈希确认仍是已审快照，变更后重新读入判断，不能盲目覆盖。
- 写后重新读取实际文件，跑解析或项目检查，核对旧锚点/新行和其他段落；验证有用时用一个失配或重复锚点作负例。回退前比较安装后哈希，保护后续改动。

来源：MIT 仓库 [structured-edit-safety](https://github.com/liushikuan63/Qoder-Optimization/tree/fe929cf1de22d4312b9526536568161d2a674439/skills/structured-edit-safety)、[safe-text-editing](https://github.com/liushikuan63/Qoder-Optimization/tree/fe929cf1de22d4312b9526536568161d2a674439/skills/safe-text-editing)、[concurrent-edit-attribution-check](https://github.com/liushikuan63/Qoder-Optimization/tree/fe929cf1de22d4312b9526536568161d2a674439/skills/concurrent-edit-attribution-check)；不复用外部写盘器。
