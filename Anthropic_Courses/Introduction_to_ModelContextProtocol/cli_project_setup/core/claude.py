from openai import OpenAI
import os


class Claude:
    def __init__(self, model: str):
        # Initialize OpenAI client pointing to 9router local proxy
        self.client = OpenAI(
            base_url=os.getenv("OPENAI_BASE_URL", "http://localhost:20128/v1"),
            api_key=os.getenv("OPENAI_API_KEY", "dummy-key"),  # Local proxy may not need real key
        )
        self.model = model

    def add_user_message(self, messages: list, message):
        """Add a user message to the conversation history"""
        # Handle both string and message object inputs
        if isinstance(message, dict):
            content = message.get("content", "")
        elif hasattr(message, "content"):
            # Handle OpenAI message objects
            content = message.content
        else:
            content = str(message)

        user_message = {
            "role": "user",
            "content": content,
        }
        messages.append(user_message)

    def add_assistant_message(self, messages: list, message):
        """Add an assistant message to the conversation history"""
        # Handle both string and message object inputs
        if isinstance(message, dict):
            content = message.get("content", "")
        elif hasattr(message, "content"):
            # Handle OpenAI message objects
            content = message.content
        else:
            content = str(message)

        assistant_message = {
            "role": "assistant",
            "content": content,
        }
        messages.append(assistant_message)

    def text_from_message(self, message):
        """Extract text content from a message object"""
        if isinstance(message, dict):
            return message.get("content", "")
        elif hasattr(message, "choices"):
            # OpenAI ChatCompletion object
            return message.choices[0].message.content or ""
        elif hasattr(message, "content"):
            return message.content or ""
        return str(message)

    def chat(
        self,
        messages,
        system=None,
        temperature=1.0,
        stop_sequences=[],
        tools=None,
        thinking=False,
        thinking_budget=1024,
    ):
        """Send a chat request to the LLM via 9router proxy"""
        # Build the messages list
        chat_messages = []

        # Add system message if provided
        if system:
            chat_messages.append({
                "role": "system",
                "content": system,
            })

        # Add conversation messages
        chat_messages.extend(messages)

        # Build request parameters
        params = {
            "model": self.model,
            "messages": chat_messages,
            "temperature": temperature,
            "max_tokens": 8000,
        }

        # Add stop sequences if provided
        if stop_sequences:
            params["stop"] = stop_sequences

        # Add tools if provided (OpenAI format)
        if tools:
            params["tools"] = tools

        # Note: OpenAI doesn't have a direct "thinking" mode equivalent
        # If thinking is enabled, we could add a system message or handle differently
        if thinking:
            # Add a note in system message to encourage reasoning
            thinking_prompt = "\n\nPlease think through your response step by step before answering."
            if system:
                params["messages"][0]["content"] += thinking_prompt
            else:
                params["messages"].insert(0, {
                    "role": "system",
                    "content": thinking_prompt,
                })

        # Make the API call
        response = self.client.chat.completions.create(**params)
        return response
