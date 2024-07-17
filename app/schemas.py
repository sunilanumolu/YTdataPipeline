from pydantic import BaseModel

class VideoProfile(BaseModel):
    video_id: str
    title: str
    channel_title: str
    category_id: int
    tags: str
    views: int
    likes: int
    dislikes: int
    comment_count: int
    thumbnail_link: str
    comments_disabled: bool
    ratings_disabled: bool
    video_error_or_removed: bool
    description: str

    class Config:
        from_attributes = True
