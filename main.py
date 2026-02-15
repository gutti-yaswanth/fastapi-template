from fastapi import FastAPI
from api.routes.v1.router import router as api_router_v1
from api.routes.v2.router import router as api_router_v2
from core.db import engine, Base
from infrastructure.db.models import (
    User,
    Blog,
    Job,
    ZanUser,
    ZanCrew,
    ChatRoom,
    ChatParticipant,
    ChatMessage,
    MessageRead,
)  # Import models to register them
from core.cache import get_redis_client

app = FastAPI(title="Zanzo Service")

@app.on_event("startup")
async def startup_event():
    """Create database tables and initialize Redis connection on startup"""
    try:
        Base.metadata.create_all(bind=engine)
        print("Database tables created/verified successfully")
    except Exception as e:
        print(f"Warning: Could not create database tables: {e}")
        print("Make sure your CONNECTION_STRING is correct and the database is accessible")
    
    # Initialize Redis connection
    try:
        redis_client = get_redis_client()
        redis_client.ping()
        print("Redis connection established successfully")
    except Exception as e:
        print(f"Warning: Could not connect to Redis: {e}")
        print("Caching will be disabled. Make sure Redis is running and configured correctly.")

@app.get("/")
def main():
    return {"message": "Welcome to Zanzo Backend API"}

app.include_router(api_router_v1)
app.include_router(api_router_v2)