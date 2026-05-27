# Class-01: Model Context Protocol - Introduction and Basic HTTP Theory, JSON-RPC

## What is MCP?

**Model Context Protocol (MCP)** is an open-source standard that enables AI applications to connect seamlessly to external data sources and tools through a standardized JSON-RPC protocol.

### Key Benefits
- **Standardized Interface**: Provides a uniform way for LLMs to interact with external systems
- **Composable Integrations**: Build once, use across multiple AI applications
- **Secure Context Sharing**: Controlled access to data sources and tools
- **Extensible Architecture**: Easy to add new capabilities and integrations
- Previously writing tool schema and running tool is responsibility of our own local server but now it is becoming the reponsibility of MCP server, which make out local server light.

---

## Core Architecture

### Three Main Participants

```
┌─────────────────────────────────────┐
│     MCP Host (AI Application)       │
│  ┌─────────┐  ┌─────────┐           │
│  │ Client 1│  │ Client 2│  ...      │
│  └────┬────┘  └────┬────┘           │
└───────┼────────────┼────────────────┘
        │            │
        │ Dedicated  │ Dedicated
        │ Connection │ Connection
        │            │
   ┌────▼────┐  ┌────▼────┐
   │ Server A│  │ Server B│
   │ (Local) │  │ (Remote)│
   └─────────┘  └─────────┘
```

#### 1. **MCP Host**
- The AI application (e.g., Claude Desktop, IDE)
- Manages multiple MCP clients
- Orchestrates communication between clients and servers

#### 2. **MCP Client**
- Connects to MCP servers
- Obtains context from servers
- Each client maintains a **dedicated connection** to one server
- Lives inside the host application

#### 3. **MCP Server**
- Provides context to clients (tools, resources, prompts)
- Can run **locally** (using STDIO transport) or **remotely** (using HTTP transport)
- Local servers typically serve a single client
- Remote servers can serve multiple clients

---

## [AI Protocols](https://github.com/panaversity/learn-agentic-ai/tree/main/03_ai_protocols)

### [HTTP Theory](https://github.com/panaversity/learn-agentic-ai/tree/main/03_ai_protocols/01_mcp/01_http_theory)

#### Core HTTP Concepts

- **Request-Response Cycle**: A client sends a request, the server processes it, and returns a response.
- **HTTP Message Structure**: Each request/response contains a start line, headers, a blank line, and optionally a body.
- **Common HTTP Methods**: `GET` fetches data, `POST` sends data, `PUT` replaces data, `PATCH` updates part of data, and `DELETE` removes data.
- **Status Codes**: `2xx` means success, `3xx` redirection, `4xx` client error, and `5xx` server error.
- **Statelessness**: HTTP treats each request independently, so apps use cookies or tokens to maintain state.
- **Headers**: Headers carry metadata such as content type, authorization, caching, and connection details.

#### Raw HTTP Messages and Their Components

**1. GET Request**

```
GET /resource/example.html HTTP/1.1
Host: example.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Connection: keep-alive
```

- **Start-Line**: `GET /resource/example.html HTTP/1.1` (method + path + version)
- **Headers**: metadata like `Host`, `User-Agent`, `Accept*`, `Connection`
- **Empty line**: separates headers from body
- **Body**: usually none for `GET`

**2. GET Response**

```
HTTP/1.1 200 OK
Date: Thu, 12 Jun 2025 08:51:00 GMT
Server: Apache/2.4.41 (Unix)
Content-Type: text/html; charset=UTF-8
Content-Length: 51
Connection: keep-alive

<html>
<head><title>Example</title></head>
<body><h1>Hello, World!</h1></body>
</html>
```

- **Start-Line**: `HTTP/1.1 200 OK` (version + status code + reason)
- **Headers**: response metadata like `Content-Type`, `Content-Length`
- **Body**: the returned content (HTML here)

**3. POST Request**

```
POST /api/submit HTTP/1.1
Host: example.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36
Accept: application/json
Content-Type: application/json
Content-Length: 47
Connection: keep-alive

{
  "name": "Alice",
  "message": "Hello, Server!"
}
```

- **Start-Line**: `POST /api/submit HTTP/1.1`
- **Headers**: `Content-Type` tells body format; `Content-Length` is body size
- **Body**: payload (JSON here)

**4. POST Response**

```
HTTP/1.1 201 Created
Date: Thu, 12 Jun 2025 08:51:05 GMT
Server: Apache/2.4.41 (Unix)
Content-Type: application/json
Content-Length: 75
Connection: keep-alive

{
  "received": {"name": "Alice", "message": "Hello, Server!"},
  "status": "success"
}
```

