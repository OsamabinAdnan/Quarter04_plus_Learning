from dotenv import load_dotenv
import os
from rich import print
from agents import Agent, Runner, OpenAIChatCompletionsModel, set_tracing_disabled
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

def main():
    # This agent will use the custom LLM provider
    agent_level = Agent (
        name="Assitant",
        instructions="You only respond in Spanish language.",
        model=OpenAIChatCompletionsModel(model="gemini-2.5-flash", openai_client=client),
    )

    result = Runner.run_sync(
        agent_level,
        "Hello, My name is Osama bin Adnan.",
    )

    print(result.final_output)

main()