from mcp import ClientSession
import asyncio
from mcp.client.streamable_http import streamable_http_client
from contextlib import AsyncExitStack

class MCPClient:
    def __init__(self, url):
        self.url = url
        self.stack = AsyncExitStack()
        self._session = None
    
    async def list_tools(self):
        async with self._session as session:
            response = (await session.list_tools()).tools
            return response
        
    async def __aenter__(self):
        # Server Sent Events (SSE) connection/client with http
        read, write, _ = await self.stack.enter_async_context(
            streamable_http_client(self.url)
        )

        # Client Session provide by MCP library to use methods like list_tools, call_tool, etc.
        self._session = await self.stack.enter_async_context(
            ClientSession(read, write)
        )
        await self._session.initialize()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.stack.aclose()
        self._session = None

    # Listing tools
    async def list_tools(self):
        if self._session is None:
            raise ConnectionError(
                "Client session not initialized or cache not populated. Call connect_to_server first."
            )
        result = await self._session.list_tools()
        return result.tools

    # Calling tools
    async def call_tool(self, tool_name: str, tool_input: dict):
        if self._session is None:
            raise ConnectionError(
                "Client session not initialized or cache not populated. Call connect_to_server first."
            )
        return await self._session.call_tool(tool_name, tool_input)
    

async def main():
    async with MCPClient("http://localhost:8000/mcp") as client:
        tools = await client.list_tools()
        print(tools, "tools")

asyncio.run(main())