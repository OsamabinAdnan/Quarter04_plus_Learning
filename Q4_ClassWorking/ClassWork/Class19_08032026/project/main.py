import asyncio
import os

from agents import Agent, Runner
from agents.mcp import MCPServerStdio
from dotenv import load_dotenv

load_dotenv()

GITHUB_ACCESS_TOKEN = os.getenv("GITHUB_ACCESS_TOKEN")
if not GITHUB_ACCESS_TOKEN:
    raise ValueError("GITHUB_ACCESS_TOKEN is not set in environment variables.")

async def main():

    async with MCPServerStdio(
        params = {
                "command": "npx",
                "args": [
                    "-y",
                    "@modelcontextprotocol/server-github"
                ],
                "env": {
                    "GITHUB_PERSONAL_ACCESS_TOKEN":GITHUB_ACCESS_TOKEN
                }
        },
    ) as mcp_server:
        print("MCP Server Started")

        agent = Agent(
            name="MCP Calling Agent",
            instructions=
                    """
                    You are a personal AI assistant with access to GitHub tools via MCP.
                    
                    When the user asks about a GitHub account:
                    
                    1. Use the `get_user` tool to get user information.
                    2. Use the `list_repositories` tool to count repositories.
                    3. Do NOT use search_repositories or get_file_contents for this task.
                    
                    Always ask for the GitHub username if it is not provided.
                    """,
            model="gpt-4o",
            mcp_servers=[mcp_server],
        )

        result = await Runner.run(
            agent,
            input="My GitHub username is `OsamabinAdnan`. Check my account and tell me my name and total repositories?"
        )
        print("Final Result:", result.final_output)

if __name__ == "__main__":
    asyncio.run(main())