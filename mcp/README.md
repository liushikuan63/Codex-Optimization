# MCP：让 Codex 查官方文档

[English](README.en.md) · [返回首页](../README.md)

MCP 是 Codex 调用外部工具的一种方式。这里提供两个可选连接：OpenAI Developer Docs 查 Codex 和 OpenAI API 的官方文档；Context7 查 React、Spring 等第三方库和框架的文档。已有同一服务时，直接使用现有连接。

在终端运行 `codex mcp list` 查看已有连接。手动配置时，把 [TOML 片段](servers.example.toml) 中你需要的部分合并到 `~/.codex/config.toml`，保留其他设置。也可在终端按需运行：

```text
codex mcp add openai-docs --url https://developers.openai.com/mcp
codex mcp add context7 --url https://mcp.context7.com/mcp
```

这些命令会修改 Codex 的用户级 MCP 配置。添加 Context7 时，Codex 可能让你在浏览器登录；是否完成登录由你决定。若服务要求密钥或提示限额，参照 [Context7 安装说明](https://github.com/upstash/context7#installation) 在本机配置，别把密钥写进仓库。

重开 Codex 会话。用一条公开查询确认能取回内容，例如“请用 Context7 查 React 的 `useEffect` 清理函数何时运行，并给出文档链接”。`codex mcp list` 只能说明连接已登记；真正查到文档才说明连接可用。两项服务会收到查询文本，发送公开库名、版本和必要问题即可。

不用时运行 `codex mcp remove openai-docs` 或 `codex mcp remove context7`，只移除你为此新增的连接。更多见 [Codex 官方 MCP 指南](https://developers.openai.com/codex/mcp)。

本版已验证 Codex 能读出两条配置，Context7 能通过 MCP 返回 React 文档。发布环境访问 OpenAI Developer Docs 时收到 HTTP 403，未能验证实际查询。
