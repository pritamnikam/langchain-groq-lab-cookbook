from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field

# Import dotenv to load environment variables from a .env file
from dotenv import load_dotenv
# Load environment variables (e.g., GROQ_API_KEY) from .env
load_dotenv()

llm = ChatGroq(model="llama3-8b-8192")

class Author(BaseModel):
    # The name of the author
    name: str = Field(description="The name of the author")
    # The number of books written by the author
    number: int = Field(description="The number of books written by the author")
    # The list of books they wrote
    books: list[str] = Field(description="The list of books they wrote")

# Create a Pydantic output parser for the Author model
output_parser = PydanticOutputParser(pydantic_object=Author)

# Create a prompt template for a structured output, using the parser's format instructions
prompt_list = PromptTemplate.from_template(
    # Template for the prompt, with placeholders for format instructions and question
    template = "Answer the question.\n{format_instructions}\n{question}",
    # Input variables for the prompt template
    input_variables = ["question"],
    # Partial variables for the prompt template, including format instructions
    partial_variables = {"format_instructions": output_parser.get_format_instructions()},
)

# Invoke the prompt template with a specific question
prompt_value = prompt_list.invoke({"question": "Generate the books written by Dan Brown"})

# Get the response from the LLaMA model
response = llm.invoke(prompt_value)

# Parse the response using the Pydantic output parser
returned_object = output_parser.parse(response.content)

# Print the author's information
print(f"Author: {returned_object.name}")
print(f"Number of books: {returned_object.number}")
print("Books:")
for book in returned_object.books:
    print(book)
print(f"{returned_object.name} wrote {returned_object.number} books.")
print(returned_object.books)