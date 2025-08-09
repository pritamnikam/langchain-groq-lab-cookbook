# Example: LangGraph + LLM tool calling demo (requires OPENAI_API_KEY)
# This script demonstrates how to use LangGraph with an OpenAI LLM and a Python tool.
# It requires an OpenAI API key (set OPENAI_API_KEY in your environment or .env file).

from langgraph.graph import MessagesState, StateGraph, START, END
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage
from dotenv import load_dotenv

# --- Step 1: Load environment variables ---
# This loads your OpenAI API key from a .env file if present
load_dotenv()

# --- Step 2: Define a custom state for the graph ---
class MyMessagesState(MessagesState):
    # Inherits from MessagesState, which manages message history
    pass

# --- Step 3: Initialize the LLM ---
# Replace 'gpt-4o' with your preferred OpenAI model if needed
llm = ChatOpenAI(model="gpt-4o")

# --- Step 4: Define a Python function as a tool ---
def multiply(a: int, b: int) -> int:
    """Multiplies two integers."""
    return a * b

# Bind the tool to the LLM
llm_with_tools = llm.bind_tools([multiply])

# --- Step 5: Define the node logic for tool calling ---
def tool_calling_llm(state: MyMessagesState):
    # The LLM will decide whether to use the tool based on the message
    response = llm_with_tools.invoke(state["messages"])
    return {"messages": [response]}

# --- Step 6: Build the LangGraph state graph ---
builder = StateGraph(MyMessagesState)
builder.add_node("tool_calling_llm", tool_calling_llm)
builder.add_edge(START, "tool_calling_llm")
builder.add_edge("tool_calling_llm", END)
graph = builder.compile()

# --- Step 7: Run the graph with different user inputs ---
print("\n--- LLM with tool, user says 'Hello!' ---")
messages = graph.invoke({"messages": HumanMessage(content="Hello!")})
for m in messages['messages']:
    print(m)

print("\n--- LLM with tool, user says 'Multiply 2 and 3' ---")
messages = graph.invoke({"messages": HumanMessage(content="Multiply 2 and 3")})
for m in messages['messages']:
    print(m)