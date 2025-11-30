# 🎭 Dynamic Instructions: Make Your Agent Adapt
# Simple examples to learn dynamic instructions

import os
from dotenv import load_dotenv
from agents import Agent, Runner, OpenAIChatCompletionsModel, AsyncOpenAI, set_tracing_disabled, RunContextWrapper

# 🌿 Load environment variables
load_dotenv()
set_tracing_disabled(disabled=True)

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

 # 🎯 Example 1: Basic Dynamic Instructions
def main():
    """Learn Dynamic Instructions with simple examples."""
    print("\n🎭 Example 1: Basic Dynamic Instructions")
    print("-" * 40)

    def basic_dynamic (context:RunContextWrapper, agent:Agent) -> str:
        """Basic dynamic instructions function."""
        return f"You are {agent.name}. Be helpful and friendly."
    

    agent_basic = Agent(
        name="BasicAgent",
        instructions=basic_dynamic,
        model=model
    )

    result = Runner.run_sync(
        agent_basic,
        "Hello!"
    )

    print(f"Agent Response: {result.final_output}\n")

main()