from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from src.schemas.posting.schemas import PostCreate
from src.database import get_async_session

router = APIRouter(
    prefix="/posts",
    tags=["Posts"]
)

@router.get("/") #shows most recent posts in group
async def get_recent_posts(group_id: int, session: AsyncSession = Depends(get_async_session)):
    return



