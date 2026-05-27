# Class 02

from mcp.server.fastmcp import FastMCP

mcp = FastMCP(
    name="hello_mcp",
    stateless_http=True
)

@mcp.tool()
def hello(name:str):
    return f"Hello {name}"

@mcp.tool()
def search_online(query:str):
    return f"Results for {query}"


# command to run below mcp server `uv run uvicorn main:mcp_app`
# Transport
mcp_app = mcp.streamable_http_app()