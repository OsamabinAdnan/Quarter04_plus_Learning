import os
from dotenv import load_dotenv
from rich import print
from agents import Agent, Runner, OpenAIChatCompletionsModel, function_tool, enable_verbose_stdout_logging
from openai import AsyncOpenAI
import asyncio

load_dotenv()

enable_verbose_stdout_logging()

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

@function_tool
def get_weather():
  return "It is sunny"

weather_agent:Agent = Agent(
      name="weather checker",
      instructions="Use available tools get weather info",
      tools=[get_weather],
      model=llm_model
  )


@function_tool
async def weather_agent_fun(query: str) -> str:
    """You are weather tool, call weather_agent to get weather information"""
    result = await Runner.run(weather_agent, query)

    return (result.final_output)
    


agent:Agent = Agent(
    name="General Agent",
    instructions="Answer general purpose query efficently if tool call is require call available tools",
    tools=[weather_agent_fun],
    model=llm_model
)


async def main():
    result = await Runner.run(
        agent, 
        "What is the weather like today?"
    )
    print(result.final_output)


if __name__ == "__main__":
    asyncio.run(main())
