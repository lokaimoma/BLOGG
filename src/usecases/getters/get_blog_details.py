from typing import Optional, Callable

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from src.model import get_database_session
from src.model.blog import Blog


async def get_blog_details(blog_id: int, current_user: Optional[int] = None,
                           func: Callable[[], AsyncSession] = get_database_session):
    query = select(Blog).options(selectinload(Blog.engagements)).filter(Blog.id == blog_id)
    async with func() as session:
        result = await session.execute(query)
        blog = result.scalar_one_or_none()
        blog_domain_data = {
            "title": blog.title,
            "body": blog.body,
            "created_date": blog.created_date
        }
        title: str
        body: str
        created_date: Optional[datetime] = datetime.now()
        last_updated: Optional[datetime] = datetime.now()
        user_id: int