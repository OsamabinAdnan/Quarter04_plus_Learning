from mcp.server.fastmcp import FastMCP


mcp = FastMCP(
    name="MCP Client",
    stateless_http=True
)

docs = {
    "deposition.md": "This deposition covers the testimony of Angela Smith, P.E.",
    "report.pdf": "The report details the state of a 20m condenser tower.",
    "financials.docx": "These financials outline the project's budget and expenditures.",
    "outlook.pdf": "This document presents the projected future performance of the system.",
    "plan.md": "The plan outlines the steps for the project's implementation.",
    "spec.txt": "These specifications define the technical requirements for the equipment.",
}

@mcp.resource(
    uri="docs://documents",
    mime_type="application/json" # Multipurpose Internet Mail Extensions type
)
def list_docs():
    """List all available documents."""
    return {"docs": list(docs.keys())}

@mcp.resource(
    uri="docs://documents/{doc_id}",
    mime_type="text/plain"
)
def get_doc_contents(doc_id: str):
    """Get the contents of a specific document."""
    if doc_id not in docs:
        raise ValueError(f"Document {doc_id} not found")
    return {"name": doc_id, "content": docs[doc_id]}


mcp_server = mcp.streamable_http_app()
