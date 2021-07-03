from typing import Callable

from sqlalchemy import delete
from sqlalchemy.ext.asyncio import AsyncSession

from src.model import get_database_session
from src.model.blog import Blog
from src.model.engagement import Engagement


async def delete_blog(blog_id: int,
                      func: Callable[[], AsyncSession] = get_database_session):
    blog_query = delete(Blog).where(Blog.id == blog_id)
    engagement_query = delete(Engagement).where(Engagement.blog_id == blog_id)
    async with func() as session:
        await session.execute(blog_query)
        await session.execute(engagement_query)
        await session.commit()
