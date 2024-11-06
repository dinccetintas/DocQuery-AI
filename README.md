# PDF-RAG Assistant

## Overview

**PDF-RAG Assistant** is a Retrieval-Augmented Generation (RAG) chatbot application built using IBM Watsonx AI and LangChain. The application allows users to upload PDF documents, which are processed and embedded into a vector database. Users can then ask questions about the content of the uploaded PDF, and the chatbot will retrieve relevant sections from the document to answer the query. This project is designed with clean code and object-oriented principles, making it modular and easy to maintain.

## Features

- **PDF Upload and Processing**: Upload PDF documents, which are split into text chunks.
- **Vector Storage**: Embedded document chunks are stored in a vector database for efficient retrieval.
- **Retrieval-Augmented Generation**: Uses IBM Watsonx AI's language models to generate answers based on retrieved document content.
- **Interactive Chatbot Interface**: Built with Gradio for a user-friendly experience.

## Project Structure

```plaintext
pdf-rag-assistant/
│
├── app/
│   ├── __init__.py
│   ├── chatbot.py           # Defines the RAGChatbot class for chatbot functionality
│   └── interface.py         # Manages the Gradio interface setup
│
├── config/
│   └── config.py            # Configuration files for model parameters and API keys
│
├── data/                    # Folder to store any sample PDF data for testing
│
├── models/
│   └── model.py             # Defines the Watsonx model wrapper and helper functions
│
├── processing/
│   └── vector_store.py      # Handles vector store creation and retrieval
│
├── retriever/
│   └── retriever.py         # Defines the document retrieval process
│
├── utils/
│   ├── __init__.py
│   └── suppress_warnings.py # Utility to suppress warnings
│
├── .env                     # Environment variables for API keys (not included in the repo)
├── main.py                  # Main entry point to run the application
├── requirements.txt         # Dependencies required to run the project
└── README.md                # Project documentation

```


## Prerequisites

- **Python** 3.8 or higher
- **IBM Watsonx AI** account and API access
- **Docker** (optional, for containerized deployment)

## Installation

  1. **Clone the repository:**
   ```bash
   git clone https://github.com/dinccetintas/pdf-rag-assistant.git
   cd pdf-rag-assistant
  ```
  2. **Create a virtual environment and activate it:**
  ```bash
  python3 -m venv rag_langchain
source rag_langchain/bin/activate
  ```
  3. **Install dependencies:**
  ```bash
  pip install -r requirements.txt
  ```
  4. **Configure environment variables:**
  ```bash
  Create a .env file in the root directory and add your IBM Watsonx API credentials:

  API_KEY=your_ibm_watsonx_api_key
  PROJECT_ID=your_project_id
  MODEL_ID=your_model_id_for_embeddings
  URL=your_ibm_watsonx_url
  ```
## Usage

  1.	**Run the Application:**
  ```bash
  python main.py
  ```
  3.	**Interact with the Chatbot:**
	    •	Open the Gradio interface in your browser (typically http://localhost:7860).
	    •	Upload a PDF document and ask questions based on its content.
    	
## Key Files

- `main.py`: Entry point to start the Gradio-based chatbot application.
- `app/chatbot.py`: Contains the RAGChatbot class for managing RAG functionality.
- `app/interface.py`: Sets up and configures the Gradio interface.
- `config/config.py`: Manages configuration variables and API keys.
- `processing/vector_store.py`: Handles vector database setup and embeddings.
- `retriever/retriever.py`: Manages document retrieval operations.

## Project Details

- **Embedding Model**: IBM Watsonx AI embedding model.
- **Text Processing**: PDF documents are processed, split into chunks, and stored as embeddings.
- **Vector Database**: Chroma is used as the vector storage for efficient retrieval.
 
