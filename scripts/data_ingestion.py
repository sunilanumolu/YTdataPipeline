import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../')

import pandas as pd
from app.database import SessionLocal, engine
from app.models import Base, Video
from app.schemas import VideoProfile
import logging

logging.basicConfig(level=logging.INFO)

# Read the CSV file
df = pd.read_csv(os.path.join(os.path.dirname(__file__), '../data/USvideos.csv')).fillna('')

# Create an SQLite database
Base.metadata.create_all(bind=engine)
session = SessionLocal()
logging.info('Starting ingestion into database')
# Insert data into the database
for _, row in df.iterrows():
    profile = VideoProfile(
        video_id=row['video_id'],
        title=row['title'],
        channel_title=row['channel_title'],
        category_id=row['category_id'],
        tags=row['tags'],
        views=row['views'],
        likes=row['likes'],
        dislikes=row['dislikes'],
        comment_count=row['comment_count'],
        thumbnail_link=row['thumbnail_link'],
        comments_disabled=row['comments_disabled'],
        ratings_disabled=row['ratings_disabled'],
        video_error_or_removed=row['video_error_or_removed'],
        description=row['description']
    )
    video = session.query(Video).filter(Video.video_id == profile.video_id).first()

    if video:
        # Update existing record
        video.title = profile.title
        video.channel_title = profile.channel_title
        video.category_id = profile.category_id
        video.tags = profile.tags
        video.views = profile.views
        video.likes = profile.likes
        video.dislikes = profile.dislikes
        video.comment_count = profile.comment_count
        video.thumbnail_link = profile.thumbnail_link
        video.comments_disabled = profile.comments_disabled
        video.ratings_disabled = profile.ratings_disabled
        video.video_error_or_removed = profile.video_error_or_removed
        video.description = profile.description
    else:
        # Insert new record
        video = Video(
            video_id=profile.video_id,
            title=profile.title,
            channel_title=profile.channel_title,
            category_id=profile.category_id,
            tags=profile.tags,
            views=profile.views,
            likes=profile.likes,
            dislikes=profile.dislikes,
            comment_count=profile.comment_count,
            thumbnail_link=profile.thumbnail_link,
            comments_disabled=profile.comments_disabled,
            ratings_disabled=profile.ratings_disabled,
            video_error_or_removed=profile.video_error_or_removed,
            description=profile.description
        )
    session.add(video)
logging.info('Completed ingestion into database, of all video profiles')
session.commit()
