from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.services.embedding_service import EmbeddingService
from typing import List
import random

router = APIRouter()
embedding_service = EmbeddingService()

class ScenarioRequest(BaseModel):
    task: str

@router.post("/generate-scenario")
async def generate_scenario(request: ScenarioRequest):
    """Endpoint to generate a test scenario based on a user-defined task"""
    try:
        task = request.task  # Access the task from the request body
        # Generate a user persona, chatbot goal, and task description
        user_persona = generate_user_persona()
        chatbot_goal = generate_chatbot_goal()
        scenario = {
            "user_persona": user_persona,
            "chatbot_goal": chatbot_goal,
            "task": task
        }
        
        # Create embeddings for the scenario
        embeddings = embedding_service.embed_texts([task, user_persona, chatbot_goal])
        
        return {
            "scenario": scenario,
            "embeddings": embeddings
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

def generate_user_persona() -> str:
    """Generate a random user persona"""
    personas = [
        "A tech-savvy millennial looking for quick solutions.",
        "A senior citizen needing assistance with technology.",
        "A busy professional seeking efficient customer service.",
        "A student looking for information on academic resources."
    ]
    return random.choice(personas)

def generate_chatbot_goal() -> str:
    """Generate a random chatbot goal"""
    goals = [
        "Assist users with account-related queries.",
        "Provide information about business hours and services.",
        "Help users navigate the website.",
        "Answer frequently asked questions."
    ]
    return random.choice(goals) 