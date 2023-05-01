from datetime import date
from pydantic import BaseModel


class PostCreate(BaseModel):
    id: int
    author_id: int
    group_id: int
    post_name: str
    date: date
    text: str


class PostRead(BaseModel):
    id: int
    author_id: int
    group_id: int
    post_name: str
    date: date
    text: str
