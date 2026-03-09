from langchain_community.vectorstores import Chroma
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.embeddings import HuggingFaceEmbeddings

from app.config import VECTOR_DB_PATH, GEMINI_API_KEY


def get_rag_chain():

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    vectordb = Chroma(
        persist_directory=VECTOR_DB_PATH,
        embedding_function=embeddings
    )

    retriever = vectordb.as_retriever()

    llm = ChatGoogleGenerativeAI(
        model="gemini-pro",
        google_api_key=GEMINI_API_KEY
    )

    return retriever, llm