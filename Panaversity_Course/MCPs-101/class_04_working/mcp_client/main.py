from mcp import ClientSession, types
import asyncio
from mcp.client.streamable_http import streamable_http_client
from contextlib import AsyncExitStack
from pydantic import AnyUrl
from pprint import pprint
import json

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

# //////////////////////////// Tools ////////////////////////////

    # Listing tools
    async def list_tools(self) -> types.ListToolsResult | list[None]:
        assert self._session, "Session is not available"
        if self._session is None:
            raise ConnectionError(
                "Client session not initialized or cache not populated. Call connect_to_server first."
            )
        result = await self._session.list_tools()
        return result.tools

    # Calling tools
    async def call_tool(self, tool_name: str, tool_input: dict):
        assert self._session, "Session is not available"
        if self._session is None:
            raise ConnectionError(
                "Client session not initialized or cache not populated. Call connect_to_server first."
            )
        return await self._session.call_tool(tool_name, tool_input)

# //////////////////////////// Resources ////////////////////////////
    # Listing resources
    async def list_resources(self) -> types.ListResourcesResult | list[None]:
        assert self._session, "Session is not available"
        if self._session is None:
            raise ConnectionError(
                "Client session not initialized or cache not populated. Call connect_to_server first."
            )
        result = await self._session.list_resources()
        return result.resources

    # Read resource
    async def read_resource(self, uri: AnyUrl) -> types.ReadResourceResult | None:
        assert self._session, "Session is not available"
        if self._session is None:
            raise ConnectionError(
                "Client session not initialized or cache not populated. Call connect_to_server first."
            )
        result = await self._session.read_resource(uri)
        pprint(f"READ RESOURCE: {result.__dict__}")
        resource = result.contents[0]
        if isinstance (resource, types.TextResourceContents):
            if resource.mimeType == "application/json":
                try:
                    return json.loads(resource.text)
                except json.JSONDecodeError as e:
                    print(f"Error decoding JSON: {e}")
            return resource.text
        return resource

    # List resources with parameter i.e., list resource templates
    async def list_resource_templates(self) -> types.ListResourceTemplatesResult| None:
        assert self._session, "Session is not available"
        if self._session is None:
            raise ConnectionError(
                "Client session not initialized or cache not populated. Call connect_to_server first."
            )
        result = await self._session.list_resource_templates()
        pprint(f"LIST RESOURCE TEMPLATES: {result.__dict__}")
        return result.resourceTemplates






async def main():
    async with MCPClient("http://localhost:8000/mcp") as client:
        tools = await client.list_tools()
        print("Tools:", tools)

        # Listing resources
        resources = await client.list_resources()
        print("Resources:", resources)

        # Reading a resource
        resource = await client.read_resource("docs://documents")
        print("Resource Content:", resource)

        # List resource templates
        print("\n@@@@@@@@@@@ Resource Templates @@@@@@@@@@@@\n")
        resource_templates = await client.list_resource_templates()
        print("\nResource Templates:", resource_templates)
asyncio.run(main())