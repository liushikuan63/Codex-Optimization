# 派生元数据事务验收

用于安装、升级或层级迁移同时改变源文件与其派生索引、可读目录、启用回执的实现与验收。仅改正文、不生成派生文件时无需此流程。

## 需要保持的不变量

- 从同一次收集的条目生成机器索引与可读目录；暂存输出写在本任务拥有的目录，发布后的路径指向实际安装位置。子进程使用已核验版本的 builder 与依赖，检查实际导出 API；旧 builder 不支持新输出时，保留原文件并报告所需升级，不能让它直接写现役索引补救。
- 规划时保存将触及文件的内容哈希与对象身份；发布前比较预像，独占创建目标。原内容与本次新增对象都纳入同一恢复记录。单项返回成功后，还要核对最终元数据是否仍属于该事务；多文件依次发布不等于系统级原子事务。
- 回滚只撤销本事务仍拥有的对象。**读哈希后直接 unlink 仍有竞态窗口**：比较后路径可能被替换。需要删除时，先把路径撤到同卷的自有 stage，再核对实际撤入对象的身份和内容；匹配才删除。不匹配就独占还原，保留并发内容及恢复目录，报告恢复未完成。还原遇到目标已存在也不能覆盖。

## 有效验收场景

1. 正常安装或迁移后，重新收集实际条目，校验索引与可读目录一致，并确认条目指向现役路径。
2. 派生目录已发布后注入故障：没有并发写入时，源文件与全部派生文件恢复到事务前字节；不能只检查安装命令退出非零。
3. 在“所有权检查完成、删除尚未执行”的边界替换目录文件：并发新字节仍存在，旧备份可追回，进程明确返回失败/需恢复。只在检查前编辑文件不能覆盖这个窗口。
4. 用旧 builder 或缺少预期 API 的 builder 验证拒绝路径；原索引、目录和用户源文件保持可恢复，不把安全拒绝计为安装成功。

故障注入限于隔离、自有测试树。真实用户目录的检查沿原任务授权执行；该参考不授权扩大安装范围、后台监控、账号访问或外部发布。工具回调或进程被强制终止时，仍须读取恢复记录判断状态，不能由异常退出推断完整回滚。

## 来源与适配

2026-11-06 从 [Qoder-Optimization](https://github.com/liushikuan63/Qoder-Optimization) v0.0.30 候选的主安装器、直接目录安装器与技能层级迁移审查中提炼。重点来自 `install-package.cjs` 的统一发布与回滚，以及 `pkg-catalog.cjs` 新增目录文件在“快照读取到 unlink”窗口的真实丢写复现。此处独立改写方法，未复制客户端运行时或个人状态；不能把本轮 Windows 隔离验证推广为所有文件系统的原子性保证。

上游采用 [MIT License](https://github.com/liushikuan63/Qoder-Optimization/blob/main/LICENSE)，保留许可声明：

```text
MIT License

Copyright (c) 2026 liushikuan63

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
