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
    
    # 🎯 Example 6: Practical Agent Family
    print("\n🎯 Example 6: Practical Agent Family")
    print("-" * 40)
    
    # Create a base agent for different writing styles
    base_writer = Agent(
        name="BaseWriter",
        instructions="You are a helpful writer.",
        model_settings=ModelSettings(temperature=0.7),
        model=model
    )
    
    # Create writing style variants
    writing_agents = {
        "Poet": base_writer.clone(
            name="Poet",
            instructions="You are a poet. Respond in verse.",
            model_settings=ModelSettings(temperature=0.9)
        ),
        "Scientist": base_writer.clone(
            name="Scientist", 
            instructions="You are a scientist. Be precise and factual.",
            model_settings=ModelSettings(temperature=0.1)
        ),
        "Chef": base_writer.clone(
            name="Chef",
            instructions="You are a chef. Talk about food and cooking."
        )
    }
    
    # Test all writing styles
    query = "What is love?"
    
    for name, agent in writing_agents.items():
        result = Runner.run_sync(agent, query)
        print(f"\n{name}:")
        print(result.final_output[:100] + "...")
    
    print("\n🎉 You've learned Agent Cloning!")
    print("💡 Try creating your own agent families!")

if __name__ == "__main__":
    main()