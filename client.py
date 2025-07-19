from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain_groq import ChatGroq
from langgraph.prebuilt import create_react_agent
import asyncio
from dotenv import load_dotenv
import os

load_dotenv()

async def main():
    client = MultiServerMCPClient(
        {
            "math": {
                "command": "python",
                "args": ["mathserver.py"],
                "transport": "stdio",
            },
            "weather": {
                "url": "http://localhost:8000/mcp",
                "transport": "streamable_http",
            }
        }
    )

    os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY") or ""

    tools = await client.get_tools()
    print("🛠 Tools loaded:", [t.name for t in tools])

    model = ChatGroq(model="llama3-8b-8192")
    agent = create_react_agent(model=model, tools=tools)

    try:
        math_response = await agent.ainvoke({
            "messages": [
                {"role": "user", "content": "What is 2+2?"}
            ]
        })
        print("📦 math_response:", math_response["messages"][-1].content)
    except Exception as e:
        print("❌ Error invoking agent:", str(e))

asyncio.run(main())
