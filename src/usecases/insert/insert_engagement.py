from typing import Callable
from sqlalchemy import select
from sqlalchemy import func
from sqlalchemy.ext.asyncio import AsyncSession
from src.model import get_database_session
from src.domain_logic.engagement_domain import EngagementDomain
from src.model.engagement import Engagement
from src.usecases.update.update_engagement import update_engagement


async def insertEngagement(engagementDomain: EngagementDomain, func: Callable[[], AsyncSession] = get_database_session):
    async with func() as session:
        engagementExists = await __checkEngagementExists(session=session,
                                                         blog_id=engagementDomain.blog_id,
                                                         user_id=engagementDomain.user_id)

        if engagementExists:
            await update_engagement(engagement_domain=engagementDomain)
            return

        engagement = Engagement(engagementDomain=engagementDomain)
        session.add(engagement)
        await session.commit()


async def __checkEngagementExists(session: AsyncSession, blog_id: int, user_id: int) -> bool:
    query = select(func.count(Engagement.id)).filter(
        Engagement.blog_id == blog_id, Engagement.user_id == user_id)

    result = await session.execute(query)
    result = result.scalar()
    return result == 1

