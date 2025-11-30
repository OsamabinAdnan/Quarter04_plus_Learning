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
    
    # 🎯 Example 2: Cloning with Different Settings
    print("\n🎯 Example 2: Cloning with Different Settings")
    print("-" * 40)
    
    
    # Base agent
    base_agent = Agent(
        name="BaseAssistant",
        instructions="You are a helpful assistant.",
        model_settings=ModelSettings(temperature=0.7),
        model=model
    )
    
     # Clone with different temperature
    creative_agent = base_agent.clone(
        name="CreativeAssistant",
        instructions="You are a creative writing assistant.",
        model_settings=ModelSettings(temperature=0.9)  # Higher creativity
    )
    
    precise_agent = base_agent.clone(
        name="PreciseAssistant", 
        instructions="You are a precise, factual assistant.",
        model_settings=ModelSettings(temperature=0.1)  # Lower creativity
    )
    
    # Test creativity levels
    query = "Describe a sunset."
    
    result_creative = Runner.run_sync(creative_agent, query)
    result_precise = Runner.run_sync(precise_agent, query)
    
    print("Creative Agent:")
    print(result_creative.final_output)
    print("\nPrecise Agent:")
    print(result_precise.final_output)

if __name__ == "__main__":
    main()