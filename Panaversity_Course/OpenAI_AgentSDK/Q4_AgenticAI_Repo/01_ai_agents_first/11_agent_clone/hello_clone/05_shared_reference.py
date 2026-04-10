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
    
     # 🎯 Example 5: Understanding Shared References
    print("\n🎯 Example 5: Understanding Shared References")
    print("-" * 40)
    
    # Demonstrate shared references
    original_agent = Agent(
        name="Original",
        tools=[calculate_area],
        instructions="You are helpful.",
        model=model
    )
    
    # Clone without new tools list
    shared_clone = original_agent.clone(
        name="SharedClone",
        instructions="You are creative."
    )
    
    # Add tool to original
    @function_tool
    def new_tool() -> str:
        return "I'm a new tool!"
    
    original_agent.tools.append(new_tool)
    
    # Check if clone also has the new tool
    print("Original tools:", len(original_agent.tools))  # 2
    print("Shared clone tools:", len(shared_clone.tools))  # 2 (shared!)
    
    # Create independent clone
    independent_clone = original_agent.clone(
        name="IndependentClone",
        tools=[calculate_area],  # New list
        instructions="You are independent."
    )
    
    original_agent.tools.append(new_tool)
    print("Independent clone tools:", len(independent_clone.tools))  # 1 (independent!)
    
    print("\n💡 Notice: Shared clone has the same tools as original,")
    print("   while independent clone has its own tool list!")

if __name__ == "__main__":
    main()