from typing import Callable

from sqlalchemy import delete
from sqlalchemy.ext.asyncio import AsyncSession

from src.model.blog import Blog


async def delete_blog(blog_id: int,
                      func: Callable[[], AsyncSession]):
    query = delete(Blog).where(Blog.id == blog_id)
    async with func() as session:
        await session.execute(query)
        await session.commit()
