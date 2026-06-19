# [04_fundamental_ primitives](https://github.com/panaversity/learn-agentic-ai/tree/main/03_ai_protocols/01_mcp/04_fundamental_%20primitives) (Cont.)

## [05_defining_resources](https://github.com/panaversity/learn-agentic-ai/tree/main/03_ai_protocols/01_mcp/04_fundamental_%20primitives/05_defining_resources)

Resources expose data to clients, similar to GET request handlers in HTTP servers — perfect for fetching information rather than performing actions.

### MCP Resources vs. What You Know

| **Familiar concept** | **MCP Resources are like...** | **Key advantage** |
|---|---|---|
| File Systems | Files the AI can browse and read | Discoverable and structured for AI |
| REST API GET endpoints | Read-only API endpoints | Built-in metadata and categorization |
| RAG | Knowledge base for AI context | Standardized across all AI platforms |
| Documentation Sites | Docs the AI can navigate | Self-describing with rich metadata |
| Database Views | Queryable data collections | AI-friendly formatting and discovery |

### Key Characteristics

- **Read-only**: Resources provide data, not actions
- **URI-based**: Accessed via URIs with optional parameters
- **MIME-typed**: Support JSON, text, images, etc.
- **App-controlled**: Application decides when to expose resources
- **Static or templated**: Direct resources or parameterized

### URI Concept in MCP Resources

A URI is a structured address: `scheme://host/endpoint`.

**Examples:**
- `http://panaversity.com/courses/` → public web resource
- `http://127.0.0.1:8000/courses/` → local server by IP
- `http://localhost:8000/courses/` → local server by name

MCP can also use custom resource schemes:
- `docs://documents` → in-memory data or CMS
- `db://pana` → database or database API
- `file://C:\path\to\file.txt` → local file
- `s3://bucket/path/to/file.txt` → AWS S3 object
- `screen://capture` → screen capture
- `queue://task` → message queue
- `cache://key` → cache storage
- `ftp://user:password@host:port/path/to/file.txt` → FTP file

These URIs are often logical identifiers. The MCP server resolves them to the real data source.

### Resource URIs

Format: `[protocol]://[host]/[path]`

Examples:
- `file:///home/user/documents/report.pdf`
- `postgres://database/customers/schema`
- `screen://localhost/display1`

Protocol and path structure is defined by the server implementation.

### Content Types

1. **Text resources**: UTF-8 encoded (source code, config files, JSON/XML)
2. **Binary resources**: Raw binary encoded in base64 (images, PDFs, audio, video)

### How Resources Work

Request-response pattern:
- Client sends `ReadResourceRequest` with URI
- Server returns `ReadResourceResult`

Use `mime_type` to hint content type:
- `"application/json"` — structured data
- `"text/plain"` — plain text
- `"application/pdf"` — binary files

The MCP Python SDK auto-serializes return values — no manual JSON conversion needed.

### Types of Resources

#### 1. Direct Resources
Static URIs that never change. Perfect for parameterless operations.

#### 2. Templated Resources
URIs include parameters. SDK auto-parses and passes them as keyword arguments.

_Learn More:_ [MCP Resources Specification](https://modelcontextprotocol.io/specification/2025-06-18/server/resources)

### Protocol Messages

#### 1. Listing Resources

**Request:**
```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "resources/list",
  "params": { "cursor": "optional-cursor-value" }
}
```

**Response:**
```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": {
    "resources": [
      {
        "uri": "file:///project/src/main.rs",
        "name": "main.rs",
        "title": "Rust Software Application Main File",
        "description": "Primary application entry point",
        "mimeType": "text/x-rust"
      }
    ],
    "nextCursor": "next-page-cursor"
  }
}
```

#### 2. Reading Resources

**Request:**
```json
{
  "jsonrpc": "2.0",
  "id": 2,
  "method": "resources/read",
  "params": { "uri": "file:///project/src/main.rs" }
}
```

**Response:**
```json
{
  "jsonrpc": "2.0",
  "id": 2,
  "result": {
    "contents": [
      {
        "uri": "file:///project/src/main.rs",
        "name": "main.rs",
        "title": "Rust Software Application Main File",
        "mimeType": "text/x-rust",
        "text": "fn main() {\n    println!(\"Hello world!\");\n}"
      }
    ]
  }
}
```

#### 3. List Resource Templates

Templates expose parameterized resources via URI templates. Arguments can be auto-completed through the completion API.

**Request:**
```json
{
  "jsonrpc": "2.0",
  "id": 3,
  "method": "resources/templates/list"
}
```

### Exercise: Add Resources to Server

**1. Resource returning all doc IDs:**
```python
@mcp.resource(
    "docs://documents",
    mime_type="application/json"
)
def list_docs() -> list[str]:
    return list(docs.keys())
```

**2. Resource returning a specific doc's content:**
```python
@mcp.resource(
    "docs://{doc_id}",
    mime_type="text/plain"
)
def get_doc(doc_id: str) -> str:
    return docs[doc_id]
```

### Implementing Resource Reading in MCP Client

Add imports to `mcp_client.py`:
```python
import json
from pydantic import AnyUrl
```

Core function:
```python
async def read_resource(self, uri: str) -> Any:
    result = await self.session().read_resource(AnyUrl(uri))
    resource = result.contents[0]

    if isinstance(resource, types.TextResourceContents):
        if resource.mimeType == "application/json":
            return json.loads(resource.text)

    return resource.text
```

### Testing Resource Access

1. **MCP Inspector** — verify server resources are implemented correctly
2. **Postman** — explore resources in more detail
3. **CLI app** — type `@` + resource name to autocomplete, select, and inject resource content directly into the prompt (no extra tool call needed)
4. **Postman requests** — use "List Documents Resource" and "Get Document Content" to verify endpoints directly

This is smoother UX compared to having the AI make separate tool calls for data access.

### Resources

- [MCP Resource Specification](https://modelcontextprotocol.io/specification/2025-06-18#resources)
- [MIME Types Reference](https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/MIME_types)
- [URI Design Best Practices (RFC 3986)](https://tools.ietf.org/html/rfc3986)

---

In this Class we are working on [Class 04 Working](class_04_working/) folder in client and server as well

### MIME type

**MIME type (Multipurpose Internet Mail Extensions type)** is a standard that tells a system **what type of data a file or HTTP response contains**, so it knows how to handle it.

**Format:**

```
type/subtype
```

Examples:

-   `text/plain` → Plain text
-   `text/html` → HTML page
-   `application/json` → JSON data
-   `image/png` → PNG image
-   `application/pdf` → PDF file

**Why it's used:**

-   Tells browsers how to display content.
-   Tells APIs/servers what data is being sent or returned.
-   Helps applications choose the correct program or parser for a file.
-   Improves security by preventing incorrect content handling.

