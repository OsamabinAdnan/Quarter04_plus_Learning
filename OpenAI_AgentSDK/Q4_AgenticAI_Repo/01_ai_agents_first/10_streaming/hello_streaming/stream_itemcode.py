import time
import os
import asyncio
from dotenv import load_dotenv, find_dotenv
from dataclasses import dataclass
from typing import Callable
from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel, set_tracing_disabled, function_tool, RunContextWrapper, ItemHelpers, RunConfig
from openai.types.responses import ResponseTextDeltaEvent
from rich import print
import random

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

@function_tool
def how_many_jokes() -> int:
    return random.randint(1, 10)

async def main():
    agent = Agent(
        name="Joker",
        instructions="First call the `how_many_jokes` tool, then tell that many jokes.",
        tools=[how_many_jokes],
        model=model,
    )

    result = Runner.run_streamed(
        agent,
        input="Hello",

    )
    print("=== Run starting ===")

    async for event in result.stream_events():
        # We'll ignore the raw responses event deltas
        if event.type == "raw_response_event":
            continue
        elif event.type == "agent_updated_stream_event":
            print(f"[bold yellow]Agent State Update:[/bold yellow] {event.new_agent.name}")
        elif event.type == "run_item_stream_event":
            if event.item.type == "tool_call_item":
                print("[bold red]Tool was called[/bold red]")
            elif event.item.type == "tool_call_output_item":
                print(f"[bold blue]Tool output:[/bold blue] {event.item.output}")
            elif event.item.type == "message_output_item":
                print(f"[bold green]Message output:[/bold green]:\n\n{ItemHelpers.text_message_output(event.item)}")
            else:
                pass
        else:
            raise Exception(f"Unknown event type: {event.type}")

try:
    asyncio.run(main())
except:
    pass
print("=== Run complete ===")