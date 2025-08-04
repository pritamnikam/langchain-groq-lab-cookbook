# Import the ChatGroq class from langchain_groq
from langchain_groq import ChatGroq
# Import dotenv to load environment variables from a .env file
from dotenv import load_dotenv
# Load environment variables (e.g., GROQ_API_KEY) from .env
load_dotenv()

# Initialize the Groq LLM with the desired model
llm = ChatGroq(model="llama-3.3-70b-versatile")

# Define the conversation context for the assistant
messages = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Hi, my name is Alex."}
]

# Invoke the model with the messages and get a response
response = llm.invoke(messages)

# Print the assistant's reply
print(response.content)