# Example: LangGraph routing/system example with tool calls (requires OPENAI_API_KEY)
# This script demonstrates how to use LangGraph to build a graph with conditional routing and tool calling.
# It requires an OpenAI API key (set OPENAI_API_KEY in your environment or .env file).

from langgraph.graph import MessagesState, StateGraph, START, END
from langchain_openai import ChatOpenAI
from langgraph.prebuilt import ToolNode, tools_condition
from langchain_core.messages import HumanMessage
from dotenv import load_dotenv

# --- Step 1: Load environment variables ---
# Loads your OpenAI API key from a .env file if present
load_dotenv()

# --- Step 2: Define a custom MessagesState (optional for clarity) ---
class MyMessagesState(MessagesState):
    pass

# --- Step 3: Initialize the LLM ---
llm = ChatOpenAI(model="gpt-4o")

# --- Step 4: Define a Python function as a tool ---
def multiply(a: int, b: int) -> int:
    """Multiplies two integers."""
    return a * b

# Bind the tool to the LLM (not strictly needed for ToolNode, but shown for clarity)
llm_with_tools = llm.bind_tools([multiply])

# --- Step 5: Define the LLM node logic ---
def tool_calling_llm(state: MyMessagesState):
    # The LLM will decide whether to use the tool based on the message
    response = llm.invoke(state["messages"])
    return {"messages": [response]}

# --- Step 6: Build the LangGraph state graph ---
builder = StateGraph(MessagesState)
builder.add_node("tool_calling_llm", tool_calling_llm)

# ToolNode automatically handles executing any tool calls made by the LLM
builder.add_node("tools", ToolNode([multiply]))

# Connect the start to our LLM node
builder.add_edge(START, "tool_calling_llm")

# Add a conditional edge that uses 'tools_condition'
# If the LLM’s response indicates a tool call, it routes to "tools"
# Otherwise, it routes to END
builder.add_conditional_edges("tool_calling_llm", tools_condition)

builder.add_edge("tools", END)
graph = builder.compile()

# --- Step 7: Run the graph with different user inputs ---
print("\n--- LLM with tool call: 'Multiply 3 and 2' ---")
messages = [HumanMessage(content="Multiply 3 and 2")]
result = graph.invoke({"messages": messages})
for m in result['messages']:
    m.pretty_print()

print("\n--- LLM with non-tool message: 'Hello world.' ---")
messages = [HumanMessage(content="Hello world.")]
result = graph.invoke({"messages": messages})
for m in result['messages']:
    m.pretty_print()