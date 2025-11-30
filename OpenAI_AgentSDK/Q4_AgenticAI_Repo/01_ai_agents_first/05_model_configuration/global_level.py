from dotenv import load_dotenv
import os
from rich import print
from agents import Agent, Runner, AsyncOpenAI, set_default_openai_client, set_tracing_disabled, set_default_openai_api

load_dotenv()


gemini_api_key = os.getenv("GEMINI_API_KEY")
if not gemini_api_key:
    raise ValueError("GEMINI_API_KEY environment variable not set")

set_tracing_disabled(True)
set_default_openai_api("chat_completions")

client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url= "https://generativelanguage.googleapis.com/v1beta/openai/"
)

set_default_openai_client(client)

agent : Agent = Agent(
    name="Assitant",
    instructions="You are helpful assistant.",
    model="gemini-2.5-flash",
)

result = Runner.run_sync(
    agent,
    "Hello, My name is Osama bin Adnan?",
)

print(result.final_output)