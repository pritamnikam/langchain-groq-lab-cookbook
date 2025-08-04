# Example: Using LangChain message roles and types with Groq
#
# LangChain supports four roles:
# - system: Provides instructions or constraints to the model, guiding its behavior.
# - user: Represents the user’s input.
# - assistant: Represents the model’s response.
# - tool: Use to pass information back to the model after a tool has been invoked.
#
# Message types for each role:
# - SystemMessage: for system role
# - HumanMessage: for user role
# - AIMessage: for assistant role
# - AIMessageChunk: for streaming assistant
# - ToolMessage: for tool role

from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, SystemMessage
from dotenv import load_dotenv
# Load environment variables (e.g., GROQ_API_KEY) from .env
load_dotenv()

# Initialize the Groq LLM
llm = ChatGroq(model="llama3-8b-8192")

# Compose a conversation using message objects
messages = [
    SystemMessage(content="You are a math tutor who provides answers with a bit of sarcasm."),
    HumanMessage(content="What is the square of 2?")
]

# Get the AI's response
response = llm.invoke(messages)
print("Assistant response:")
print(response.content)
print("Type of response:", type(response))