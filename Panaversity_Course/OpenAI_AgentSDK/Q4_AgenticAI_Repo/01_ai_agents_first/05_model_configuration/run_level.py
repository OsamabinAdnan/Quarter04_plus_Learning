from dotenv import load_dotenv
import os
from rich import print
from agents import Agent, Runner, OpenAIChatCompletionsModel, set_tracing_disabled, RunConfig
from openai import AsyncOpenAI

load_dotenv()

set_tracing_disabled(True)

gemini_api_key = os.getenv("GEMINI_API_KEY")
if not gemini_api_key:
    raise ValueError("GEMINI_API_KEY environment variable not set")

client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url= "https://generativelanguage.googleapis.com/v1beta/openai/"
)

model = OpenAIChatCompletionsModel(
    model="gemini-2.5-flash", 
    openai_client=client,
)

config = RunConfig(
    model=model,
    model_provider=client,
    tracing_disabled=True,
)

agent = Agent (
    name="Assitant",
    instructions="You are helpful assistant.",
)

result = Runner.run_sync(
    agent,
    "Hello, My name is Osama bin Adnan. How are you today?",
    run_config=config,
)

print(result.final_output)