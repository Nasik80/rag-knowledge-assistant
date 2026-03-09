from langchain_community.vectorstores import Chroma
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains import RetrievalQA

from app.config import VECTOR_DB_PATH, GEMINI_API_KEY
from langchain_google_genai import GoogleGenerativeAIEmbeddings


def get_rag_chain():

    embeddings = GoogleGenerativeAIEmbeddings(
        model="models/embedding-001",
        google_api_key=GEMINI_API_KEY
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

    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        return_source_documents=True
    )

    return qa_chain