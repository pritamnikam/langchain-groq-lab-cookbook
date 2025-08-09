# Example: Simple LangGraph state graph demo (no API key required)
# This script demonstrates how to use LangGraph to build a simple state machine with conditional logic.
# It does NOT require any external API keys or cloud services.

from typing_extensions import TypedDict
from typing import Literal
import random
from langgraph.graph import StateGraph, START, END

# Define the state structure for the graph
class State(TypedDict):
    graph_state: str

# Node 1: Appends 'AGI' to the state
def node_1(state):
    print("---Node 1---")
    return {"graph_state": state['graph_state'] + " AGI"}

# Node 2: Appends 'Achieved!' to the state
def node_2(state):
    print("---Node 2---")
    return {"graph_state": state['graph_state'] + " Achieved!"}

# Node 3: Appends 'Not Achieved :(' to the state
def node_3(state):
    print("---Node 3---")
    return {"graph_state": state['graph_state'] + " Not Achieved :("}

# Decision function: randomly chooses between node_2 and node_3
# In a real application, this could use the state to make a meaningful decision
def decide_mood(state) -> Literal["node_2", "node_3"]:
    # Here, we randomly split between Node 2 and Node 3
    if random.random() < 0.5:
        return "node_2"
    return "node_3"

# Build the state graph
builder = StateGraph(State)
builder.add_node("node_1", node_1)
builder.add_node("node_2", node_2)
builder.add_node("node_3", node_3)

# Define the edges and conditional transitions
builder.add_edge(START, "node_1")
builder.add_conditional_edges("node_1", decide_mood)
builder.add_edge("node_2", END)
builder.add_edge("node_3", END)

# Compile the graph
graph = builder.compile()

# Run the graph with different initial states
print("\n--- Running with initial question ---")
result1 = graph.invoke({"graph_state" : "Has AGI been achieved?"})
print("Final state:", result1)

print("\n--- Running with empty initial state ---")
result2 = graph.invoke(State(graph_state=""))
print("Final state:", result2)

