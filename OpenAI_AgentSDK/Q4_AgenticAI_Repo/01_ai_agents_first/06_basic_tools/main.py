import os
from dotenv import load_dotenv
from agents import (
    Agent, 
    Runner, 
    OpenAIChatCompletionsModel,
    function_tool,
    set_default_openai_client,
    )
from openai import AsyncOpenAI
from rich import print

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    raise Exception("Please set the GEMINI_API_KEY environment variable")

BASE_URL= os.getenv("BASE_URL")
if not BASE_URL:
    raise Exception("Please set the BASE_URL environment variable")

# 🌐 Initialize the AsyncOpenAI-compatible client with Gemini details
external_client: AsyncOpenAI = AsyncOpenAI(
    api_key=GEMINI_API_KEY,
    base_url=BASE_URL,
)

# 🧠 Model Initialization
model: OpenAIChatCompletionsModel = OpenAIChatCompletionsModel(
    model="gemini-2.5-flash",        # ⚡ Fast Gemini model
    openai_client=external_client
)

# 🛠️ Define tools (functions wrapped for tool calling)
@function_tool
def multiply(a: int, b: int) -> int:
    """Exact multiplication (use this instead of guessing math)."""
    multiplying = a * b
    return f"The product of {a} and {b} is {multiplying}."

@function_tool
def sum(a: int, b: int) -> int:
    """Exact addition (use this instead of guessing math)."""
    adding = a + b
    return f"The sum of {a} and {b} is {adding}."

# 🤖 Create agent and register tools
agent: Agent = Agent(
    name="Assistant",  # 🧑‍🏫 Agent's identity
    instructions=(
        "You are a helpful assistant. "
        "Always use tools for math questions. Always follow DMAS rule (division, multiplication, addition, subtraction). "
        "Explain answers clearly and briefly for beginners."
    ),
    model=model,
    tools=[multiply, sum],  # 🛠️ Register tools here
)

# 🧪 Run the agent with a prompt (tool calling expected)
prompt = "what is 19 + 23 * 2?"
result = Runner.run_sync(
    agent, 
    prompt
)

# 📤 Print the final result from the agent
print("\n🤖 CALLING AGENT\n")
print(result.final_output)