- **Start-Line**: `HTTP/1.1 201 Created`
- **Body**: often confirms what happened (created/accepted/processed)

![HTTP Protocol](/assets/Class01_01.png)

---

### [REST API](https://github.com/panaversity/learn-agentic-ai/tree/main/03_ai_protocols/01_mcp/02_rest) (quick notes)

An API is called `"RESTful"` because it conforms to the principles of REST (Representational State Transfer).
The suffix `"-ful"` simply means "full of" or "complying with" those exact rules. Think of it like this: an API that follows the REST style is RESTful, just like a person who shows care is careful.
The name itself was coined in the year 2000 by computer scientist `Roy Fielding` in his PhD dissertation. 

- **REST** is an architectural style for building web APIs over HTTP.
- REST works with **resources** (e.g., `users`, `products`) identified by **URIs**.
- Clients interact with resources using standard HTTP methods (CRUD mapping):
  - `GET` → Read
  - `POST` → Create
  - `PUT` → Replace (or create if absent)
  - `PATCH` → Partial update
  - `DELETE` → Remove
- Responses commonly return a **representation** of data in **JSON**.

#### Core Architectural Constraints of REST (brief)

- **Client–Server**: UI/client and server (data + logic) are separated; both can evolve independently.
- **Stateless**: each request is self-contained; server keeps no client session state.
- **Cacheable**: responses declare cache rules; caches/CDNs can reuse responses to reduce latency/load.
- **Layered system**: intermediaries (proxies, gateways, load balancers) can sit between client and server.
- **Code on demand (optional)**: server can send executable code to extend client behavior.
- **Uniform interface**:
  - Resources identified by **URIs**
  - Operate via **representations** (JSON/XML)
  - **Self-descriptive messages** (method + headers + payload)
  - **HATEOAS** links guide next actions (often not implemented)


#### REST Alternatives (industry)

Apart from REST APIs, the software industry also uses other API styles/protocols optimized for real-time streaming, complex data fetching, or high-performance systems.

| API Type | Best For | Data Format | Communication Style |
| --- | --- | --- | --- |
| **GraphQL** | Mobile apps and complex frontend data fetching | JSON | Request-Response (Flexible) |
| **gRPC** | Microservices and high-performance internal communication | Protocol Buffers (Binary) | Request-Response & Streaming |
| **WebSockets** | Real-time bi-directional apps (e.g., chat, live sports scores) | Text or Binary | Continuous, Two-way Stream |
| **SOAP** | Legacy enterprise systems, banking, and strict compliance | XML | Request-Response (Strict) |
| **Webhooks** | Event-driven notifications (e.g., payment confirmations) | JSON / XML | One-way Server Push |

### [JSON-RPC 2.0](https://github.com/panaversity/learn-agentic-ai/tree/main/03_ai_protocols/01_mcp/03_json_rpc)

#### What is JSON-RPC?
- **[JSON-RPC](https://www.jsonrpc.org/specification)** is a lightweight remote procedure call (RPC) protocol that uses **JSON** to call methods between two programs.
- It standardizes message fields like: `jsonrpc`, `method`, `params`, `id`, `result`, `error`.

#### Message Types
- **Request**: calls a method (must include an `id` if you expect a response)
- **Response**: returns either `result` (success) or `error` (failure) for the same `id`
- **Notification**: like a request but **no `id`**, so **no response** (fire-and-forget)

#### Minimal Examples

**Request**
```json
{ "jsonrpc": "2.0", "id": 1, "method": "tools/list", "params": {} }
```

**Success Response**
```json
{ "jsonrpc": "2.0", "id": 1, "result": { "tools": [] } }
```

**Error Response**
```json
{ "jsonrpc": "2.0", "id": 1, "error": { "code": -32601, "message": "Method not found" } }
```

**Notification**
```json
{ "jsonrpc": "2.0", "method": "notifications/roots/list_changed" }
```

#### JSON vs JSON-RPC (difference)
- **JSON** = data format (just data)
- **JSON-RPC** = protocol (rules for request/response using JSON)

For more detail read **[Examples](https://www.jsonrpc.org/specification)** from official JSON-RPC docs

To read about all protocol, see **[extra](https://github.com/panaversity/learn-agentic-ai/tree/main/03_ai_protocols/01_mcp/extra)** in panversity github repo

