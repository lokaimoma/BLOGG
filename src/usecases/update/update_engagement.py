from sqlalchemy import select

from src.domain_logic.engagement_domain import EngagementDomain
from src.model import get_database_session
from src.model.engagement import Engagement


async def update_engagement(engagement_domain: EngagementDomain):
    async with get_database_session() as session:
        query = select(Engagement).filter(Engagement.blog_id ==
                                          engagement_domain.blog_id, Engagement.user_id == engagement_domain.user_id)
        result = await session.execute(query)
        # Crash In Case Of None
        engagement: Engagement = result.scalar_one()
        engagement.isDisLiked = engagement_domain.isDisliked
        engagement.isLiked = engagement.isLiked
        await session.commit()
