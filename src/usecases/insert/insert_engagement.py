from typing import Callable
from sqlalchemy import select
from sqlalchemy import func
from sqlalchemy.ext.asyncio import AsyncSession
from src.model import get_database_session
from src.domain_logic.engagement_domain import EngagementDomain
from src.model.engagement import Engagement
from src.usecases.update.update_engagement import update_engagement


async def insert_engagement(engagement_domain: EngagementDomain,
                            db_session_getter: Callable[[], AsyncSession] = get_database_session):
    async with db_session_getter() as session:
        engagement_exists = await __check_engagement_exists(session=session,
                                                            blog_id=engagement_domain.blog_id,
                                                            user_id=engagement_domain.user_id)

        if engagement_exists:
            await update_engagement(engagement_domain=engagement_domain)
            return

        engagement = Engagement(engagement_domain=engagement_domain)
        session.add(engagement)
        await session.commit()


async def __check_engagement_exists(session: AsyncSession, blog_id: int, user_id: int) -> bool:
    query = select(func.count(Engagement.id)).filter(
        Engagement.blog_id == blog_id, Engagement.user_id == user_id)

    result = await session.execute(query)
    result = result.scalar()
    return result == 1
