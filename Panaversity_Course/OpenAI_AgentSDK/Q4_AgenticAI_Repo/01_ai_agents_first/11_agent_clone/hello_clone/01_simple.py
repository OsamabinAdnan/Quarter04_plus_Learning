import os
from dotenv import load_dotenv
from agents import Agent, Runner, OpenAIChatCompletionsModel, AsyncOpenAI, set_tracing_disabled, ModelSettings, function_tool

# 🌿 Load environment variables
load_dotenv()
set_tracing_disabled(disabled=True)

# 🔐 Setup Gemini client
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
BASE_URL = "https://generativelanguage.googleapis.com/v1beta/openai/"

external_client = AsyncOpenAI(api_key=GEMINI_API_KEY, base_url=BASE_URL)
model = OpenAIChatCompletionsModel(model="gemini-2.5-flash", openai_client=external_client)

# 🛠️ Simple tools for learning
@function_tool
def calculate_area(length: float, width: float) -> str:
    """Calculate the area of a rectangle."""
    area = length * width
    return f"Area = {length} × {width} = {area} square units"

@function_tool
def get_weather(city: str) -> str:
    """Get weather information for a city."""
    return f"The weather in {city} is sunny and 72°F"

def main():
    """Learn Agent Cloning with simple examples."""
    print("🧬 Agent Cloning: Create Agent Variants")
    print("=" * 50)
    
    # 🎯 Example 1: Basic Cloning
    print("\n🎯 Example 1: Basic Cloning")
    print("-" * 40)
    
    # Base agent
    base_agent = Agent(
        name="BaseAssistant",
        instructions="You are a helpful assistant.",
        model_settings=ModelSettings(temperature=0.7),
        model=model
    )
    
    # Simple clone
    friendly_agent = base_agent.clone(
        name="FriendlyAssistant",
        instructions="You are a very friendly and warm assistant."
    )
    
    # Test both agents
    query = "Hello, how are you?"
    
    result_base = Runner.run_sync(base_agent, query)
    result_friendly = Runner.run_sync(friendly_agent, query)
    
    print("Base Agent:")
    print(result_base.final_output)
    print("\nFriendly Agent:")
    print(result_friendly.final_output)

if __name__ == "__main__":
    main()