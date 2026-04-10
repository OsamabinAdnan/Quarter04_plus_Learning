"""
OpenRouter API Integration Example
This script demonstrates how to use OpenRouter's API to access various AI models,
specifically using the DeepSeek chat model. It uses the OpenAI client library
with a custom base URL to connect to OpenRouter's services.

Author: [Osama bin Adnan]
Date: June 19, 2025
"""

import os
from dotenv import load_dotenv  # For loading environment variables from .env file
from openai import OpenAI  # Using OpenAI's client library with custom base URL

load_dotenv()

def main():
    # Get OpenRouter API key from environment variables
    openrouter_api_key = os.getenv("OPENROUTER_API_KEY")

    # Check if API key is present
    if not openrouter_api_key:
        print("Error: OpenRouter API key not found in environment variables.")
        return
    
    # Initialize OpenAI client with OpenRouter's base URL
    client = OpenAI(
        api_key=openrouter_api_key,
        base_url="https://openrouter.ai/api/v1" # OpenRouter API endpoint
    )

    # Get user input for the conversation
    user_input = input("Enter your question:")

    # Make an API call to OpenRouter
    response = client.chat.completions.create(
        model="deepseek/deepseek-chat-v3-0324:free",  # Using DeepSeek's free model
        messages=[
            {
                "role":"user",
                "content":user_input
            }
        ],
        max_tokens=200, # Maximum number of tokens in the response
        temperature=0.8 # Temperature controls the randomness of the response
    )

    # Print the response in a formatted way
    print("OpenRouter Response:")
    print("=" * 40)
    print(response.choices[0].message.content)
    print("=" * 40)
    print(f"Model used: {response.model}")
    print(f"Total tokens used: {response.usage.total_tokens}")

    print("*" * 40)
    print(f"Response {response}")

if __name__ == "__main__":
    main()