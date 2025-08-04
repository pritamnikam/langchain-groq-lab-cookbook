from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain.output_parsers import DatetimeOutputParser

# Import dotenv to load environment variables from a .env file
from dotenv import load_dotenv

# Load environment variables (e.g., GROQ_API_KEY) from .env
load_dotenv()

# Initialize the LLaMA model for the chat
llm = ChatGroq(model="llama3-8b-8192")

# Create a parser for date/time output
parser_dateTime = DatetimeOutputParser()

# Create a prompt template for a date/time question, using the parser's format instructions
prompt_dateTime = PromptTemplate.from_template(
    template = "Answer the question.\n{format_instructions}\n{question}",
    input_variables = ["question"],  # Fix typo: 'input_vairables' -> 'input_variables'
    partial_variables = {"format_instructions": parser_dateTime.get_format_instructions()}
)

# Invoke the prompt template with a specific question
prompt_value = prompt_dateTime.invoke({"question": "When was the iPhone released"})

# Get the response from the LLaMA model
response = llm.invoke(prompt_value)

# Print the response content
print("Response:")
print(response.content)

# Parse the response content using the date/time parser
returned_object = parser_dateTime.parse(response.content)
print(type(returned_object))
print(returned_object)