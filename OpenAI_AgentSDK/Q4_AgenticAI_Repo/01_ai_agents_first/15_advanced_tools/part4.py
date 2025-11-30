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

@function_tool()
def get_weather(city:str) -> str:
    try:
        # If Call Fails Call another service i.e get_weather_alternative
        pass
    except ValueError:
        raise ValueError("Weather Service is Down")
    except TimeoutError:
        raise TimeoutError("Weather service request timed out.")
    except Exception as e:
        raise Exception(f"An unexpected error occurred: {str(e)}")

base_agent: Agent = Agent(
    name="WeatherAgent", 
    instructions="",
    model=llm_model, tools=[get_weather]
)

async def main():
    res = await Runner.run(base_agent, "What is weather in Lahore")
    print(res.final_output)

if __name__ == "__main__":
    asyncio.run(main())