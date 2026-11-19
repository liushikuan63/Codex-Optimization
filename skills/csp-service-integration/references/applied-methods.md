# 任务示例 | Worked examples

下表按来源列出本技能吸纳的具体做法。每项用目标项目自己的数据验证。
Each row identifies a method retained from its source. Use representative data from the target project.

| 来源技能 / Source | 中文操作示例 | Worked example |
| --- | --- | --- |
| `agent-client-network-triage` | 客户端能打开网页却连不上服务时，分别记录应用和浏览器的解析、连接与请求结果。用同一个公开端点对照，指出第一次出现差异的层。 | When the browser works but the client fails, compare name resolution, connection and request results for the same public endpoint. Identify the first layer that differs. |
| `byok-model-retry` | 区分认证失败、限流、空响应和流式中断；用脱敏的状态与终止标记核对。重试限于可重试错误，并确认不会造成双重计费或重复效果。 | Distinguish authentication errors, rate limits, empty responses and interrupted streams using redacted status and terminal events. Bound retries to retryable requests and check for duplicated effects or cost. |
| `local-reverse-proxy-triage` | 在自己管理的服务上对照直连与经代理的同一个只读请求，分别看响应类型、状态、超时和应用日志，确定差异发生在哪一段。 | On a service you manage, compare the same read-only request directly and through the proxy. Compare response type, status, timing and application logs to locate the differing segment. |
| `oauth-login-failure-triage` | 按浏览器授权、回调到达、令牌交换和应用读回会话分段。日志只保留脱敏的状态和时间，回调成功不能替代会话有效。 | Separate browser consent, callback arrival, token exchange and application session readback. Use redacted status and timing only; callback success does not establish a valid session. |
