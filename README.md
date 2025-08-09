# LangChain Groq Example Project

This project demonstrates how to use [LangChain](https://python.langchain.com/) with [Groq](https://groq.com/) for LLM-based applications in Python. It features 8 example scripts, robust environment variable handling, Docker support, and clear code commentary for educational and practical use.

## Features
- Simple hello world with Groq and LangChain
- Chat and message-based models
- Prompt templates
- Output parsers: datetime, comma-separated list, Pydantic, and structured output
- Docker support for containerized execution
- Modern Python best practices

## Example Scripts

| Script | Description |
|--------|-------------|
| 01-langchain-groq-hello.py | Basic hello world with Groq and LangChain |
| 02-langchain-chat-model.py | Chat model with invoke and stream |
| 03-langchain-message-model.py | Message-based conversation with roles |
| 04-llama-prompt-template.py | PromptTemplate for dynamic prompts |
| 05-langchain-tools-datetimeparser.py | Datetime output parser example |
| 06-langchain-tools-csv-output-parser.py | Comma-separated list output parser |
| 07-langchain-tools-pydantic-output-parser.py | Pydantic output parser for structured data |
| 08-langchain-tools-with-structured-output.py | Direct structured output using Pydantic |
| 09-langchain-example-chain-to-classify-sentiments.py | Sentiment classification using a LangChain chain (includes multi-step chain with parsing, summarization, and sentiment analysis) |
| 10-langchain-toolscalls-example.py | Tool calling example: Python function tool (discount calculator) with Groq |
| 11-langchain-vector-store.py | Vector store example: In-memory vector search with OpenAI embeddings (requires OPENAI_API_KEY) |

## Running Examples

### Locally
Activate your virtual environment and run any script:

```bash
python 01-langchain-groq-hello.py
python 02-langchain-chat-model.py
python 03-langchain-message-model.py
python 04-llama-prompt-template.py
python 05-langchain-tools-datetimeparser.py
python 06-langchain-tools-csv-output-parser.py
python 07-langchain-tools-pydantic-output-parser.py
python 08-langchain-tools-with-structured-output.py
```

### In Docker

Build the Docker image:

```bash
docker build -t langchain-groq-demo .
```

Run any example (replace `your_key_here` and script name):

```bash
docker run --rm -it -e GROQ_API_KEY=your_key_here langchain-groq-demo python 01-langchain-groq-hello.py
# or
# docker run --rm -it -e GROQ_API_KEY=your_key_here langchain-groq-demo python 08-langchain-tools-with-structured-output.py
```

Or start an interactive shell and run scripts manually:

```bash
docker run --rm -it -e GROQ_API_KEY=your_key_here langchain-groq-demo
# Then run: python 06-langchain-tools-csv-output-parser.py
```

### Example Usage Matrix

| Script | Local Command | Docker Command |
|--------|---------------|---------------|
| 01 | python 01-langchain-groq-hello.py | docker run --rm -it -e GROQ_API_KEY=your_key langchain-groq-demo python 01-langchain-groq-hello.py |
| 02 | python 02-langchain-chat-model.py | docker run --rm -it -e GROQ_API_KEY=your_key langchain-groq-demo python 02-langchain-chat-model.py |
| 03 | python 03-langchain-message-model.py | docker run --rm -it -e GROQ_API_KEY=your_key langchain-groq-demo python 03-langchain-message-model.py |
| 04 | python 04-llama-prompt-template.py | docker run --rm -it -e GROQ_API_KEY=your_key langchain-groq-demo python 04-llama-prompt-template.py |
| 05 | python 05-langchain-tools-datetimeparser.py | docker run --rm -it -e GROQ_API_KEY=your_key langchain-groq-demo python 05-langchain-tools-datetimeparser.py |
| 06 | python 06-langchain-tools-csv-output-parser.py | docker run --rm -it -e GROQ_API_KEY=your_key langchain-groq-demo python 06-langchain-tools-csv-output-parser.py |
| 07 | python 07-langchain-tools-pydantic-output-parser.py | docker run --rm -it -e GROQ_API_KEY=your_key langchain-groq-demo python 07-langchain-tools-pydantic-output-parser.py |
| 08 | python 08-langchain-tools-with-structured-output.py | docker run --rm -it -e GROQ_API_KEY=your_key langchain-groq-demo python 08-langchain-tools-with-structured-output.py |

---

## Prerequisites
- Python 3.10+
- [Groq API Key](https://console.groq.com/keys)

## Setup

```bash
# Clone the repo
git clone https://github.com/your-repo/your-repo.git
cd your-repo
# Create and activate a virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 4. Set up your `.env` file

Create a file named `.env` in this folder with the following line:

```env
GROQ_API_KEY=your_actual_groq_api_key_here
```

---

## Docker Usage

1. Build the Docker image:
   ```sh
   docker build -t langchain-groq-hello .
   ```
2. Run the container (pass your API key as an environment variable):
   ```sh
   docker run --rm -e GROQ_API_KEY=your_actual_groq_api_key_here langchain-groq-hello
   ```

---

## Troubleshooting
- **Missing API key:** Ensure `GROQ_API_KEY` is set in your environment or `.env` file.
- **Dependency errors:** Double-check you are in the correct virtual environment and `pip install -r requirements.txt` completed successfully.
- **Python version:** Use Python 3.9 or later.

---

## License

This project is licensed under the MIT License, a permissive open-source license that allows you to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the software for any purpose, including educational and commercial use, provided that the original copyright and license notice are included.

The MIT License is widely used for learning and open-source projects because it is simple, flexible, and encourages sharing and collaboration.

See the full license text below:

```
MIT License

Copyright (c) 2025 [Your Name or Organization]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
