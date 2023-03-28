from typing import List
from fastapi import FastAPI
from models import User, fake_users


app = FastAPI()


@app.get("/")
def get_hello():
    return "Hello world"

@app.get("/users/{user_id}")
def get_user(user_id: int):
    return fake_users[user_id - 1]

@app.post("/users")
def add_user(user: List[User]):
    fake_users.extend(user)
    return {"status": 200, "data": fake_users}
