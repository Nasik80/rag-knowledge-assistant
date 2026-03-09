from fastapi import FastAPI
from pydantic import BaseModel

from app.rag_pipeline import get_rag_chain

app = FastAPI()

retriever, llm = get_rag_chain()


class QueryRequest(BaseModel):
    question: str


@app.post("/ask")
async def ask_question(request: QueryRequest):

    docs = retriever.invoke(request.question)

    context = "\n\n".join([doc.page_content for doc in docs])

    prompt = f"""
Answer the question based on the context below.

Context:
{context}

Question:
{request.question}
"""

    response = llm.invoke(prompt)

    return {
        "answer": response.content,
        "sources": [doc.metadata for doc in docs]
    }