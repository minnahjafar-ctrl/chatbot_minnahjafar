#TASK1 - chatbot_minnahjafar

## Problem Statement
- Build an AI chatbot using Groq API and Python
- Receive user input and generate AI responses
- Store previous conversations for multi-turn interaction

## Approach Adopted
- Used Python and Groq API to develop the chatbot
- Tested different settings such as max_tokens and temperature
- Compared chatbot responses under different parameter values

## Steps Involved
- Created the chatbot using Python
- Connected the chatbot to Groq API
- Tested the chatbot in single-turn mode
- Converted the chatbot into multi-turn mode
- Stored previous conversation history
- Tested the chatbot using different inputs
- Modified max_tokens and temperature settings to observe response changes

## Challenges Faced
- Faced difficulty understanding API integration initially
- Converting the chatbot from single-turn mode to multi-turn mode was challenging
- Resolved issues through testing and experimentation

## How to Run the Application
1. Download or clone the project
2. Open the project folder in Visual Studio Code
3. Install the required Python package
4. Run the Python file
5. Start interacting with the chatbot

# Task 2 – RAG PDF Chatbot

## Overview
- Developed a RAG (Retrieval-Augmented Generation) based PDF chatbot.
- The chatbot answers user queries using information retrieved from uploaded PDF documents.
- Built using Python, Streamlit, LangChain, ChromaDB, and Groq API.

---

## Features
- PDF document upload
- Text extraction from PDFs
- Text chunking
- Embedding generation
- Vector database storage using ChromaDB
- Retrieval of relevant chunks
- AI-generated answers
- Chat history support

---

## Workflow
1. Upload PDF document
2. Extract text from PDF
3. Split text into smaller chunks
4. Generate embeddings for chunks
5. Store embeddings in ChromaDB
6. Retrieve relevant chunks based on user query
7. Generate final response using the LLM

---

## Technologies Used
- Python
- Streamlit
- LangChain
- ChromaDB
- Groq API
- PyPDF
- Sentence Transformers

---

## How Retrieval Works
- The uploaded PDF is converted into text chunks.
- Embeddings are generated for each chunk.
- The embeddings are stored in ChromaDB.
- When a user asks a question, the most relevant chunks are retrieved using semantic similarity.
- The retrieved chunks are passed to the LLM to generate the final answer.

---

## Retrieved Chunks
- Relevant chunks from the PDF are displayed to show the source of the generated answer.
- This improves transparency and answer reliability.

---

## Issues Faced
- Streamlit rerun issues
- ChromaDB permission errors on Windows
- Managing vector database updates
- Handling PDF uploads properly
- API key security during GitHub push

---

## Possible Improvements
- Support for multiple PDF uploads
- Better UI design
- Improved retrieval accuracy
- Better chat memory handling
- Smarter chunking strategies
- Source highlighting in answers

---

## Files Included
- rag.py
- requirements.txt
- Sample PDF
- Screenshots of retrieved chunks
- Screenshots of final answers
