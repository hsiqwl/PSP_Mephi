from fastapi import FastAPI
from src.controller.auth.base_config import auth_backend, fastapi_users
from src.schemas.auth.schemas import UserRead, UserCreate
from src.controller.group.router import router as router_group
from src.controller.posting.router import router as router_posting

app = FastAPI()


app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)

app.include_router(router_group)

app.include_router(router_posting)


