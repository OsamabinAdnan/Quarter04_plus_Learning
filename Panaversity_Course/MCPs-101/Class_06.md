# [04_fundamental_ primitives](https://github.com/panaversity/learn-agentic-ai/tree/main/03_ai_protocols/01_mcp/04_fundamental_%20primitives) (Cont.)

## [06_working_with_prompts](https://github.com/panaversity/learn-agentic-ai/tree/main/03_ai_protocols/01_mcp/04_fundamental_%20primitives/06_working_with_prompts)

Check [class_06_working](class_06_working/) working for prompt

---

## MCP — The "USB Type-C" for AI

MCP is an open, standardized protocol (over JSON-RPC) that lets AI agents discover and interact with external tools, data, and instructions without custom adapters.

> Like Type-C standardized phone charging, MCP standardizes how AI talks to its world.

It exposes **three pillars**: **Tools**, **Resources**, **Prompts**.

| Pillar | Category | Goal | Role in Context Engineering |
|---|---|---|---|
| **Tools** | Action | "To do something" | Execution & side effects |
| **Resources** | Data | "To know something" | Ground truth & knowledge |
| **Prompts** | Instruction | "To be told how" | Persona & governance |

Together they form **Context Engineering** — giving the AI the right persona (prompt), facts (resource), and ability (tool) in one cycle.

---

## Pillar 1 — Tools (Actions)

- **Purpose:** Allow the AI to create impact / side effects (run code, modify data, call APIs)
- **Format:** JSON in → JSON out
- **Methods:**
  - `tools/list` — discover available actions
  - `tools/call` — invoke a tool with arguments

**Example side effects:** creating a GitHub issue, restarting a server, executing a Python script, editing a document.

---

## Pillar 2 — Resources (Read-Only Data)

- **Purpose:** Provide safe, read-only context (documents, knowledge bases, profiles)
- **No side effects** — accessing a resource never modifies underlying data
- **Identified by URIs** (e.g. `docs://documents`, `users://{user_id}/profile`)

### Two Types

| Type | Description | URI Pattern |
|---|---|---|
| **Simple Resources** | Static data points (e.g. a markdown file) | `docs://documents` |
| **Resource Templates** | Dynamic, parameterized data | `docs://{doc_id}` |

**Why templates?** Without them, you'd need a separate resource for every record (1,000 students = 1,000 resources). Templates let the MCP server generate entries on demand.

### Methods

| Method | Purpose |
|---|---|
| `resources/list` | List static, predefined resources |
| `resources/templates/list` | Discover dynamic URI patterns |
| `resources/read` | Fetch the actual content |

> Dynamic templates do **not** appear in `resources/list` — only in `resources/templates/list`.

---

## Pillar 3 — Prompts (Structured Instructions)

Pre-defined, expert-vetted templates stored on the MCP server that give the AI a specific persona / way of working.

### Three Major Benefits

1. **Standardization (Certification):** Organizations lock specific versions (e.g., "Senior DevOps Persona") so all agents behave consistently.
2. **Versioning (Governance):** Prevents "prompt drift" — every agent uses the same vetted version.
3. **Dynamic Templating:** Prompts accept variables (e.g., `{doc_id}`, `{persona}`) and can fetch related resources before responding.

> A certified prompt acts as a **governance layer** — the AI behaves like a specific professional, not a generic assistant.

### Methods

| Method | Purpose |
|---|---|
| `prompts/list` | Discover available prompts |
| `prompts/get` | Retrieve a prompt's messages (with `User` / `Assistant` roles for the Chat Completion API) |

### Implementation in Python

```python
from mcp.server.fastmcp import FastMCP
from mcp.server.fastmcp.prompts import base

mcp = FastMCP("MyServer")

@mcp.prompt(
    name="summarize",
    title="Summarize Document",
    description="Summarize the contents of a document.",
)
def summarize_document(
    doc_id: str = Field(description="Id of the document to summarize"),
) -> list[base.Message]:
    return [base.UserMessage(f"Summarize document: {doc_id}")]
```

Under the hood, prompt communication happens via **JSON-RPC 2.0**.

---

## Resources vs Tools — Quick Distinction

| | Tools | Resources |
|---|---|---|
| **Purpose** | Actions / side effects | Read-only data |
| **Examples** | Restart server, edit document, send email | Fetch file, read profile, list docs |
| **Methods** | `tools/list`, `tools/call` | `resources/list`, `resources/read`, `resources/templates/list` |
| **Safe to retry?** | No (state changes) | Yes (idempotent) |

---

## Real-World Usage

- **`@` symbol** in Claude Desktop / Cursor → pulls in a resource
- **`/` or `\` symbol** → triggers a standardized prompt
- **MCP Inspector** → `npx @modelcontextprotocol/inspector` — visual UI for testing tools, resources, and prompts before integration

---

## Q&A Highlights

**MCP vs FastAPI?**
FastAPI is a general-purpose web framework. MCP **standardizes the AI-facing interface** — predictable schemas that LLMs are trained to interact with, so you don't write custom integrations per agent.

**Security benefit of resources?**
Read-only by design → safer for **compliance & governance**. AI can access information without accidentally modifying it; modifications require explicit tools.

---

## Hands-on Checklist

- [ ] Launch the server: `uv run uvicorn mcp_server:mcp_app --reload`
- [ ] Connect Inspector: `npx @modelcontextprotocol/inspector`
- [ ] Audit pillars: verify `tools/list`, `resources/templates/list`, `prompts/list` return expected JSON
- [ ] Test `prompts/get` — observe messages with `User`/`Assistant` roles ready for an LLM
