from mcp.server.fastmcp import FastMCP

mcp=FastMCP('weather')

@mcp.tool()
def get_weather(location:str):
    """
    get the weather of a location
    """
    return "the weather of a location"

if __name__=="__main__":
    mcp.run(transport="streamable-http")
    
