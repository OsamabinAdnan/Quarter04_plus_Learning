"""
server.py - FastMCP Weather Server
=====================================

This is our MCP server.
It has two tools that Agent will use to get weather information.

main.py starts this server automatically using MCPServerStdio, so you don't need to run this file separately.
"""
from fastmcp import FastMCP

# Create the server

mcp = FastMCP("Weather MCP Server")

# Tool 1: Get a weather of a city

@mcp.tool
def get_weather(city:str) -> str:
    """Return the weather of the city"""
    data = {
        "New York": "Sunny, 25°C",
        "London": "Cloudy, 18°C",
        "Paris": "Rainy, 20°C",
        "Tokyo": "Sunny, 30°C",
    }
    result = data.get(city.lower())
    if result:
        return f"The weather in {city} is {result}"
    return f"Sorry, I don't have weather information for {city}"

# Tool 2: List available cities
@mcp.tool
def list_cities() -> list[str]:
    """Return a list of available cities"""
    return "Available cities: New York, London, Paris, Tokyo"

if __name__ == "__main__":
    mcp.run(transport="stdio")