# Example: Using LangChain with Groq to chat with an LLM
from langchain_groq import ChatGroq
# Import dotenv to load environment variables from a .env file
from dotenv import load_dotenv
# Load environment variables (e.g., GROQ_API_KEY) from .env
load_dotenv()

# Initialize the Groq LLM with the desired model
llm = ChatGroq(model="llama3-8b-8192")

# Send a simple prompt and print the response
response = llm.invoke("What is the tallest building in the world?")
print("Invoke response:")
print(response.content)

# We can use the stream method instead of the invoke method to stream the message. 
# This will return a generator object. We must process the output with a simple loop to print it.
# Stream the response for the same prompt
print("\nStreamed response:")
response = llm.stream("What is the tallest building in the world?")
for chunk in response:
  print(chunk.content, end="")
print()