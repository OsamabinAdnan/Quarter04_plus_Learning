# Import required libraries
import os
from dotenv import load_dotenv
from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel
from agents.run import RunConfig

# Load environment variables from .env file
load_dotenv()

# Get the Gemini API key from environment variables
gemini_api_key = os.getenv("GEMINI_API_KEY")

# Check if the API key is available
if not gemini_api_key:
    raise ValueError("GEMINI_API_KEY not set")

# Reference: https://ai.google.dev/gemini-api/docs/openai

# Initialize the AsyncOpenAI client with Gemini API configuration
external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

# Set up the chat completions model using Gemini-2.0-flash
model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=external_client
)

# Configure the runner with model settings
config = RunConfig(
    model=model,
    model_provider=external_client,
    tracing_disabled=True  # Disable tracing for simpler output
)

# Create an AI agent with basic instructions
agent: Agent = Agent(
    name="Assistant",
    instructions="You are a helpful assistant",
    model=model
)

# Run the agent synchronously with a test question
result = Runner.run_sync(
    agent,
    "What is Agentic AI?",
    run_config=config,
)

print("\nCALLING AGENT")
print("=" * 50)

print(result.final_output)