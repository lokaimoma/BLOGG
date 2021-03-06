from typing import List, Callable

from sqlalchemy import select, desc
from sqlalchemy.ext.asyncio import AsyncSession

from src.model import get_database_session
from src.model.blog import Blog


async def get_all_blogs(func: Callable[[], AsyncSession] = get_database_session) -> List[Blog]:
    query = select(Blog).order_by(desc(Blog.last_updated))
    async with func() as session:
        result = await session.execute(query)
        blog_list = result.scalars().all()
        return blog_list
