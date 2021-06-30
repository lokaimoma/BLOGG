from typing import Callable
from sqlalchemy.ext.asyncio import AsyncSession
from src.model import get_database_session
from src.domain_logic.blog_domain import BlogDomain
from src.model.blog import Blog


async def insert_blog(blogDomain: BlogDomain, func: Callable[[], AsyncSession] = get_database_session):
    blog = Blog(blogDomain=blogDomain)
    async with func() as session:
        session.add(blog)
        await session.commit()
