import time
import os
import asyncio
from dotenv import load_dotenv, find_dotenv
from dataclasses import dataclass
from typing import Callable
from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel, set_tracing_disabled, function_tool, RunContextWrapper, ItemHelpers
from openai.types.responses import ResponseTextDeltaEvent
from rich import print

load_dotenv(find_dotenv())

# 🔐 Setup Gemini client
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
BASE_URL = "https://generativelanguage.googleapis.com/v1beta/openai/"

external_client = AsyncOpenAI(
    api_key=GEMINI_API_KEY, 
    base_url=BASE_URL
)
model = OpenAIChatCompletionsModel(
    model="gemini-2.5-flash", 
    openai_client=external_client
)

@dataclass
class UserContext:
    username : str
    email : str | None = None

@function_tool()
async def search(local_context: RunContextWrapper[UserContext], query:str) -> str:
    """Search the web for relevant information."""
    time.sleep(5) # Simulating a delay for the search operation
    return f"No results found for '{query}'"

def special_prompt(special_context: RunContextWrapper[UserContext], agent: Agent[UserContext]) -> str:
    # who is user?
    # which agent
    print(f"\nUser: {special_context.context},\n Agent: {agent.name}\n")
    return f"You are a math expert. User: {special_context.context.username}, Agent: {agent.name}. Please assist with math-related queries."

math_agent:Agent = Agent(
    name="Genius",
    instructions=special_prompt,
    model=model,
    tools=[search],
)

async def call_agent():
    user_context = UserContext(username="Alice", email="abc@example.com")

    result = Runner.run_streamed(
        starting_agent=math_agent, 
        input="search for the best math tutor in my area?",
        context=user_context
    )

    async for event in result.stream_events():
        if event.type == "raw_response_event" and isinstance(event.data, ResponseTextDeltaEvent):
            print("##DATA",event.data.delta, end="", flush=True)
            # print(event)

asyncio.run(call_agent())