import asyncio
import os
from dotenv import load_dotenv, find_dotenv
from agents import Agent, Runner, OpenAIChatCompletionsModel, function_tool, RunContextWrapper, RunConfig
from openai import AsyncOpenAI
from rich import print
import time
from pydantic.dataclasses import dataclass

load_dotenv(find_dotenv())

gemini_api_key=os.getenv("GEMINI_API_KEY")
if not gemini_api_key:
    raise Exception("GEMINI_API_KEY is not set. Please set it in the .env file.")

external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

model = OpenAIChatCompletionsModel(
    model="gemini-2.5-flash-lite",
    openai_client=external_client,
)

run_config = RunConfig(
    model=model,
)

@dataclass
class UserContext:
    username: str
    email: str | None = None

@function_tool
async def search (local_context:RunContextWrapper[UserContext], query:str):
    time.sleep(10) # Simulating a delay for the search operation
    return "No result found"

async def special_prompt(special_context:RunContextWrapper[UserContext], agent:Agent[UserContext]) -> str:
    print(f"\nUser: {special_context.context}, Agent: {agent.name}")
    return f"You are a math expert. User: {special_context.context.username}, Agent: {agent.name}. Please answer the question of maths and its concepts step by step with reasoning."

math_agent = Agent(
    name="Genius",
    instructions=special_prompt,
    model=model,
    tools=[search],
)
# [{"role": "system", "content": "..."}, {"role": "user", "content": "..."}, {"role": "assistant", "content": "..."}]

async def call_agent():
    # Call the agent with a specific input
    user_context = UserContext(username="Osama bin Adnan", email="H5VtJ@example.com")

    output = await Runner.run(
        starting_agent=math_agent, 
        input="""
        Greet with me by name and solve and
        - Differentiate f(x) = x^3 + 5x^2 - 7x + 2
        """,
        context=user_context
        )
    print(f"\n\nOutput: {output.final_output}\n\n")
    
asyncio.run(call_agent())
