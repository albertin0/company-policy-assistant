from fastapi import FastAPI
from pydantic import BaseModel
from app.pdf_loader import load_and_chunk_pdf
from app.rag_pipeline import RAGPipeline

app = FastAPI(title="Company Policy Assistant (Groq + Qdrant)")
rag = RAGPipeline()

class Query(BaseModel):
    question: str

@app.on_event("startup")
def startup_event():
    chunks = load_and_chunk_pdf("data/IT-Policy-Veedol.pdf")
    rag.initialize_db(chunks)

@app.post("/ask")
def ask_question(query: Query):
    answer = rag.answer_query(query.question)
    return {"answer": answer}
