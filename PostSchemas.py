from pydantic import BaseModel


class Comment(BaseModel):
    user: str
    content: str
    photo: str = None


class PostSchema(BaseModel):
    user: str
    date: str
    text: str
    likes: list = []
    comments: list = []