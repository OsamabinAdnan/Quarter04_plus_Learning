import sys
import asyncio
import os
from pathlib import Path
from dotenv import load_dotenv
from contextlib import AsyncExitStack

# Add project root to sys.path so the root-level `mcp_client.py` is importable
sys.path.insert(0, str(Path(__file__).resolve().parent))

from mcp_client import MCPClient
from core.agent_service import AgentService
from core.cli_chat import CliChat
from core.cli import CliApp

load_dotenv()

# 9router (local LLM proxy) config
model = os.getenv("LLM_MODEL", "kiro-and-openai")
api_key = os.getenv("LLM_MODEL_API_KEY", "dummy-key")
base_url = os.getenv("LLM_CHAT_COMPLETION_URL", "http://localhost:20128/v1")
mcp_server_url = os.getenv("MCP_SERVER_URL", "http://localhost:8000/mcp/")

# Validate configuration
assert model, "Error: LLM_MODEL cannot be empty. Update .env"
print(f"Using model: {model}")
print(f"Using base URL: {base_url}")
print(f"MCP server URL: {mcp_server_url}")


async def main():
    agent_service = AgentService(
        model=model,
        api_key=api_key,
        base_url=base_url,
    )

    clients: dict[str, MCPClient] = {}

    async with AsyncExitStack() as stack:
        doc_client = await stack.enter_async_context(
            MCPClient(server_url=mcp_server_url)
        )
        clients["doc_client"] = doc_client

        chat = CliChat(
            doc_client=doc_client,
            clients=clients,
            agent_serve=agent_service,
        )

        cli = CliApp(chat)
        await cli.initialize()
        await cli.run()


if __name__ == "__main__":
    if sys.platform == "win32":
        asyncio.set_event_loop_policy(asyncio.WindowsProactorEventLoopPolicy())
    asyncio.run(main())
