import os
import json
import redis
import logging
from app.database import SessionLocal
from app.models import Video

logging.basicConfig(level=logging.INFO)

# Configure Redis
redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)

# Directory for object store (local file system)
OBJECT_STORE_DIR = 'object_store'

# Ensure the directory exists
os.makedirs(OBJECT_STORE_DIR, exist_ok=True)

def move_data_to_stores():
    db = SessionLocal()
    try:
        videos = db.query(Video).order_by(Video.views.desc()).limit(100).all()
        for video in videos:
            # Move metadata to Redis
            metadata = {
                'video_id': video.video_id,
                'title': video.title,
                'views': video.views,
                'likes': video.likes,
                'dislikes': video.dislikes,
                'comment_count': video.comment_count,
            }
            redis_key = f"video_metadata:{video.video_id}"
            redis_client.set(redis_key, json.dumps(metadata))
            logging.info(f"Stored metadata for video {video.video_id} {video.title} in Redis.")
            
            # Move description to object store (local file system)
            description_file_path = os.path.join(OBJECT_STORE_DIR, f"{video.video_id}.txt")
            with open(description_file_path, 'w') as file:
                file.write(video.description)
            logging.info(f"Stored description for video ID {video.video_id} {video.title} in object store.")
    finally:
        db.close()

if __name__ == "__main__":
    move_data_to_stores()
