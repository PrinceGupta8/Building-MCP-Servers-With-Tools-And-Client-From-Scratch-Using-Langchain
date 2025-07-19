from mcp.server.fastmcp import FastMCP

mcp=FastMCP("Math")

@mcp.tool()
def add(a:int,b:int)-> int:
    """
    Add two number a and b return the output
    """
    return a+b#

@mcp.tool()
def multiply(a:int,b:int)-> str:
    """
    multiply two number a and b return the output
    """
    return a*b

if __name__=="__main__":
    mcp.run(transport='stdio')