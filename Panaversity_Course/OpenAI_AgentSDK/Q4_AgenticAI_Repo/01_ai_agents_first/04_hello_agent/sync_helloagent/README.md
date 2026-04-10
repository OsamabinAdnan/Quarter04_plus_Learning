# Sync Hello Agent

A simple demonstration of creating and running an AI agent using the Gemini API with a synchronous execution model.

## Description

This project showcases the implementation of a basic AI agent using Google's Gemini API. The agent is configured to act as a helpful assistant and can respond to user queries in a synchronous manner.

## Features

- Integration with Google's Gemini API
- Synchronous agent execution
- Environment variable configuration
- Simple question-answering capability

## Prerequisites

- Python 3.x
- Gemini API key

## Installation

1. Clone this repository
2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the root directory and add your Gemini API key:
```env
GEMINI_API_KEY=your_api_key_here
```

## Project Structure

```
├── main.py           # Main application file
├── pyproject.toml    # Project configuration
├── README.md         # Project documentation
└── uv.lock          # Dependency lock file
```

## Usage

Run the application using:

```bash
python main.py
```

The program will execute a test query "What is Agentic AI?" and display the agent's response.

## Configuration

The project uses the following configurations:
- Gemini 2.0 Flash model
- Synchronous execution
- Disabled tracing for cleaner output

## Environment Variables

- `GEMINI_API_KEY`: Your Google Gemini API key (required)

## Dependencies

- `python-dotenv`: For environment variable management
- `agents`: For AI agent implementation
- Additional dependencies as specified in `pyproject.toml`

