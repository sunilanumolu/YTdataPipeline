import asyncio
import logging
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models import Video

logging.basicConfig(level=logging.INFO)

async def fetch_trending_video():
    while True:
        logging.info("Fetching the most trending video based on views...")
        
        # Create a new session
        db = SessionLocal()
        try:
            # Query the database for the video with the highest views
            trending_video = db.query(Video).order_by(Video.views.desc()).first()
            if trending_video:
                logging.info(f"Most Trending Video: {trending_video.title}, Views: {trending_video.views}")
            else:
                logging.info("No videos found in the database.")
        finally:
            db.close()
        
        # Wait for 30 sec
        await asyncio.sleep(30)
