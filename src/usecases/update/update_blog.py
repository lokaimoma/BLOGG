from typing import Callable

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.domain_logic.blog_domain import BlogDomain
from src.model import get_database_session
from src.model.blog import Blog
from src.usecases.insert.insert_blog import insert_blog


async def update_blog(blog_id: int, blog_info: BlogDomain, func: Callable[[], AsyncSession] = get_database_session):
    async with func() as session:
        blog_query = select(Blog).filter(Blog.id == blog_id)
        result = await session.execute(blog_query)
        blog: Blog = result.scalar_one_or_none()
        if blog:
            blog.title = blog_info.title
            blog.body = blog_info.body
            blog.last_updated = blog_info.last_updated
            await session.commit()
            return

        await insert_blog(blogDomain=blog_info)
        return
