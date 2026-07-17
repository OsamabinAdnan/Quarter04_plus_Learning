# [05_capabilities_and_transport](https://github.com/panaversity/learn-agentic-ai/tree/main/03_ai_protocols/01_mcp/05_capabilities_and_transport)

**First Read** [Advanced MCP Course Lessons](https://docs.google.com/document/d/1mvWO9NzzomRea_uJuKHEoiyswGVJTpkuQqjUBGalptE/)

## [01_mcp_transports](https://github.com/panaversity/learn-agentic-ai/tree/main/03_ai_protocols/01_mcp/05_capabilities_and_transport/01_mcp_transports)

---

### What Is the MCP Transport Layer?

The Model Context Protocol defines *what* messages flow between clients and servers. The **transport layer** defines *how* those messages physically move. Two transports dominate: **STDIO** for local work and **Streamable HTTP** for production. Both speak the exact same JSON-RPC dialect — only the channel changes.

> "MCP is natively a bidirectional protocol — the client can call the server, and the server can call the client."

That bidirectionality is the core tension. HTTP is natively unidirectional (request → response), so MCP uses Server-Sent Events (SSE) as a workaround to push server messages back to clients over a long-lived HTTP connection.

---

### 1. Foundational Communication Standards

#### 1.1 JSON and JSON-RPC

Every MCP message — regardless of transport — is encoded as JSON and conforms to **JSON-RPC 2.0**. Unlike REST (which scatters logic across many HTTP endpoints), JSON-RPC carries the method name and arguments *inside* the message body, so the same message structure works over any transport.

**Request example:**
```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "tools/list",
  "params": {}
}
```

**Response example:**
```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": { "tools": [] }
}
```

#### 1.2 Two Message Categories

MCP groups messages into two functional types:

| Category | Behavior | Examples |
|---|---|---|
| **Request / Response** | Synchronous; client waits for result | `tools/list`, `tools/call`, `resources/list`, `prompts/list` |
| **Notification** | Asynchronous, one-way; no response expected | `tools/list_changed`, `notifications/progress`, `notifications/resources/updated` |

Notifications are how the server "talks back" without a pending request — used for tool-list refreshes, progress bars, and resource updates.

---

### 2. The MCP Connection Lifecycle: The 3-Way Handshake

Every MCP session, on either transport, must complete a **three-step handshake** before any feature can be used. Skip a step and the server won't accept tool calls.

```
Client                              Server
  |                                    |
  |--- 1. Initialize Request --------->|   (client version + capabilities)
  |<-- 2. Initialize Result ----------- |   (server version + capabilities + Session ID)
  |--- 3. Initialize Notification ---->|   (acceptance)
  |                                    |
  |=== feature traffic begins ========|
```

**Step 1 — Initialize Request (client → server):** The client declares its MCP version and the capabilities it expects (tools, resources, prompts).

**Step 2 — Initialize Result (server → client):** The server confirms its own version and supported features. On HTTP transports, this response carries a critical **MCP Session ID** that must be echoed on every subsequent request.

**Step 3 — Initialize Notification (client → server):** A one-way `notifications/initialized` message telling the server the proposal was accepted.

> Without all three, `tools/call`, `resources/read`, etc. will be rejected.

---

### 3. Transport: STDIO

STDIO is the **original** MCP transport and remains the standard for local development.

#### 3.1 How It Works

- Both processes live on **the same machine**
- The client **launches** the server as a subprocess and pipes its `stdin` / `stdout`
- Messages travel through **RAM**, not the network

```
┌─────────────┐  stdin / stdout  ┌─────────────┐
│   Client    │ ───────────────► │   Server    │
│  (parent)   │ ◄─────────────── │  (subproc)  │
└─────────────┘   (pipes)        └─────────────┘
```

#### 3.2 Strengths

- **Secure by default** — no network exposure, no auth/TLS/API-gateway work
- **Fast** — direct memory transfer, near-zero latency
- **Simple** — no ports, no DNS, no certificates
- **Bidirectionality comes for free** — both `stdin` and `stdout` are full-duplex streams

#### 3.3 Limitation

- **Local only.** The moment you need cloud hosting, multi-user, or shared infrastructure, STDIO can't follow.

> "STDIO is the most ideal implementation of the MCP specification, but its biggest limitation is that it cannot be deployed in production."

---

### 4. Transport: Streamable HTTP (SSE)

To bring MCP to the cloud, the protocol sits on **Streamable HTTP** — standard HTTP/1.1 with an open-ended response stream (Server-Sent Events) for server-to-client traffic.

#### 4.1 The HTTP Bidirectionality Problem

Plain HTTP is stateless and unidirectional. To fake bidirectional communication, MCP "cheats" using SSE.

> "In HTTP, we used a technique to cheat... we used the HTTP protocol to do the work of WebSockets to introduce bidirectional conversation."

#### 4.2 How SSE Works

- The client opens a **long-lived HTTP request**
- The server **keeps the response open**, sending chunks as they become available instead of closing after the first payload
- Client requests flow over **POST**, server events flow over the **GET-style open stream**

```
Client                                Server
  |                                      |
  |--- POST (e.g. tools/call) --------->|
  |                                      |
  |<── HTTP 200 + chunked stream ─────── |  (initial response)
  |     data: {...event 1...}            |
  |     data: {...event 2...}            |
  |     data: {...event 3...}            |  (server pushes events)
  |                                      |
  |--- POST (next request) ------------->|
  |<── more chunks ────────────────────── |
```

#### 4.3 Two Modes: Stateful vs Stateless

| Aspect | Stateful (default) | Stateless (`stateless_http=True`) |
|---|---|---|
| **Session ID** | Issued and tracked in memory | Not used |
| **3-way handshake** | Required | Bypassed |
| **Server-initiated push** | ✅ Full SSE streaming | ❌ Request/response only |
| **Notifications** | ✅ `tools/list_changed`, progress, etc. | ❌ Lost |
| **Horizontal scaling** | ❌ Session pinned to one instance | ✅ Any instance handles any request |
| **Best for** | Single-server deployments, demos, dev | Cloud production behind a load balancer |

```python
# FastMCP: choose at construction time
mcp = FastMCP("hello_mcp", stateless_http=True)   # stateless
mcp = FastMCP("hello_mcp")                        # stateful (default)
```

> "If you use `stateless_http=True`, you get horizontal scalability, but the downside is you will lose the streaming options, notifications, and tool lists."

---

### 5. Production Scalability Challenges

#### 5.1 The Session ID Conflict

In a stateful HTTP setup, Server Instance A issues a Session ID. If a load balancer routes the next request to Server Instance B, B has no record of that session and the call fails.

#### 5.2 The Workaround

Use `stateless_http=True` so any server instance can answer any request. Trade-off accepted: no live streaming, no server-pushed notifications.

```
            ┌──►  Server A  ──┐
Client ─────┼──►  Server B  ──┼──►  MCP API
            └──►  Server C  ──┘
                  (stateless: any instance can answer)
```

#### 5.3 Decision Matrix

| Need | Choose |
|---|---|
| Local dev, single user, fast iteration | **STDIO** |
| Single-server cloud deployment, need streaming/notifications | **Stateful HTTP** |
| Multi-instance production behind a load balancer | **Stateless HTTP** (`stateless_http=True`) |
| Live progress bars, tool-list refresh notifications, server logs | **Stateful HTTP** (or STDIO) |

---

### 6. Transport Comparison

| Feature | STDIO | Streamable HTTP (Stateful) | Streamable HTTP (Stateless) |
|---|---|---|---|
| Environment | Local / single machine | Production / remote, single instance | Production / massive scale |
| Bidirectional | Native (stdin/stdout) | Simulated via SSE | Request/response only |
| 3-way handshake | Required | Required | Bypassed |
| Session ID | Not needed (implicit) | Required, in-memory | Not used |
| Network security needed | No | Yes (TLS, auth, gateway) | Yes |
| Server-pushed notifications | Yes | Yes | No |
| Horizontal scaling | N/A | Hard | Easy |
| Typical use case | Dev / desktop assistants | Demos, single-node prod | Multi-node cloud |

---

### 7. Practical Implications

#### 7.1 Why SSE Accept Headers Matter

When a client talks to a streamable HTTP server, it must advertise SSE support, otherwise the server rejects the request:

```http
POST /mcp/ HTTP/1.1
Host: localhost:8000
Accept: text/event-stream, application/json
Content-Type: application/json

{"jsonrpc":"2.0","id":1,"method":"tools/list","params":{}}
```

A client that only advertises `application/json` will hit:

```json
{
  "jsonrpc": "2.0",
  "id": "server-error",
  "error": {
    "code": -32600,
    "message": "Not Acceptable: Client must accept text/event-stream"
  }
}
```

#### 7.2 Choosing Between Transports

- **Cursor / Claude Desktop → STDIO** — desktop hosts spawn the server locally
- **Production SaaS → Stateless HTTP** — scale across many instances, lose streaming
- **Hybrid → Stateful HTTP** — when you need notifications but can pin to one instance

#### 7.3 Code Configuration (FastMCP)

```python
from mcp.server.fastmcp import FastMCP

# Local dev with STDIO (default when no transport arg)
mcp = FastMCP("DocumentMCP", log_level="ERROR")
mcp.run(transport="stdio")

# Cloud prod with stateless HTTP
mcp = FastMCP("DocumentMCP", stateless_http=True)
mcp_app = mcp.streamable_http_app()
# serve with uvicorn: uvicorn main:mcp_app --host 0.0.0.0 --port 8000
```

---

### 8. Key Takeaways

1. **JSON-RPC is transport-agnostic** — same message structure on STDIO, HTTP, or anything else
2. **The 3-way handshake is mandatory** — without it, no tools, resources, or prompts work
3. **STDIO is the most spec-accurate transport** — true bidirectionality, but local-only
4. **HTTP achieves bidirectionality via SSE** — long-lived streams simulate push
5. **Stateful vs stateless is a trade-off** — streaming and notifications vs horizontal scalability
6. **For real production**, expect to combine stateless HTTP at the edge with a separate notification channel (websocket, polling) if you need live updates

> Pick your transport based on **where it runs** (local vs cloud) and **what features you need** (streaming/notifications vs scale).
