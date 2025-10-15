from sentence_transformers import SentenceTransformer

class EmbeddingGenerator:
    def __init__(self, model_name: str):
        self.model = SentenceTransformer(model_name)

    def embed_texts(self, texts):
        return self.model.encode(texts).tolist()
