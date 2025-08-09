# Example: Using a vector store with LangChain and OpenAI embeddings
from langchain_core.documents import Document
from uuid import uuid4
from langchain_core.vectorstores import InMemoryVectorStore
from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

# Load environment variables (e.g., OpenAI API key for embeddings) from .env
load_dotenv()

# --- Step 1: Create example documents ---
# Create three example documents with different content and metadata
document_1 = Document(
    page_content="I had chocolate chip pancakes and scrambled eggs for breakfast this morning.",
    metadata={"source": "tweet"},
    id=1,
)
document_2 = Document(
    page_content="The weather forecast for tomorrow is cloudy and overcast, with a high of 62 degrees.",
    metadata={"source": "news"},
    id=2,
)
document_3 = Document(
    page_content="Building an exciting new project with LangChain - come check it out!",
    metadata={"source": "tweet"},
    id=3,
)

# Store the documents in a list for later use
documents = [document_1, document_2, document_3]

# --- Step 2: Set up OpenAI embeddings ---
# NOTE: You must have OPENAI_API_KEY set in your environment or .env file for this to work.
# Initialize OpenAI embeddings with a specific model (text-embedding-3-large)
embeddings = OpenAIEmbeddings(model="text-embedding-3-large")

# --- Step 3: Create an in-memory vector store ---
# Create an in-memory vector store using the OpenAI embeddings
vector_store = InMemoryVectorStore(embeddings)

# --- Step 4: Add documents to the vector store ---
# Generate unique IDs for each document
uuids = [str(uuid4()) for _ in range(len(documents))]
# Add the documents to the vector store with their corresponding IDs
vector_store.add_documents(documents=documents, ids=uuids)

# --- Step 5: Perform similarity search ---
# Define a query to search for similar documents
query = "What's the weather going to be like tomorrow?"
# Perform a similarity search with the query and retrieve the top 1 match
results = vector_store.similarity_search(query, k=1)  # e.g., top 1 match

# --- Step 6: Print results ---
# Print the query and the most similar document found
print("Query:", query)
print("Most similar document found:")
for doc in results:
    print("- Content:", doc.page_content)
    print("  Metadata:", doc.metadata)