import os
from dotenv import load_dotenv
from rich import print
from agents import Agent, Runner, OpenAIChatCompletionsModel, function_tool, enable_verbose_stdout_logging, StopAtTools
from openai import AsyncOpenAI

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

@function_tool
def get_weather(city:str) -> str:
    """A simple function to get the weather for a user."""
    return f"The weather in {city} is sunny."

@function_tool
def get_travel_plan(city: str) -> str:
    """Plan Travel for your city"""
    return f"Travel Plan is not available"

base_agent = Agent(
    name="WeatherAgent",
    instructions="You are a helpful assistant.",
    model=llm_model,
    tools=[get_weather, get_travel_plan],
    tool_use_behavior=StopAtTools(stop_at_tool_names=["get_travel_plan"])
)

# res = Runner.run_sync(base_agent, "What is weather in Lahore")

res = Runner.run_sync(base_agent, "Make me travel plan for Lahore")

print(res.final_output)