import time
import os
import asyncio
from dotenv import load_dotenv, find_dotenv
from dataclasses import dataclass
from typing import Callable
from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel, set_tracing_disabled, function_tool, RunContextWrapper, ItemHelpers, RunConfig
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

config = RunConfig(
    model=model,
    model_provider=external_client,
    tracing_disabled=True
)

async def main():
    agent = Agent(
        name="Joker",
        instructions="You are a helpful assistant.",
        model=model,

    )

    result = Runner.run_streamed(agent, input="Please tell me 5 jokes.")
    async for event in result.stream_events():
        if event.type == "raw_response_event" and isinstance(event.data, ResponseTextDeltaEvent):
            print(event.data.delta, end="", flush=True)



asyncio.run(main())