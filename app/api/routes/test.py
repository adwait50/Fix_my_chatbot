from fastapi import APIRouter, HTTPException
from app.services.chroma_service import ChromaService
import uuid

router = APIRouter()
chroma_service = ChromaService()

@router.post("/add-test-data")
async def add_test_data():
    """Test endpoint to add sample data to ChromaDB"""
    try:
        # Sample test data
        texts = [
            "How can I reset my password?",
            "What are your business hours?",
            "Can I get a refund?"
        ]
        
        metadata = [
            {"type": "support", "category": "account"},
            {"type": "info", "category": "general"},
            {"type": "support", "category": "billing"}
        ]
        
        # Generate unique IDs
        ids = [str(uuid.uuid4()) for _ in range(len(texts))]
        
        success = chroma_service.add_documents(texts, metadata, ids)
        
        if success:
            return {"message": "Test data added successfully"}
        else:
            raise HTTPException(status_code=500, message="Failed to add test data")
            
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/query-similar/{query_text}")
async def query_similar(query_text: str):
    """Test endpoint to query similar documents"""
    try:
        results = chroma_service.query_similar(query_text)
        return {"results": results}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) 