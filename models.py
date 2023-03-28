from pydantic import BaseModel, Field


class User(BaseModel):
    id: int
    name: str
    email: str = Field(max_length=30)

fake_users = [
    {"id": 1, "name": "raif", "email": "1@example.com"},
    {"id": 2, "name": "bob", "email": "2@example.com"},
    {"id": 3, "name": "jamal", "email": "3@example.com"},
]