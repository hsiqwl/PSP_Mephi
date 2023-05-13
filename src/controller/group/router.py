from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.database import get_async_session

router = APIRouter(
    prefix="/groups",
    tags=["Group"]
)


@router.get("/") #show all groups for user
async def get_user_groups(user_id: int, session: AsyncSession = Depends(get_async_session)):
    return


@router.post("/join_group") #add user to a group
async def add_user_to_group(group_id: int, user_id: int, session: AsyncSession = Depends(get_async_session)):
    return


@router.get("/group_users") #show all group users
async def get_all_group_users(group_id: int, session: AsyncSession = Depends(get_async_session)):
    return


@router.post("/create_group") #create new group
async def add_new_group(new_group_name: str, session: AsyncSession = Depends(get_async_session)):
    return
