import chromadb
from chromadb.config import Settings
import os
from app.core.config import settings

class ChromaService:
    def __init__(self):
        # Create a persistent directory for ChromaDB
        self.persist_directory = "chroma_data"
        if not os.path.exists(self.persist_directory):
            os.makedirs(self.persist_directory)
        
        # Initialize ChromaDB client with persistence
        self.client = chromadb.PersistentClient(
            path=self.persist_directory,
            settings=Settings(
                allow_reset=True,
                is_persistent=True
            )
        )
        
        # Create or get the collection for storing chatbot data
        self.collection = self.client.get_or_create_collection(
            name="chatbot_tests",
            metadata={"hnsw:space": "cosine"}  # Using cosine similarity for matching
        )
    
    def add_documents(self, texts: list[str], metadata: list[dict], ids: list[str]):
        """
        Add documents to the collection
        """
        try:
            self.collection.add(
                documents=texts,
                metadatas=metadata,
                ids=ids
            )
            return True
        except Exception as e:
            print(f"Error adding documents: {e}")
            return False
    
    def query_similar(self, query_text: str, n_results: int = 5):
        """
        Query similar documents
        """
        try:
            results = self.collection.query(
                query_texts=[query_text],
                n_results=n_results
            )
            return results
        except Exception as e:
            print(f"Error querying documents: {e}")
            return None 