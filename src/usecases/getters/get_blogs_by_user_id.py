from typing import Optional, List

from sqlalchemy import select

from src.model import get_database_session
from src.model.blog import Blog


async def get_blogs_by_user_id(blog_id: int) -> Optional[List[Blog]]:
    query = select(Blog).filter(Blog.id == blog_id)
    async with get_database_session() as session:
        result = await session.execute(query).all()
        return result
