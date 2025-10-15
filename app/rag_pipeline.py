from qdrant_client import QdrantClient
from qdrant_client.http import models
from app.embeddings import EmbeddingGenerator
from app.config import QDRANT_HOST, QDRANT_PORT, VECTOR_COLLECTION, EMBEDDING_MODEL, GROQ_API_KEY

# Replace this stub with real Groq SDK call when available
def call_groq_llm(prompt: str) -> str:
    # Placeholder Groq LLM function
    # You can later integrate the Groq API endpoint here
    return f"[Groq LLM Response]\n\n{prompt[:400]}..."

class RAGPipeline:
    def __init__(self):
        self.client = QdrantClient(host=QDRANT_HOST, port=QDRANT_PORT)
        self.embedder = EmbeddingGenerator(EMBEDDING_MODEL)

    def initialize_db(self, chunks):
        print("Initializing vector database with company handbook...")
        embeddings = self.embedder.embed_texts([c["text"] for c in chunks])

        self.client.recreate_collection(
            collection_name=VECTOR_COLLECTION,
            vectors_config=models.VectorParams(size=len(embeddings[0]), distance=models.Distance.COSINE),
        )

        self.client.upload_collection(
            collection_name=VECTOR_COLLECTION,
            vectors=embeddings,
            payload=chunks,
            ids=list(range(len(chunks))),
        )
        print("Database ready ✅")

    def retrieve_context(self, query: str, top_k: int = 3):
        query_embedding = self.embedder.embed_texts([query])[0]
        results = self.client.search(collection_name=VECTOR_COLLECTION, query_vector=query_embedding, limit=top_k)
        return " ".join([r.payload["text"] for r in results])

    def answer_query(self, query: str):
        context = self.retrieve_context(query)
        prompt = f"Use the following company policy information to answer.\n\n{context}\n\nQuestion: {query}\nAnswer:"
        return call_groq_llm(prompt)