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

# 🎯 Example 4: Stateful Instructions (Remembers)
print("\n🎭 Example 4: Stateful Instructions")
print("-" * 40)
def main():
    """Learn Dynamic Instructions with simple examples."""

    class StatefulInstructions:
        """Stateful instructions that remember interaction count."""
        def __init__(self):
            self.interaction_count = 0
        
        def __call__(self, context: RunContextWrapper, agent: Agent) -> str:
            self.interaction_count += 1

            if self.interaction_count == 1:
                return "You are a learning assistant. This is our first interaction - be welcoming!"
            elif self.interaction_count <= 3:
                return f"You are a learning assistant. This is interaction #{self.interaction_count} - build on our conversation."
            else:
                return f"You are an experienced assistant. We've had {self.interaction_count} interactions - be efficient."
    
    instruction_gen = StatefulInstructions()
    

    agent_stateful = Agent(
        name="Stateful Agent",
        instructions=instruction_gen,
        model=model
    )
    
    # Test multiple interactions

    for i in range(3):
        result = Runner.run_sync(
            agent_stateful,
            f"Question {i+1}: Tell me a fun fact about AI? briefly.",
        )
        print(f"\nInteraction {i+1}:")
        print(result.final_output[:100]+ "...")  # show only first 100 chars of output
        print() # blank line for readability

main()