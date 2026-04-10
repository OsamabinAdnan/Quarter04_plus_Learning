from agents import (
    Agent,
    OpenAIChatCompletionsModel,
    Runner,
    function_tool,
    StopAtTools,
    AsyncOpenAI,
    set_tracing_disabled,
)
from dotenv import find_dotenv, load_dotenv
import asyncio
import os

load_dotenv()

# enable_verbose_stdout_logging()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY environment variable not set")

BASE_URL = os.getenv("BASE_URL")
if not BASE_URL:
    raise ValueError("BASE_URL environment variable not set")

# 1. Which LLM Service?
external_client: AsyncOpenAI = AsyncOpenAI(
    api_key=GEMINI_API_KEY,
    base_url=BASE_URL,
)

# 2. Which LLM Model?
llm_model: OpenAIChatCompletionsModel = OpenAIChatCompletionsModel(
    model="gemini-2.5-flash",
    openai_client=external_client
)

@function_tool
def get_user_data(user_id: str) -> str:
    """Looks up user data."""
    return f"Data for {user_id}: Name - Alex, Role - user"


# TODO 1: Make this an admin-only tool using `is_enabled`.
@function_tool
def delete_user(user_id: str) -> str:
    """Deletes a user. This is a final action."""
    return f"User {user_id} has been deleted."


admin_agent = Agent(
    name="Admin Agent",
    instructions="Help manage users. First get data, then delete if asked.",
    tools=[get_user_data, delete_user],
    model=llm_model,
    # TODO 2: Make the agent stop immediately after a user is deleted
    # using `tool_use_behavior` and `StopAtTools`.
    tool_use_behavior=StopAtTools(stop_at_tool_names=["delete_user"]),
)


async def main():
    print("--- Running as a regular user ---")
    result_user = await Runner.run(
        admin_agent, "Please delete user client_456.", context={"role": "user"}
    )
    print(f"Final Output: {result_user.final_output}")

    print("\n--- Running as an admin ---")
    # TODO 3: Set max_turns to 3 for this run as a safety limit.
    result_admin = await Runner.run(
        admin_agent,
        "Get data for user_123 and then delete them.",
        context={"role": "admin"},
        max_turns=3,
    )
    print(f"Final Output: {result_admin.final_output}")


asyncio.run(main())