import os

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma

from app.config import DOCUMENT_PATH, VECTOR_DB_PATH, GEMINI_API_KEY


def ingest_documents():

    documents = []

    for file in os.listdir(DOCUMENT_PATH):

        if file.endswith(".pdf"):

            loader = PyPDFLoader(f"{DOCUMENT_PATH}/{file}")
            docs = loader.load()

            documents.extend(docs)

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=100
    )

    chunks = text_splitter.split_documents(documents)

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    vectordb = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=VECTOR_DB_PATH
    )

    vectordb.persist()

    print("Documents successfully embedded!")