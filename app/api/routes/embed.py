from fastapi import APIRouter, HTTPException
from app.services.embedding_service import EmbeddingService
from typing import List

router = APIRouter()
embedding_service = EmbeddingService()

@router.post("/embed-texts")
async def embed_texts(texts: List[str]):
    """Endpoint to embed a list of texts"""
    try:
        embeddings = embedding_service.embed_texts(texts)
        return {"embeddings": embeddings}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) 
        