from sentence_transformers import SentenceTransformer
from app.core.config import settings

class EmbeddingService:
    def __init__(self):
        # Load the embedding model
        self.model = SentenceTransformer(settings.EMBEDDING_MODEL)

    def embed_texts(self, texts: list[str]) -> list[list[float]]:
        """
        Convert a list of texts into their corresponding embeddings.
        """
        embeddings = self.model.encode(texts, convert_to_tensor=True)
        return embeddings.tolist()  # Convert tensor to list for easier handling 