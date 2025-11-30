# **OpenRouter**

OpenRouter is a platform that offers a unified interface to access a wide range of Large Language Models (LLMs) from various providers, including commercial options like OpenAI, Google, Anthropic, and Meta, as well as open-source models like Mistral and LLaMA. 

It simplifies LLM usage by providing a single API endpoint, enabling developers to switch between models without extensive code changes and optimizing requests based on factors like cost, performance, and availability.

## **Key Features and Functionality**

* **Unified Interface:** OpenRouter aggregates over 200 models into a single access point, streamlining the development process.

* **User Interface:** It provides a chatroom (available at https://openrouter.ai/chat) for interacting with multiple LLMs simultaneously and tools for account management, including monitoring token usage and costs.

* **API Compatibility:** OpenRouter's API is designed to be compatible with the OpenAI Chat Completion API, mirroring its structure and parameters. This allows developers to integrate OpenRouter by simply updating the API key and base URL to https://openrouter.ai/api/v1.

* **Function Calling (Tool Calling):** The platform supports function calling, enabling LLMs to suggest the use of external tools based on user input. This feature is standardized across compatible models and providers, aligning with OpenAI's tool-calling interface.

* **Proxy Model:** OpenRouter acts as a proxy, routing API requests to models hosted by third-party providers rather than hosting the models itself. It handles API translations, authentications, and response formatting, offering access to numerous models without the associated infrastructure costs.

* **Pricing:** It operates on a pay-per-use basis for tokens, with some models available for free.

## **Free Models and Rate Limits**

OpenRouter provides access to various free LLMs, which typically have specific usage limitations.

* **Number of Free Models:** As of June, 2025, OpenRouter offers 64 free models, including 2 models with context windows of 1 million tokens or more.

* **OpenRouter Free Model Limits:** Free model variants (those with an ID ending in :free) are generally limited to 20 requests per minute (RPM) and 200 requests per day (RPD) across all free models.

* **Google Gemini Free Tier Limits:** For development and testing, Google Gemini 2.0 Flash and Flash-Lite models (compatible with OpenAI Chat Completion API via OpenRouter) offer higher limits: 1,500 requests per day (RPD), 15 RPM for Flash, and 30 RPM for Flash-Lite. Both models also have a cap of 1,000,000 tokens per minute (TPM).

## **Common Errors and Solutions**

* **404 Error - No endpoints found matching:** This error often occurs when OpenRouter's API cannot find endpoints matching your data policy, typically due to disabled prompt training. To resolve this, visit the OpenRouter Privacy Settings and enable the "Prompt Training" option, then re-run your code.

For more details, you can refer to the following resources:

* [OpenRouter Official Website](https://openrouter.ai/)
* [OpenRouter Quickstart Guide](https://openrouter.ai/docs/quickstart)
* [OpenRouter Tool Calling Documentation](https://openrouter.ai/docs/features/tool-calling)
* [API Rate Limits - OpenRouter](https://openrouter.ai/docs/api-reference/limits)
* [Connecting to OpenRouter from Python (Medium article)](https://medium.com/%40tedisaacs/from-openai-to-opensource-in-2-lines-of-code-b4b8d2cf2541)
* [OpenRouter AI Agents SDK (Code Example)](https://colab.research.google.com/drive/1LOEOBP52WJpmMWsOS7-SUDQBLtmXZ_1d?usp=sharing)