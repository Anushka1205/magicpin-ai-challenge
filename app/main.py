from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database import models
from app.database.database import Base, engine
from app.api.health import router as health_router
from app.api.context import router as context_router
from app.api.message import router as message_router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Magicpin AI Backend Challenge",
    description="AI-powered merchant assistant for Magicpin",
    version="1.0.0"
)

# Enable CORS for React frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(health_router)
app.include_router(context_router)
app.include_router(message_router)


@app.get("/")
def root():
    return {
        "message": "Magicpin AI Backend Challenge is running!"
    }