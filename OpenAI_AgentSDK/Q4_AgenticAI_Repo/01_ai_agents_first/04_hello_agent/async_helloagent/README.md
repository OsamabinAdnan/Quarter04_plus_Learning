# Async Hello Agent

A simple demonstration of an asynchronous AI agent using the Gemini API through OpenAI-compatible endpoints.

## Description

This project implements an asynchronous AI agent that uses Google's Gemini API through OpenAI-compatible endpoints. The agent is capable of processing queries and generating responses using the Gemini language model.

## Features

- Asynchronous operation using Python's `asyncio`
- Integration with Google's Gemini API
- Environment variable-based configuration
- Simple agent-based interaction
- OpenAI-compatible interface

## Prerequisites

- Python 3.7+
- Gemini API key

## Required Environment Variables

- `GEMINI_API_KEY`: Your Google Gemini API key

## Installation

1. Clone the repository
2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

1. Create a `.env` file in the project root and add your Gemini API key:
```
GEMINI_API_KEY=your_api_key_here
```

2. Run the script:
```bash
python main.py
```

## Code Structure

- `main.py`: Contains the main implementation including:
  - API client configuration
  - Model setup
  - Agent initialization
  - Async execution logic

## Example Output

The program will execute a sample query about recursion in programming and display the response in a formatted output.

## Dependencies

- `agents`: For AI agent functionality
- `python-dotenv`: For environment variable management
- `asyncio`: For asynchronous operations

## Notes

- The code uses the OpenAI-compatible endpoint of Gemini API
- Tracing is disabled in the default configuration
- The agent is configured with basic helpful instructions

