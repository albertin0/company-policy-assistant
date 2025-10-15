import os

# Environment / configuration variables
GROQ_API_KEY = os.getenv("GROQ_API_KEY", "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")
QDRANT_HOST = os.getenv("QDRANT_HOST", "localhost")
QDRANT_PORT = int(os.getenv("QDRANT_PORT", 6333))
VECTOR_COLLECTION = "company_policy"
EMBEDDING_MODEL = "all-MiniLM-L6-v2"
