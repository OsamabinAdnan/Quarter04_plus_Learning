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
    
     # 🎯 Example 4: Multiple Clones from One Base
    print("\n🎯 Example 4: Multiple Clones from One Base")
    print("-" * 40)
    
    # Base agent
    base_agent = Agent(
        name="BaseAssistant",
        instructions="You are a helpful assistant.",
        model_settings=ModelSettings(temperature=0.7),
        model=model
    )

    # Create multiple specialized variants
    agents = {
        "Creative": base_agent.clone(
            name="CreativeWriter",
            instructions="You are a creative writer. Use vivid language.",
            model_settings=ModelSettings(temperature=0.9)
        ),
        "Precise": base_agent.clone(
            name="PreciseAssistant", 
            instructions="You are a precise assistant. Be accurate and concise.",
            model_settings=ModelSettings(temperature=0.1)
        ),
        "Friendly": base_agent.clone(
            name="FriendlyAssistant",
            instructions="You are a very friendly assistant. Be warm and encouraging."
        ),
        "Professional": base_agent.clone(
            name="ProfessionalAssistant",
            instructions="You are a professional assistant. Be formal and business-like."
        )
    }
    
    # Test all variants
    query = "Tell me about artificial intelligence."
    
    for name, agent in agents.items():
        result = Runner.run_sync(agent, query)
        print(f"\n{name} Agent:")
        print(result.final_output[:150] + "...")

if __name__ == "__main__":
    main()