from fastapi import FastAPI
from app.core.config import settings
from app.api.routes import test, embed, test_scenario

app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_V1_STR}/openapi.json"
)

# Include routers
app.include_router(test.router, prefix=settings.API_V1_STR, tags=["test"])
app.include_router(embed.router, prefix=settings.API_V1_STR, tags=["embed"])
app.include_router(test_scenario.router, prefix=settings.API_V1_STR, tags=["test_scenario"])

@app.get("/")
async def root():
    return {"message": "Welcome to Fix My Chatbot API"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}
