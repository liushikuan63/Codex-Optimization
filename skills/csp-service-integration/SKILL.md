---
name: csp-service-integration
description: 用于排查 API 客户端、登录回调、代理转发或流式响应。 Use when diagnosing a client, an authentication callback, a proxy or a streamed response.
---

# 服务集成与故障定位 | Service integration and diagnosis

1. 把一次请求分成客户端、代理、上游和回调。记录构建版本、请求时间、脱敏状态码及首个失败阶段；不要记录凭据，也不要用状态码猜根因。
2. 先用本地样例分别模拟正常返回、延迟首包、流中断及服务端限流。只有确认可安全重放的请求才重试，记录退避和最终结果。
3. 以应用自己的入口核验修复：登录回调最终形成有效会话，流式请求既有首包也有结束标记。上游不可用时，报告本地证明到哪一层。

按场景查找：[任务示例 / Worked examples](references/applied-methods.md)。

## English

1. Trace one request through the client, proxy, upstream and callback. Record the build, timestamps, redacted status and first failing stage. A status code alone does not identify its cause.
2. Use local fixtures for success, delayed headers, a broken stream and rate limiting. Retry only operations known to be safe to repeat; verify backoff and the final result.
3. Test through the application: a callback should establish a usable session, and a stream should deliver both data and a terminal event. State which layer was actually exercised.
