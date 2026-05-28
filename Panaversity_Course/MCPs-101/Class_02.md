# [04_fundamental_ primitives](https://github.com/panaversity/learn-agentic-ai/tree/main/03_ai_protocols/01_mcp/04_fundamental_%20primitives)

We have created **[01-hello_mcp_server](https://github.com/panaversity/learn-agentic-ai/tree/main/03_ai_protocols/01_mcp/04_fundamental_%20primitives/01_hello_mcp_server)**, check project in folder as well [hello_mcp](hello_mcp/)

**[02_project_setup](https://github.com/panaversity/learn-agentic-ai/tree/main/03_ai_protocols/01_mcp/04_fundamental_%20primitives/02_project_setup)** is our assignment

Now we will learn **[03_defining_tools](https://github.com/panaversity/learn-agentic-ai/tree/main/03_ai_protocols/01_mcp/04_fundamental_%20primitives/03_defining_tools)**:

## 03_defining_tools

In this step, you'll learn how to create and use MCP tools with the FastMCP Python SDK. This guide will show you how to turn your Python functions into easy-to-use tools with minimal hassle.

### How Tools Work: Discovery and Execution

- **Finding Tools**: MCP client sends `tools/list` request to discover available tools
- **Using Tools**: Client sends `tools/call` request with tool name and required parameters
- **Handling Errors**: Python exceptions are automatically converted to MCP error responses (e.g., missing document errors)

![Tools Works](/assets/Class02_01.png)

#### 1. Defining Tools with `@mcp.tool`

Using the `@mcp.tool` decorator, you can convert a regular Python function into an MCP tool. The decorator uses Python's type hints and Pydantic's `Field` to automatically create a clear, friendly interface. This means you don't have to write complex JSON schemas by hand.

_Learn More:_ [MCP Tools Documentation](https://modelcontextprotocol.io/specification/2025-06-18/server/tools)

#### 2. Listing Tools

To discover available tools, clients send a `tools/list` request. This operation supports pagination.

**Request**:

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "tools/list",
  "params": {
    "cursor": "optional-cursor-value"
  }
}
```

**Response:**

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": {
    "tools": [
      {
        "name": "get_weather",
        "title": "Weather Information Provider",
        "description": "Get current weather info",
        "inputSchema": {
          "type": "object",
          "properties": {
            "location": {
              "type": "string",
              "description": "City name or zip code"
            }
          },
          "required": ["location"]
        }
      }
    ],
    "nextCursor": "next-page-cursor"
  }
}
```

#### 3. Calling Tools

To invoke a tool, clients send a `tools/call` request:

**Request:**

```json
{
  "jsonrpc": "2.0",
  "id": 2,
  "method": "tools/call",
  "params": {
    "name": "get_weather",
    "arguments": {
      "location": "New York"
    }
  }
}
```

**Response:**

```json
{
  "jsonrpc": "2.0",
  "id": 2,
  "result": {
    "content": [
      {
        "type": "text",
        "text": "Current weather in New York:\nTemperature: 72°F\nConditions: Partly cloudy"
      }
    ],
    "isError": false
  }
}
```

Run the code in hello_mcp for hands-on.

