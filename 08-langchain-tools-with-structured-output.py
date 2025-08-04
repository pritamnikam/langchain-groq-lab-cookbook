# Import necessary libraries
from langchain_groq import ChatGroq
from pydantic import BaseModel, Field

# Import dotenv to load environment variables from a .env file
from dotenv import load_dotenv

# Load environment variables (e.g., GROQ_API_KEY) from .env
load_dotenv()

# Initialize the Groq LLM with the specified model
llm = ChatGroq(model="llama3-8b-8192")

# Define a Pydantic model for the structured output
class Author(BaseModel):
    # The name of the author
    name: str = Field(description="The name of the author")
    # The number of books written by the author
    number: int = Field(description="The number of books written by the author")
    # The list of books they wrote
    books: list[str] = Field(description="The list of books they wrote")

# Create a structured LLM that will return output as an Author model
structured_llm = llm.with_structured_output(Author)

# Invoke the structured LLM with a question
returned_object = structured_llm.invoke("Generate the books written by Dan Brown")

# Print the structured output
print(f"Author: {returned_object.name}")
print(f"Number of books: {returned_object.number}")
print("Books:")
# Iterate over the list of books and print each one
for book in returned_object.books:
    print(f"- {book}")
# Print a summary statement
print(f"{returned_object.name} wrote {returned_object.number} books.")