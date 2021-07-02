from typing import Callable

from sqlalchemy import select, func
from sqlalchemy.ext.asyncio import AsyncSession
from src.model import get_database_session
from src.domain_logic.blog_domain import BlogDomain
from src.model.blog import Blog
from src.model.user import User


async def insert_blog(blog_domain: BlogDomain,
                      db_session: Callable[[], AsyncSession] = get_database_session) -> bool:
    blog = Blog(blog_domain=blog_domain)
    async with db_session() as session:
        user_exists = await __check_user_exists(user_id=blog_domain.user_id, session=session)
        if user_exists:
            session.add(blog)
            await session.commit()

        return user_exists


async def __check_user_exists(user_id: int, session: AsyncSession) -> bool:
    query = select(func.Count(User.id)).filter(User.id == user_id)
    result = await session.execute(query)
    user_exists = result.scalar()
    return user_exists == 1
