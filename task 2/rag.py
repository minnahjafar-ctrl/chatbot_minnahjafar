from langchain_community.document_loaders import PyPDFLoader # pdf loading tool
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings #form embeddings
from langchain_community.vectorstores import Chroma #to store embeddings
from groq import Groq
import os
import glob

client = Groq(
    api_key="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"
)

documents = []

pdf_files = glob.glob("pdfs/*.pdf")

for pdf_file in pdf_files:

    print(f"Loading {pdf_file}...")

    loader = PyPDFLoader(pdf_file) #Makes an object of notespdf

    documents.extend(loader.load()) #forms document objects and adds to documents list


# loader = PyPDFLoader("notes.pdf") #Makes an object of notespdf

# documents = loader.load() #forms document objects

#print(documents[0])

#chunking object

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500, #no of characters
    chunk_overlap=50 #similar char in consecutive chunks
)

chunks = text_splitter.split_documents(documents) #forms chunks

# print("chunk 1 = ",chunks[0])
# print("\n chunk 2 = ",chunks[1])

# Load embedding model
embedding_model = HuggingFaceEmbeddings(
    model_name="all-MiniLM-L6-v2"
)

# Store embeddings in ChromaDB

print("Creating vector database...")

if os.path.exists("chroma_db"):

    print("Loading existing vector database...")

    vectorstore = Chroma(
        persist_directory="chroma_db",
        embedding_function=embedding_model
    )

else:

    print("Creating new vector database...")

    vectorstore = Chroma.from_documents(
        documents=chunks,
        embedding=embedding_model,
        persist_directory="chroma_db"
    )

    print("Vector database created successfully")

print("Vector database created successfully")

#print("Number of chunks:", len(chunks))

chat_history = []

def ask_rag(query,chat_history):
# while True:


    # query = input("\nAsk a question: ")

    # if query.lower() == "exit":
    #     print("Exiting the program...")
    #     break

    retrieved_docs = vectorstore.similarity_search(
        query,
        k=3
    )

    # print("\nRetrieved Chunks:\n")

    # for doc in retrieved_docs:
    #     print(doc.page_content)
    #     print("\n" + "-"*50 + "\n")

    context = "\n\n".join(
        [doc.page_content for doc in retrieved_docs]
    )

    prompt = f"""
    Answer the question using only the provided context.

    Chat History:
    {chat_history}

    Context:
    {context}

    Question:
    {query}
    """
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    answer=(response.choices[0].message.content)

    # print("\nSource Chunks:\n")

    # for i, doc in enumerate(retrieved_docs, start=1):

    #     print(f"Chunk {i}:\n")

    #     print(doc.page_content)

    #     print("\n" + "-"*50 + "\n")


    # chat_history.append(f"User: {query}")

    # chat_history.append(
    # f"Assistant: {response.choices[0].message.content}"
    # )

    return answer,retrieved_docs