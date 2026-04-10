from dotenv import load_dotenv
import os
from pprint import pprint
from agents import enable_verbose_stdout_logging
from rich import print
from openai import OpenAI
import asyncio

load_dotenv()

enable_verbose_stdout_logging()

gemini_api_key = os.getenv("GEMINI_API_KEY")
if not gemini_api_key:
    raise ValueError("GEMINI_API_KEY environment variable not set")


client = OpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)
async def main():
    print("🧠 Asking Gemini a question...\n")

    response = client.chat.completions.create(
        model="gemini-2.5-flash",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user",   "content": "Explain how AI works in simple terms."}
        ],
    )

    print("💡 Raw Gemini Response:\n")
    print(response)
    message = response.choices[0].message.content
    print(f"💡 Gemini's Response:\n")
    pprint(message)

if __name__ == "__main__":
    asyncio.run(main())