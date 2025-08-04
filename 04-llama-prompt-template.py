# Example: Using LangChain PromptTemplate with Groq
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
# Load environment variables (e.g., GROQ_API_KEY) from .env
load_dotenv()

# Initialize the Groq LLM
llm = ChatGroq(model="llama3-8b-8192")

# Define a prompt template for an invitation email
email_template = PromptTemplate.from_template(
    "Create an invitation email to the recipient that is {recipient_name}\n"
    "for an event that is {event_type}\n"
    "in a language that is {language}\n"
    "Mention the event location that is {event_location}\n"
    "and event date that is {event_date}.\n"
    "Also write few sentences about the event description that is {event_description}\n"
    "in style that is {style}."
)

# Specify details for the template
# These will be substituted into the placeholders in the prompt



details = {
    "recipient_name": "John",
    "event_type": "product launch",
    "language": "American english",
    "event_location": "Grand Ballroom, City Center Hotel",
    "event_date": "11 AM, January 15, 2024",
    "event_description": "an exciting unveiling of our latest GenAI product",
    "style": "enthusiastic tone"
}

# Render the prompt with the details
prompt_value = email_template.invoke(details)

# Get the LLM's response
response = llm.invoke(prompt_value)
print("Generated invitation email:\n")
print(response.content)