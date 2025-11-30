# 🎭 Dynamic Instructions: Make Your Agent Adapt
# Simple examples to learn dynamic instructions

import os
from dotenv import load_dotenv
from agents import Agent, Runner, OpenAIChatCompletionsModel, AsyncOpenAI, set_tracing_disabled, RunContextWrapper
import datetime

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

 # 🎯 Example 3: Time-Based Instructions
def main():
    """Learn Dynamic Instructions with simple examples."""
    print("\n🎭 Example 3: Time-Based Instructions")
    print("-" * 40)

    def time_based (context:RunContextWrapper, agent:Agent) -> str:
        """Time-based instructions based on current hour."""
        current_hour = datetime.datetime.now().hour

        if 6 <= current_hour < 12:
            return f"You are {agent.name}. Good morning! Be energetic and positive."
        elif 12 <= current_hour < 17:
            return f"You are {agent.name}. Good afternoon! Be focused and productive."
        elif 17 <= current_hour < 19:
            return f"You are {agent.name}. Good evening! Be calm and helpful."
        else:
            return f"You are {agent.name}. Good night! Be soothing and considerate."
    

    agent_time = Agent(
        name="Time Aware Agent",
        instructions=time_based,
        model=model
    )
    
    result = Runner.run_sync(agent_time, "How are you today?")
    print("Time-Based Agent:")
    print(result.final_output)

main()