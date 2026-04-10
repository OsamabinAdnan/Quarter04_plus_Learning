# Import required libraries
import os  # For environment variables
from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel  # Core agent components
from agents.run import RunConfig  # Configuration for the agent runner
import asyncio  # For asynchronous operations
from dotenv import load_dotenv  # For loading environment variables from .env file

# Load environment variables from .env file
load_dotenv()

# Get the Gemini API key from environment variables
gemini_api_key = os.getenv("GEMINI_API_KEY")

if not gemini_api_key:
    raise ValueError("Error: GEMINI_API_KEY environment variable not set")

# Reference: https://ai.google.dev/gemini-api/docs/openai

# Initialize AsyncOpenAI client with Gemini API configuration
external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",  # Gemini API endpoint
)

# Set up the chat completions model using Gemini's model
model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",  # Specify Gemini model version
    openai_client=external_client,  # Use our configured client
)

# Configure the runner settings
config = RunConfig(
    model=model,  # Use our configured model
    model_provider=external_client,  # Specify the model provider
    tracing_disabled=True,  # Disable tracing for simpler execution
)

async def main():
    # Create an AI agent with basic configuration
    agent = Agent(
        name="Assistant",  # Name of our AI agent
        instructions="You are a helpful agent",  # Basic instruction set
        model=model,  # Use our configured model
    )

    result = await Runner.run (agent,"Tell me about recursion in programming.", run_config=config)

    print("=" * 40)
    print("Asnyc Hello Agent")
    print("=" * 40)
    print(result.final_output)
    print("=" * 40)

    # Function calls itself,
    # Looping in smaller pieces,
    # Endless by design.

# Entry point of the program
if __name__ == "__main__":
    asyncio.run(main())  # Run the async main function