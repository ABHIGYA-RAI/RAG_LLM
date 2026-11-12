# Integrated RAG System with Ollama, MySQL & REST API

An AI-powered application integrating **Retrieval-Augmented Generation (RAG), Large Language Models (LLMs), MySQL Database, and RESTful APIs** to deliver context-aware, knowledge-grounded responses through structured JSON communication.

## Overview

This project implements an integrated Retrieval-Augmented Generation (RAG) architecture that combines the capabilities of locally hosted Large Language Models with external knowledge retrieval and structured database management.

The system retrieves relevant information from a knowledge base, augments user queries with retrieved context, and generates contextually relevant responses using **Ollama** as the LLM runtime.

MySQL handles structured data storage and management, while REST APIs facilitate communication between the application components through JSON-based request and response handling.

## Key Features

- **Retrieval-Augmented Generation (RAG):** Retrieves relevant information from an external knowledge base to improve response accuracy and contextual relevance.
- **Local LLM Integration:** Uses Ollama to run and interact with locally hosted Large Language Models.
- **MySQL Database Integration:** Manages structured application data, metadata, and persistent records.
- **REST API Development:** Provides API endpoints for communication between application components.
- **JSON Data Exchange:** Uses JSON for structured API requests and responses.
- **Context-Aware Responses:** Generates responses grounded in retrieved information rather than relying exclusively on the LLM's pretrained knowledge.
- **Modular Architecture:** Separates retrieval, generation, database operations, and API services for easier maintenance and scalability.

## System Architecture

The system follows a modular RAG pipeline:

1. **User Query:** Receives a question through the REST API.
2. **Query Processing:** Processes and prepares the incoming query for retrieval.
3. **Knowledge Retrieval:** Searches the knowledge base for semantically relevant information.
4. **Context Augmentation:** Combines the retrieved information with the original user query.
5. **LLM Inference:** Sends the augmented prompt to an Ollama-hosted LLM.
6. **Response Generation:** Generates a context-aware response based on the retrieved information.
7. **Database Operations:** Uses MySQL to manage relevant application data and records.
8. **API Response:** Returns the generated output through a structured JSON response.

## Technology Stack

| Category | Technologies |
|---|---|
| Programming Language | Python |
| Generative AI | Ollama |
| AI Architecture | Retrieval-Augmented Generation (RAG) |
| Database | MySQL |
| API Development | REST API |
| Data Serialization | JSON |
| LLM Runtime | Ollama |





## API Communication

The system uses RESTful endpoints to receive user queries and return generated responses in JSON format.

**Example Request**

```json
{
    "query": "What is Retrieval-Augmented Generation?"
}
```

**Example Response**

```json
{
    "status": "success",
    "query": "What is Retrieval-Augmented Generation?",
    "response": "Retrieval-Augmented Generation is an AI architecture that combines information retrieval with generative language models to produce contextually grounded responses.",
    "sources": []
}
```

