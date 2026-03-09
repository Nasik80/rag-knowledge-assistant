from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from app.config import DOCUMENT_PATH, VECTOR_DB_PATH, GEMINI_API_KEY

import os


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

    embeddings = GoogleGenerativeAIEmbeddings(
        model="models/embedding-001",
        google_api_key=GEMINI_API_KEY
    )

    vectordb = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=VECTOR_DB_PATH
    )

    vectordb.persist()

    print("Documents successfully embedded!")