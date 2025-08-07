# Example: Tool calling with LangChain, Groq, and Python function tools
from langchain_groq import ChatGroq
from langchain_core.tools import tool
from dotenv import load_dotenv

# Load environment variables (e.g., GROQ_API_KEY) from .env
load_dotenv()

# Initialize the Groq LLM
llm = ChatGroq(model="llama-3.1-8b-instant")

# Define a Python function as a LangChain tool
@tool
def calculate_discount(price: float, discount_percentage: float) -> float:
    """
    Calculates the final price after applying a discount.

    Args:
        price (float): The original price of the item.
        discount_percentage (float): The discount percentage (e.g., 20 for 20%).

    Returns:
        float: The final price after the discount is applied.
    """
    if not (0 <= discount_percentage <= 100):
        raise ValueError("Discount percentage must be between 0 and 100")
    discount_amount = price * (discount_percentage / 100)
    final_price = price - discount_amount
    return final_price

# Bind the tool to the LLM so it can be called via natural language
llm_with_tools = llm.bind_tools([calculate_discount])

# Example 1: LLM invocation with no tool call
hello_world = llm_with_tools.invoke("Hello world!")
print("LLM content (no tool call):", hello_world.content, '\n')

# Example 2: LLM invocation that triggers the tool call
result = llm_with_tools.invoke("What is the price of an item that costs $100 after a 20% discount?")
print("LLM content (with tool call):", result.content, '\n')
print("Tool calls made:", result.tool_calls, '\n')

# Extract the arguments from the tool call and invoke the tool directly
args = result.tool_calls[0]['args']
print("Tool call arguments:", args, '\n')
print("Tool call result (direct Python call):", calculate_discount.invoke(args), '\n')
