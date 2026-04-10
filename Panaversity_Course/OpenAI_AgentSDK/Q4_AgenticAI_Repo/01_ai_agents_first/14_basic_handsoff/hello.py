import os
from dotenv import load_dotenv
from rich import print
from agents import Agent, Runner, OpenAIChatCompletionsModel, AsyncOpenAI, handoff, set_tracing_disabled, ModelSettings, function_tool, enable_verbose_stdout_logging
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

# 1) Two specialists that will OWN the conversation after transfer
billing_agent = Agent(
    name="Billing Agent",
    instructions="Resolve billing problems end-to-end. Ask for any details you need.",
    model=llm_model,
)

refunds_agent = Agent(
    name="Refunds Agent",
    instructions="Handle refunds end-to-end. Ask for order ID and explain next steps.",
    model=llm_model,
)

# 2) Triage agent that decides WHO should take over
triage = Agent(
    name="Triage Agent",
    instructions=(
        "Greet the user and decide where to send them:\n"
        "- If the user asks about a double charge, invoice, payment, etc., hand off to Billing Agent.\n"
        "- If the user asks about refund status or returning an item, hand off to Refunds Agent.\n"
        "Once handed off, the specialist should continue the conversation."
    ),
    # You can list the agents directly or wrap with handoff(...) for later customization
    handoffs=[billing_agent, handoff(refunds_agent)],
    model=llm_model,
)

async def main():
    # Example A: A refund-style question → should hand off to Refunds Agent
    r1 = await Runner.run(triage, "Hi, I returned my headset last week. What's my refund status?")
    print("A) Final reply (from REFUNDS specialist):", r1.final_output, "\n")

    # Example B: A billing-style question → should hand off to Billing Agent
    r2 = await Runner.run(triage, "My card was charged twice for the same order.")
    print("B) Final reply (from BILLING specialist):", r2.final_output)


if __name__ == "__main__":
    asyncio.run(main())