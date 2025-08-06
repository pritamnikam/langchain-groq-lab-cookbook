# Example: Sentiment classification using LangChain, Groq, and chains
from langchain_core.runnables import RunnableLambda
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

# Load environment variables (e.g., GROQ_API_KEY) from .env
load_dotenv()

# Initialize the Groq LLM
llm = ChatGroq(model="llama-3.1-8b-instant")

# Define a prompt template for sentiment analysis
sentiment_template = PromptTemplate(
    input_variables=["feedback"],
    template="Determine the sentiment of this feedback and reply in one word as either 'Positive', 'Neutral', or 'Negative':\n\n{feedback}"
)

# Example feedbacks (uncomment one at a time to test different sentiments)
# Neutral example
user_feedback = "The delivery was late, and the product was damaged when it arrived. However, the customer support team was very helpful in resolving the issue quickly."
# Positive example
# user_feedback = "The customer service was fantastic. The representative was friendly, knowledgeable, and resolved my issue quickly."
# Negative example
# user_feedback = "I was extremely disappointed with the customer service. The representative was unhelpful and rude."

# Build the chain: prompt -> LLM -> output parser
chain = sentiment_template | llm | StrOutputParser()

# Invoke the chain with the feedback and get the sentiment
feedback_sentiment = chain.invoke({"feedback": user_feedback})

# Print the sentiment result
print("Feedback sentiment:", feedback_sentiment)


# --- Advanced Multi-Step Sentiment Chain ---
# This section demonstrates a more complex LangChain pipeline:
# 1. Parse and clean raw feedback for key information
# 2. Summarize the parsed feedback
# 3. Analyze the summary for sentiment
# Each step is chained using RunnableLambda for variable formatting between steps.

# Step 1: Parse and clean the raw feedback
parse_template = PromptTemplate(
    input_variables=["raw_feedback"],
    template="Parse and clean the following customer feedback for key information:\n\n{raw_feedback}"
)

# Step 2: Summarize the parsed feedback
summary_template = PromptTemplate(
    input_variables=["parsed_feedback"],
    template="Summarize this customer feedback in one concise sentence:\n\n{parsed_feedback}"
)

# Helper: Format output from parsing to match summary input
format_parsed_output = RunnableLambda(
    lambda output: {"parsed_feedback": output}
)

# Helper: Format output from summary to match sentiment input
format_summary_output = RunnableLambda(
    lambda output: {"feedback": output}
)

# Build the full chain: parse -> summarize -> sentiment
advanced_chain = (
    parse_template
    | llm
    | format_parsed_output
    | summary_template
    | llm
    | format_summary_output
    | sentiment_template
    | llm
    | StrOutputParser()
)

# Run the advanced chain
advanced_sentiment = advanced_chain.invoke({"raw_feedback": user_feedback})

# Print the final sentiment result from the advanced chain
print("Advanced chain sentiment result:", advanced_sentiment)



# --- Dynamic Response Routing Section ---
# This section demonstrates how to generate a tailored response based on the classified sentiment.
# It uses three prompt templates and chains:
# - Thank you message for positive sentiment
# - Request for more details for neutral sentiment
# - Apology and escalation for negative sentiment
# Routing is performed dynamically using a custom function and RunnableLambda.

# Thank you message template and chain (for positive sentiment)
thankyou_template = PromptTemplate(
    input_variables=["feedback"],
    template="Given the feedback, draft a thank you message for the user and request them to leave a positive rating on our webpage:\n\n{feedback}"
)
thankyou_chain = thankyou_template | llm | StrOutputParser()

# Request more details template and chain (for neutral sentiment)
details_template = PromptTemplate(
    input_variables=["feedback"],
    template="Given the feedback, draft a message for the user and request them provide more details about their concern:\n\n{feedback}"
)
details_chain = details_template | llm | StrOutputParser()

# Apology and escalation template and chain (for negative sentiment)
apology_template = PromptTemplate(
    input_variables=["feedback"],
    template="Given the feedback, draft an apology message for the user and mention that their concern has been forwarded to the relevant department:\n\n{feedback}"
)
apology_chain = apology_template | llm | StrOutputParser()

# Routing function: selects the appropriate chain based on sentiment
# (Note: fixed typo 'postive' -> 'positive')
def route(info):
    if "positive" in info['sentiment'].lower():
        return thankyou_chain
    elif "negative" in info['sentiment'].lower():
        return apology_chain
    else:
        return details_chain

# Example feedbacks (uncomment one at a time to test different sentiments)
# Neutral
# user_feedback = "The delivery was late, and the product was damaged when it arrived. However, the customer support team was very helpful in resolving the issue quickly."

# Positive
user_feedback = "The customer service was fantastic. The representative was friendly, knowledgeable, and resolved my issue quickly."

# Negative
# user_feedback = "I was extremely disappointed with the customer service. The representative was unhelpful and rude."

# Helper: Format output from parsing to match summary input
format_parsed_output = RunnableLambda(lambda output: {"parsed_feedback": output})

# Chain for summarizing feedback
summary_chain = (
    parse_template 
    | llm 
    | format_parsed_output 
    | summary_template 
    | llm 
    | StrOutputParser()
)

# Chain for classifying sentiment
sentiment_chain = (
    sentiment_template 
    | llm 
    | StrOutputParser()
)

# Generate summary and sentiment
summary = summary_chain.invoke({'raw_feedback': user_feedback})
sentiment = sentiment_chain.invoke({'feedback': summary})

# Print labeled outputs
print("The summary of the user's message is:", summary)
print("The sentiment was classified as:", sentiment)

# Compose a dictionary with feedback and sentiment for routing
# RunnableLambda(route) dynamically selects the correct response chain
full_chain = (
    {
        "feedback": lambda x: x['feedback'], 
        'sentiment': lambda x: x['sentiment']
    } 
    | RunnableLambda(route)
)

# Generate and print the tailored response
response_message = full_chain.invoke({'feedback': summary, 'sentiment': sentiment})
print("Tailored response message:\n", response_message)