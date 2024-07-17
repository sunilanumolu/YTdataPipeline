import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../')
from sqlalchemy.orm import sessionmaker
from app.database import engine
from app.models import Video


# Create a new session
Session = sessionmaker(bind=engine)
session = Session()

# Query the database
videos = session.query(Video).limit(10).all()

print('Results first 10 video profiles')
# Display the results
for video in videos:
    print(f"Video ID: {video.video_id}, Title: {video.title}, Views: {video.views}, Likes: {video.likes}, Dislikes: {video.dislikes}") 

session.close()
