from fastapi import FastAPI, HTTPException
from .database import SessionLocal, engine
from .models import Base, Video
from .schemas import VideoProfile
from .crud import get_video
from .routers import videos
import uvicorn
import asyncio
from .event_manager import fetch_trending_video
import logging

logging.basicConfig(level=logging.INFO)

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(videos.router)

@app.on_event("startup")
async def startup_event():
    asyncio.create_task(fetch_trending_video())

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
