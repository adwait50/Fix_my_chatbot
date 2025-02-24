from pydantic_settings import BaseSettings
from functools import lru_cache

class Settings(BaseSettings):
    # API Config
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "Fix My Chatbot"
    
    # Model Config
    EMBEDDING_MODEL: str = "all-MiniLM-L6-v2"
    LLM_MODEL: str = "mistralai/Mistral-7B-v0.1"
    
    # ChromaDB Config
    CHROMA_DATA_DIR: str = "chroma_data"
    COLLECTION_NAME: str = "chatbot_tests"
    
    class Config:
        case_sensitive = True

@lru_cache()
def get_settings():
    return Settings()

settings = get_settings()