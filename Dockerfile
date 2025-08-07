# Dockerfile for LangChain Groq Python Examples
# Build with: docker build -t langchain-groq-demo .

FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy all project files
COPY . .

# Ensure Python output is unbuffered
ENV PYTHONUNBUFFERED=1

# Usage examples for all scripts:
# docker run --rm -it -e GROQ_API_KEY=your_key langchain-groq-demo python 01-langchain-groq-hello.py
# docker run --rm -it -e GROQ_API_KEY=your_key langchain-groq-demo python 02-langchain-chat-model.py
# docker run --rm -it -e GROQ_API_KEY=your_key langchain-groq-demo python 03-langchain-message-model.py
# docker run --rm -it -e GROQ_API_KEY=your_key langchain-groq-demo python 04-llama-prompt-template.py
# docker run --rm -it -e GROQ_API_KEY=your_key langchain-groq-demo python 05-langchain-tools-datetimeparser.py
# docker run --rm -it -e GROQ_API_KEY=your_key langchain-groq-demo python 06-langchain-tools-csv-output-parser.py
# docker run --rm -it -e GROQ_API_KEY=your_key langchain-groq-demo python 07-langchain-tools-pydantic-output-parser.py
# docker run --rm -it -e GROQ_API_KEY=your_key langchain-groq-demo python 08-langchain-tools-with-structured-output.py
# docker run --rm -it -e GROQ_API_KEY=your_key langchain-groq-demo python 09-langchain-example-chain-to-classify-sentiments.py
# docker run --rm -it -e GROQ_API_KEY=your_key langchain-groq-demo python 10-langchain-toolscalls-example.py

# Default to bash shell for flexible script execution
ENTRYPOINT ["/bin/bash"]