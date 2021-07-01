from typing import Optional, List, Callable

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.model import get_database_session
from src.model.blog import Blog


async def get_blogs_by_user_id(user_id: int,
                               func: Callable[[], AsyncSession]
                               = get_database_session) -> Optional[List[Blog]]:
    query = select(Blog).filter(Blog.user_id == user_id)
    async with func() as session:
        result = await session.execute(query)
        return result.scalars().all()
