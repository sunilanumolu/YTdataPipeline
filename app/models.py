from sqlalchemy import Column, Integer, String, Boolean, DateTime
from .database import Base

class Video(Base):
    __tablename__ = 'videos'
    id = Column(Integer, primary_key=True, autoincrement=True)
    video_id = Column(String)
    title = Column(String)
    channel_title = Column(String)
    category_id = Column(Integer)
    tags = Column(String)
    views = Column(Integer)
    likes = Column(Integer)
    dislikes = Column(Integer)
    comment_count = Column(Integer)
    thumbnail_link = Column(String)
    comments_disabled = Column(Boolean)
    ratings_disabled = Column(Boolean)
    video_error_or_removed = Column(Boolean)
    description = Column(String)
