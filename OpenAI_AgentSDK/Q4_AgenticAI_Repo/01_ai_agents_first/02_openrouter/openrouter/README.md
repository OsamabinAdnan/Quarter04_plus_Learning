# OpenRouter API Integration Example

This project demonstrates how to integrate with OpenRouter's API to access various AI models, including DeepSeek's chat model. The implementation uses Python and the OpenAI client library with a custom base URL to connect to OpenRouter's services.

## Prerequisites

- Python 3.x
- OpenRouter API key (set in environment variables)
- Required Python packages:
  - `python-dotenv`
  - `openai`

## Setup

1. Create a `.env` file in the project root and add your OpenRouter API key:
   ```
   OPENROUTER_API_KEY=your_api_key_here
   ```

2. Install the required packages:
   ```bash
   pip install python-dotenv openai
   ```

## Usage

Run the script using Python:
```bash
uv run main.py
```

The script will:
1. Load your API key from environment variables
2. Initialize the OpenAI client with OpenRouter's base URL
3. Prompt you for input
4. Send your input to the AI model
5. Display the response along with usage statistics

## Sample Output

Here's an example interaction with the AI:

```
Enter your question: What is Agentic AI?

OpenRouter Response:
========================================
**Agentic AI** is a term used to describe artificial intelligence systems that exhibit **goal-directed, autonomous behavior**, often with the ability to make decisions, take actions, and adapt to changing environments without constant human oversight. Unlike traditional AI models that passively respond to inputs, agentic AI systems act more like **autonomous agents**—planning, reasoning, and executing tasks dynamically.

### **Key Characteristics of Agentic AI:**
1. **Autonomy** – Operates independently, making decisions without real-time human intervention.
2. **Goal-Oriented** – Works toward achieving specific objectives (e.g., solving problems, optimizing outcomes).
3. **Adaptive Learning** – Improves performance over time by learning from experience.
4. **Multi-Step Reasoning** – Can break complex tasks into smaller steps and execute them logically.
5. **Environment Interaction** – Perceives and interacts with digital (or physical) environments (e.g., APIs, robotics).
6. **Memory &
========================================
Model used: deepseek/deepseek-chat-v3-0324:free
Total tokens used: 209
```

### Response Object Details

The complete response object from OpenRouter includes:
```python
ChatCompletion(
    id='gen-1750319360-JWry4gZPJ5eIBwdURAnb',
    choices=[
        Choice(
            finish_reason='length',
            index=0,
            logprobs=None,
            message=ChatCompletionMessage(
                content='[message content]',
                role='assistant'
            )
        )
    ],
    created=1750319361,
    model='deepseek/deepseek-chat-v3-0324:free',
    object='chat.completion',
    usage=CompletionUsage(
        completion_tokens=200,
        prompt_tokens=9,
        total_tokens=209
    ),
    provider='Targon'
)
```

## Configuration Options

The script uses the following configuration for API calls:
- Model: `deepseek/deepseek-chat-v3-0324:free`
- Max tokens: 200
- Temperature: 0.8 (controls response randomness)

## Error Handling

The script includes basic error handling:
- Checks for missing API key
- Properly formats and displays API responses
- Includes clear separation of response sections for readability
