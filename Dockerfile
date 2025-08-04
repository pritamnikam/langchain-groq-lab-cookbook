# Dockerfile for LangChain Groq Hello Example\nFROM python:3.11-slim\n\n# Set workdir\nWORKDIR /app\n\n# Copy requirements and install dependencies\nCOPY requirements.txt ./\nRUN pip install --no-cache-dir -r requirements.txt\n\n# Copy code\nCOPY . .\n\n# Set environment variable for Python not to buffer stdout\nENV PYTHONUNBUFFERED=1\n\n# Default command\nCMD [\"python\", \"01-langchain-groq-hello.py\"]\n
# Dockerfile for LangChain Groq Hello Example
FROM python:3.11-slim

# Set workdir
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy code
COPY . .

# Set environment variable for Python not to buffer stdout
ENV PYTHONUNBUFFERED=1

# Usage: docker run --rm -it -e GROQ_API_KEY=your_key langchain-groq-demo python 01-langchain-groq-hello.py
ENTRYPOINT ["/bin/bash"]