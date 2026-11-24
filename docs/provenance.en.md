# Sources and scope

[简体中文](provenance.md) · [Home](../README.en.md)

This edition compares three sources: the maintainers’ portable Codex skills, the general working agreement and the [reviewed Qoder revision](https://github.com/liushikuan63/Qoder-Optimization/tree/9f39002a6e6713f1eb5c868ab61ad8608a1771a5). The [inventory](../inventory.json) maps each reviewed source skill to an installed workflow or gives a specific reason for keeping it upstream. To find what you can actually use, start with the [skill directory](skills.en.md) or the [project rule template](../rules/AGENTS.en.example.md).

The pack groups related practices by task. For example, the message-delivery workflow asks you to redeliver after commit but before acknowledgement and check for a single business effect. It does not install Kafka, RabbitMQ or an upstream client. The browser workflow checks the response type of a startup script so that a successful HTML fallback does not count as JavaScript loading correctly.

In the inventory, `adapted` means selected portable methods, not a complete copy of the upstream skill, assets or scripts. `upstream-only` means the named tool or procedure is not shipped; both languages give the reason. The rule mapping records reusable principles rather than another host’s absolute paths, account settings, permissions or hooks. The two optional [MCP examples](../mcp/README.en.md) are independent of skill installation.

Version 0.3.1 adapts Qoder's plain-language delivery guidance, prior troubleshooting evidence and layout checks using known failures. Its receipt-based check takes inspiration from the [DSH-Optimization deployment guide](https://github.com/liushikuan63/DSH-Optimization/blob/fa1a2c9246984cb226d54e9a0fde00fe140d7d03/docs/deployment.md) and runs in this pack's Python installer.

The project and reviewed Qoder revision use the [MIT License](../LICENSE). The Codex workflows are written for this pack. The upstream local engineering skills also credit ECC and Compound Engineering; their notices are retained in [ECC](../notices/LICENSE-ECC.txt) and [Compound Engineering](../notices/LICENSE-CE.txt). The pack does not redistribute third-party design libraries or the upstream tool collection.
