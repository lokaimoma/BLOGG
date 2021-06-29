from src.model import get_database_session
from src.domain_logic.blog_domain import BlogDomain
from src.model.blog import Blog


async def insert_blog(blogDomain: BlogDomain):
    blog = Blog(blogDomain=blogDomain)
    async with get_database_session() as session:
        session.add(blog)
        await session.commit()