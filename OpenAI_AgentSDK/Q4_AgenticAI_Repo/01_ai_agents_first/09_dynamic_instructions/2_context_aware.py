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

# 🎯 Example 2: Context-Aware Instructions
def main():
    """Learn Dynamic Instructions with simple examples."""
    print("\n🎭 Example 2: Context-Aware Instructions")
    print("-" * 40)

    def context_aware (context:RunContextWrapper, agent:Agent) -> str:
        """Context-aware instructions based on message count."""
        message_count = len(getattr(context, 'messages', []))

        if message_count == 0:
            return "You are a welcoming assistant. Introduce yourself!"
        elif message_count == 1:
            return "You are a helpful assistant. Be encouraging and detailed."
        elif message_count == 2:
            return "You are an experienced assistant. Be concise but thorough."
    

    agent_context = Agent(
        name="Context Aware Agent",
        instructions=context_aware,
        model=model
    )
    
    # Test with multiple messages
    result1 = Runner.run_sync(agent_context, "Hello!")
    print("First message:")
    print("=" * 40)
    print(result1.final_output)
    
    result2 = Runner.run_sync(agent_context, "Tell me about Python")
    print("\nSecond message:")
    print("=" * 40)
    print(result2.final_output)

    result3 = Runner.run_sync(agent_context, "What is life?")
    print("\nThird message:")
    print("=" * 40)
    print(result3.final_output)

main()