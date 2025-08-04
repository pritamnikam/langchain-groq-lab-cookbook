from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain.output_parsers import CommaSeparatedListOutputParser

# Import dotenv to load environment variables from a .env file
from dotenv import load_dotenv

# Load environment variables (e.g., GROQ_API_KEY) from .env
load_dotenv()

# Initialize the Groq model
llm = ChatGroq(model="llama3-8b-8192")

# Create a parser for comma-separated list output
parser_list = CommaSeparatedListOutputParser()

# Create a prompt template for a list output, using the parser's format instructions
prompt_list = PromptTemplate.from_template(
    template = "Answer the question.\n{format_instructions}\n{question}",
    input_variables = ["question"],  # Corrected typo: 'input_vairables' -> 'input_variables'
    partial_variables = {"format_instructions": parser_list.get_format_instructions()},
)

# Invoke the prompt template with a specific question
prompt_value = prompt_list.invoke({"question": "List 4 chocolate brands"})

# Use the Groq model to generate a response to the prompt
response = llm.invoke(prompt_value)

# Print the raw response from the model
print("Raw Response:")
print(response.content)

# Parse the response using the comma-separated list parser
returned_object = parser_list.parse(response.content)
print(type(returned_object))
print(returned_object)  