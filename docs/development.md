# 开发与验证

[English](development.en.md) · [返回首页](../README.md)

每项技能放在独立目录，目录名与 `SKILL.md` 的 `name` 一致。简介写清何时该用、何时不必用。详细步骤放在 `references/`，避免让主页挤满边界条件。

修改脚本时，说明依赖、参数、会写入的文件，以及遇到冲突会怎样。尽量保留能区分正常与异常的用例，例如同名技能存在时，安装失败且原文件不变。改动中英说明时，两份一起更新。

```text
python -m pip install -r requirements-visual.txt
python -m unittest discover -s tests -v
```

测试在临时项目里运行安装、卸载和引用检查。在 Codex 里验证时，另查它是否发现了技能、是否加载了项目规则。MCP 则要实际查一次文档；出现在连接列表里只能说明已登记。

## 说明怎么写

首页沿用 Qoder 的阅读顺序：先说这个包有什么用，给出下载入口和内容清单，再给首次安装命令。把升级、排错和来源细节分别放进专题说明。中英文使用同一顺序、版本、数量和例子；新增技能或规则时，同时更新两份清单和发布说明。命令尽量让读者只需替换一个项目路径，并说明执行后能看到什么。

## 发布检查

另取一份上游仓库，用下面的命令核对。也可以指向上游新版，先看到哪些条目需要复核，再更新清单。维护者发布前可加 `--personal-skills` 和一个或多个个人技能目录，并用 `--personal-rules` 指向本机工作约定；本机文件无需上传。来源有变化时，先审阅实际修改，再更新对应的记录。提交改动后运行：

```text
python -X utf8 scripts/check_coverage.py --upstream /path/to/Qoder-Optimization
python -X utf8 scripts/build_release.py --output Codex-Optimization.zip
```

输出文件请用新路径。脚本逐项比对 ZIP 文件的名称和内容。CI 在 Windows 和 Linux 上运行检查；发布流程还会核对上游当前分支。正式发布前，从 ZIP 安装到干净项目，确认 Codex 能发现技能、能读到所选的规则模板。

## 问题排查

如果安装前已有同名技能，换一个项目试用，或先处理原有技能。若安装被中断，查看目标 `.agents/skills` 下的收据和文件；先备份自己的内容，确认归属后再处理残留。不要把整个技能目录当成包的文件一并删除。

发布前检查本次提交和 ZIP，确认没有本地账号、密钥和工作区数据。版本见 `VERSION`。
