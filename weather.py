from mcp.server.fastmcp import FastMCP
mcp = FastMCP("Weather")

@mcp.tool()
def get_weather(location: str) -> str:
    """
    Get the current weather for a given location.

    Args:
        location (str): The name of the location to get the weather for.

    Returns:
        str: A string describing the current weather conditions.
    """
    # This is a placeholder implementation. Replace with actual weather fetching logic.
    return f'The weather is hot and dry in {location}.'

if __name__ == "__main__":
    mcp.run()
    print("Weather service is running.")
    print("Use the 'get_weather' tool to fetch weather information.")
