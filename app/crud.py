from sqlalchemy.orm import Session
from .models import Video

def get_video(db: Session, video_id: str):
    return db.query(Video).filter(Video.video_id == video_id).all()
