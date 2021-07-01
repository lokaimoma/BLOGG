from typing import Optional, Callable, List

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from src.domain_logic.blog_domain import BlogDomain
from src.domain_logic.blog_domain_detailed import BlogDomainDetail
from src.model import get_database_session
from src.model.blog import Blog
from src.model.engagement import Engagement


async def get_blog_details(blog_id: int, current_user_id: Optional[int] = None,
                           func: Callable[[], AsyncSession] = get_database_session) -> Optional[BlogDomainDetail]:
    query = select(Blog).options(selectinload(Blog.engagements)).filter(Blog.id == blog_id)
    async with func() as session:
        result = await session.execute(query)
        blog = result.scalar_one_or_none()

        if not blog:
            return blog

        blog_domain_data = {
            "title": blog.title,
            "body": blog.body,
            "created_date": blog.created_date,
            "last_updated": blog.last_updated,
            "user_id": blog.user_id
        }
        engagements: List[Engagement] = blog.engagements
        likes_count = len([engagement for engagement in engagements if engagement.isLiked])
        if current_user_id:
            current_user_like_status = [engagement for engagement in engagements if engagement.user_id == current_user_id]
            current_user_like_status = current_user_like_status[0].isLiked
        blog_detail_domain_data = {
            "blog": blog_domain_data,
            "likes_count": likes_count,
            "dislikes_count": len(engagements) - likes_count,
            "current_user_likes": current_user_like_status if current_user_id else None
        }
        blog_detail = BlogDomainDetail(**blog_detail_domain_data)
        return blog_detail
