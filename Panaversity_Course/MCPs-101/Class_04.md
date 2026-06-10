# [04_fundamental_ primitives](https://github.com/panaversity/learn-agentic-ai/tree/main/03_ai_protocols/01_mcp/04_fundamental_%20primitives) (Cont.)

## [04_implementing_client](https://github.com/panaversity/learn-agentic-ai/tree/main/03_ai_protocols/01_mcp/04_fundamental_%20primitives/04_implementing_client)

[Class-04 Code: Model Context Protocol - Implementing Core MCP Client](https://github.com/panaversity/learn-agentic-ai/blob/main/03_ai_protocols/01_mcp/04_fundamental_%20primitives/04_implementing_client/class_code)

The MCP client abstracts away the complexity of server communication, letting you focus on your application logic while still getting access to powerful external tools and data sources.

### Server-Sent Events (SSE)

**SSE (Server-Sent Events)** is a web technology that allows a **server to continuously push updates to a client (browser) over a single HTTP connection**.

**Simple Example**

Instead of the client repeatedly asking:

> "Any new data?"  
> "Any new data?"  
> "Any new data?"

The server keeps the connection open and sends updates whenever new data is available.

**SSE vs WebSocket**

-   **SSE:** Server → Client only (one-way)
-   **WebSocket:** Server ↔ Client (two-way)

**Why it's popular in AI apps**

When an LLM generates text gradually, SSE lets the server stream tokens to the browser in real time instead of waiting for the entire response to finish.

#### In MCP context

In the context of **Model Context Protocol (MCP)**:

**SSE is often used as the transport layer between an MCP client and an MCP server.**

**Why it's important**

-   **Real-time communication:** The MCP server can stream responses, tool results, logs, and progress updates to the client.
-   **Low latency:** The client receives data as it's generated instead of waiting for the entire operation to complete.
-   **Efficient:** Maintains a single long-lived HTTP connection rather than repeated polling.
-   **Streaming support:** Essential for long-running tools and LLM responses.

#### MCP Flow

```
MCP Client 
   │    
   │ HTTP + SSE    
   ▼
MCP Server    
   │    
   ├─ Tool execution    
   ├─ Resource access    
   └─ LLM interactions
```

Without SSE, an MCP client would typically need to poll the server repeatedly. With SSE, the server can push updates immediately as they occur.

Below is example code we use to make simple client
```py
import requests


URL="http://localhost:8000/mcp/"
PAYLOAD={
    "jsonrpc": "2.0",
    "method": "tools/list",
    "params": {},
    "id": 1
}
HEADERS={
    "Content-Type": "application/json",
    "Accept": "application/json,text/event-stream"
}

response = requests.post(URL, json=PAYLOAD, headers=HEADERS, stream=True)

for line in response.iter_lines():
    if line:
        print(line.decode('utf-8')) # Decode bytes to string and print
```

Below is server code

```py
from mcp.server.fastmcp import FastMCP

mcp_app = FastMCP(
    name="MCP Client",
    stateless_http=True
)

mcp_server = mcp_app.streamable_http_app()

```

Output of above code

``` py
event: message
data: {"jsonrpc":"2.0","id":1,"result":{"tools":[]}}
```
