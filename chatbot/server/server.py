from mcp.server.fastmcp import FastMCP
import time
import signal
import sys
from app.functions.chat_with_knowledge_base import (
    retriver_query
)
# Handle SIGINT (Ctrl+C) gracefully
def signal_handler(sig, frame):
    print("Shutting down server gracefully...")
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

# Create an MCP server with increased timeout
mcp = FastMCP(
    name="count-r",
    host="127.0.0.1",
    port=5000,
    # Add this to make the server more resilient
    timeout=30  # Increase timeout to 30 seconds
)


# Define our tool
@mcp.tool()
def answer_from_knowledge_base(query: str) -> str:
    """Get information from Knowledge Base for the given query."""
    return retriver_query(query)

if __name__ == "__main__":
    try:
        print("Starting MCP server 'count-r' on 127.0.0.1:5000")
        # Use this approach to keep the server running
        mcp.run()
    except Exception as e:
        print(f"Error: {e}")
        # Sleep before exiting to give time for error logs
        time.sleep(5)
        
        
        
        
        # "answer_from_knowledge_base": {
        #     "command": "E:\\Github\\AI_KnowledgeBase\\chatbot\\server\\.venv\\Scripts\\python.exe",
        #     "args": [
        #         "E:\\Github\\AI_KnowledgeBase\\chatbot\\server\\server.py"
        #     ],
        #     "host": "127.0.0.1",
        #     "port": 5000,
        #     "timeout": 30000
        # },