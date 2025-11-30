import os
from dotenv import load_dotenv
from rich import print
from agents import Agent, Runner, OpenAIChatCompletionsModel, function_tool, enable_verbose_stdout_logging, StopAtTools, MaxTurnsExceeded, RunContextWrapper, AgentBase
from dataclasses import dataclass
from openai import AsyncOpenAI
import asyncio


load_dotenv()

# enable_verbose_stdout_logging()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY environment variable not set")

BASE_URL = os.getenv("BASE_URL")
if not BASE_URL:
    raise ValueError("BASE_URL environment variable not set")

# 1. Which LLM Service?
external_client: AsyncOpenAI = AsyncOpenAI(
    api_key=GEMINI_API_KEY,
    base_url=BASE_URL,
)

# 2. Which LLM Model?
llm_model: OpenAIChatCompletionsModel = OpenAIChatCompletionsModel(
    model="gemini-2.5-flash",
    openai_client=external_client
)

@dataclass
class UserScope:
    is_admin:bool

async def is_weather_allowed(ctx:RunContextWrapper[UserScope], agent:AgentBase[UserScope]) -> bool:
    print(f"Checking if weather is allowed... {ctx.context}")
    return True if ctx.context.is_admin else False

@function_tool(is_enabled=is_weather_allowed)
def get_weather(city: str) -> str:
    return f"Sunny"

base_agent = Agent(
    name="WeatherAgent",
    instructions="""
        You are weather agent.
        - Use tools to get weather.
        - if tool result is bool value True then allow get_weather tool to answer.
        - if tool result is bool value False then deny get_weather tool to answer and simply refuse to answer about weather.
    """,
    model=llm_model,
    tools=[get_weather],

)

async def main():
    abdul_scope = UserScope(is_admin=False)
    result = await Runner.run(
        base_agent,
        "What is weather in Lahore",
        context=abdul_scope
    )

    print(result.final_output)

if __name__ == "__main__":
    asyncio.run(main())