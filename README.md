## RAG Prompt Builder & Generator CLI

## 📖 Overview

This project demonstrates the **Generation** stage of a Retrieval-Augmented Generation (RAG) pipeline.

The application retrieves relevant document chunks based on a user's question, constructs a context-aware prompt, and sends that prompt to an OpenAI Large Language Model (LLM) to generate a grounded answer.

For simplicity, this implementation uses a **mock retriever** with a small in-memory database instead of a real vector database such as FAISS or Chroma.

---

# 🚀 Features

* Simple command-line interface (CLI)
* Mock document retrieval
* Prompt construction using retrieved context
* OpenAI GPT integration
* Grounded responses with hallucination prevention
* Graceful error handling
* Continuous Q&A loop until user exits

---

# 🏗️ Project Structure

```
.
├── app.py          # Main RAG CLI application
├── README.md       # Documentation
└── requirements.txt
```

---

# ⚙️ How It Works

The application follows the standard RAG workflow.

```
User Question
      │
      ▼
Retriever (Mock Database)
      │
      ▼
Relevant Chunks
      │
      ▼
Prompt Builder
      │
      ▼
OpenAI GPT Model
      │
      ▼
Generated Answer
```

---

# 📂 Components

## 1. Retriever

The retriever searches through a mock database and returns the most relevant document chunks.

```python
retrieve_chunks(query)
```

Current implementation:

* Uses keyword matching
* Returns top matching chunks
* Simulates a vector database

In production, this can be replaced with:

* FAISS
* ChromaDB
* Pinecone
* Weaviate
* Milvus

---

## 2. Prompt Builder

The prompt builder combines all retrieved chunks into a single prompt.

Responsibilities:

* Join retrieved context
* Separate chunks clearly
* Prevent hallucinations
* Force the model to answer only from provided context

Example prompt:

```
Context:
Chunk 1
---
Chunk 2
---
Chunk 3

Question:
What is Ubuntu?

Answer:
```

---

## 3. Generator

The generator sends the prompt to the OpenAI Chat Completion API.

Settings used:

* Model: `gpt-3.5-turbo`
* Temperature: `0.0`

A low temperature improves factual consistency by reducing randomness.

---

## 4. CLI Interface

The CLI continuously accepts user questions until the user types:

```
exit
```

or

```
quit
```

---

# 📦 Installation

## Clone the repository

```bash
git clone https://github.com/gayatori-san/unprof_pyai_21
cd rag-prompt-builder
```

---

## Create a virtual environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## Install dependencies

```bash
pip install -r requirements.txt
```

or install manually:

```bash
pip install openai
```

---

# 🔑 Environment Variable

Set your OpenAI API key before running the application.

### Linux/macOS

```bash
export OPENAI_API_KEY="your_api_key"
```

### Windows (Command Prompt)

```cmd
set OPENAI_API_KEY=your_api_key
```

### Windows (PowerShell)

```powershell
$env:OPENAI_API_KEY="your_api_key"
```

---

# ▶️ Running the Application

```bash
python app.py
```

Example:

```
Welcome to the Document Q&A CLI!

📝 Enter your question:
What is RAG?

🔍 Retrieving relevant chunks...

🤖 Generating answer...

💬 Answer:
RAG stands for Retrieval-Augmented Generation, combining search with LLMs.
```

---

# 🧠 Sample Knowledge Base

The mock database contains the following example documents:

* Linux Kernel
* Ubuntu Package Manager
* Retrieval-Augmented Generation
* Quick Brown Fox sentence

---

# 🛠 Technologies Used

* Python 3
* OpenAI API
* GPT-3.5 Turbo
* Command Line Interface (CLI)

---

# 🔮 Future Improvements

* Replace mock retrieval with FAISS
* Add PDF document ingestion
* Use embeddings for semantic search
* Store vectors in ChromaDB
* Support multiple document collections
* Add streaming responses
* Implement conversation memory
* Build a web interface using Streamlit or Flask

---

# 📚 Learning Outcomes

After completing this project, you will understand:

* Retrieval-Augmented Generation (RAG)
* Context-aware prompt engineering
* Prompt construction techniques
* OpenAI Chat Completion API
* Grounding LLM responses
* CLI application development
* Error handling in Python
* End-to-end RAG workflow
