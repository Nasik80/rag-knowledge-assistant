from fastapi import FastAPI
from pydantic import BaseModel
from app.rag_pipeline import get_rag_chain

app = FastAPI()

qa_chain = get_rag_chain()


class QueryRequest(BaseModel):
    question: str


@app.post("/ask")
def ask_question(request: QueryRequest):

    result = qa_chain({"query": request.question})

    return {
        "answer": result["result"],
        "sources": [doc.metadata for doc in result["source_documents"]]
    }