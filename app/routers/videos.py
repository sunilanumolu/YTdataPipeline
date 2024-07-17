from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import Video
from app.schemas import VideoProfile
from app.crud import get_video
import logging

logging.basicConfig(level=logging.INFO)

router = APIRouter()

@router.get("/videos/{video_id}", response_model=list[VideoProfile])
def read_video(video_id: str, db: Session = Depends(get_db)):
    logging.info(f"Fetching video details based on video_id : {video_id}")
    video = get_video(db, video_id)
    logging.info(f"Fetched video details based on video_id : {video_id}")
    if not video:
        raise HTTPException(status_code=404, detail="Video not found")
    return video    
