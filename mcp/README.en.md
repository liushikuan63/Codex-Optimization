# MCP: Look up documentation from Codex

[简体中文](README.md) · [Home](../README.en.md)

MCP gives Codex access to external tools. OpenAI Developer Docs covers Codex and the OpenAI API. Context7 covers third-party libraries and frameworks such as React and Spring. Reuse an existing connection if you already have one.

Run `codex mcp list` to see what is configured. To set up a connection manually, merge only the sections you need from the [TOML example](servers.example.toml) into `~/.codex/config.toml`. You can also add either service from the terminal:

```text
codex mcp add openai-docs --url https://developers.openai.com/mcp
codex mcp add context7 --url https://mcp.context7.com/mcp
```

These commands update Codex's user-level MCP settings. When you add Context7, Codex may invite you to sign in through a browser. You can decide whether to complete that step. If the service requires a key or you hit a limit, follow the [Context7 setup guide](https://github.com/upstash/context7#installation) and keep your key out of the repository.

Open a new Codex session and try a public query: “Use Context7 to find when React runs the `useEffect` cleanup function. Include a link to the documentation.” The server can appear in `codex mcp list` before it can answer queries. Send only the public library name, version, and question you need answered.

To disconnect a service you added here, run `codex mcp remove openai-docs` or `codex mcp remove context7`. See the [official Codex MCP guide](https://developers.openai.com/codex/mcp) for more detail.

For this release, Codex loaded both configuration entries, and Context7 returned React documentation over MCP. The OpenAI Developer Docs endpoint returned HTTP 403 from the release environment, so a live query there remains unverified.
