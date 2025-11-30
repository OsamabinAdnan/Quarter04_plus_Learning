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
    
    # 🎯 Example 3: Cloning with Different Tools
    print("\n🎯 Example 3: Cloning with Different Tools")
    print("-" * 40)
    
    
    # Base agent
    base_agent_with_tools = Agent(
        name="BaseAssistant",
        tools=[calculate_area],
        instructions="You are a helpful assistant.",
        model=model
    )
    
    # Clone with additional tool
    weather_agent = base_agent_with_tools.clone(
        name="WeatherAssistant",
        tools=[calculate_area, get_weather],  # New tools list
        instructions="You are a weather and math assistant."
    )
    
    # Clone with different tools
    math_agent = base_agent_with_tools.clone(
        name="MathAssistant",
        tools=[calculate_area],  # Same tools
        instructions="You are a math specialist."
    )
    
    # Test tool usage
    query = "What's the area of a 5x3 rectangle and the weather in Tokyo?"
    
    result_weather = Runner.run_sync(weather_agent, query)
    result_math = Runner.run_sync(math_agent, query)
    
    print("Weather Agent:")
    print(result_weather.final_output)
    print("\nMath Agent:")
    print(result_math.final_output)

if __name__ == "__main__":
    main()