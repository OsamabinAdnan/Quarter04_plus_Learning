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

# A focused sub-agent
proofreader = Agent(
    name="Proofreader",
    instructions="Fix grammar and punctuation. Keep meaning. Reply only with the corrected text.",
    model=llm_model
)

@function_tool
async def proofread_text(text: str) -> str:
    """Fix grammar and punctuation; return only corrected text."""
    result = await Runner.run(proofreader, text, max_turns=3)
    return str(result.final_output)

# Main agent that uses the proofreader as just another tool
teacher_agent = Agent(
    name="Teacher",
    instructions="Help students write clearly. Use tools when asked to fix text.",
    tools=[proofread_text],
    model=llm_model
)

async def main():
    # Example A: ask for Spanish translation
    result = await Runner.run(
        teacher_agent, 
        "Please Profread: She dont like going to the park anymore, its boring and there's too much people. I told her we can go somewhere else but she just ignore me."
    )

    print(f"Final reply: {result.final_output}")

if __name__ == "__main__":
    asyncio.run(main())