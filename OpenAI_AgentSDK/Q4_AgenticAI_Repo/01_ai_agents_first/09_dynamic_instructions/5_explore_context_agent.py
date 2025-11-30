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

# 🎯 Example 5: Exploring Context and Agent
print("\n🎭 Example 5: Exploring Context and Agent")
print("-" * 40)
def main():
    def explore_context_and_agent(context: RunContextWrapper, agent: Agent) -> str:
        """Explore what's available in context and agent."""

        # Access conversation messages
        messages = getattr(context, 'messages', [])
        message_count = len(messages)

        # Access agent properties
        agent_name = agent.name
        tool_count = len(agent.tools)

        return f"""
            You are {agent_name} with {tool_count} tools. 
            This is message #{message_count} in our conversation.
            Be helpful and informative!
            """
    
    agent_explorer = Agent(
        name="Context Explorer",
        instructions=explore_context_and_agent,
        model=model
    )
    
    result = Runner.run_sync(agent_explorer, "What can you tell me about yourself?")
    print("Context Explorer Agent:")
    print(result.final_output)

    
main()