import unittest
from aiounittest import async_test
from sqlalchemy import select
from src.tests import get_test_database_session
from src.tests import create_all_tables
from src.tests import drop_all_tables
from src.domain_logic.user_domain import UserDomain
from src.domain_logic.blog_domain import BlogDomain
from src.domain_logic.engagement_domain import EngagementDomain
from src.usecases.insert.insert_user import insert_user
from src.usecases.insert.insert_blog import insert_blog
from src.usecases.insert.insert_engagement import insertEngagement
from src.model.engagement import Engagement


class InsertEngament(unittest.TestCase):
    @async_test
    async def test_insert_engagment(self):
        await create_all_tables()
        # insert user, id needed to create blog
        user_data = {"username": "Mako",
                     "email": "mako@mako_mail.com",
                     "password": "Zu(|<erBerG"
                     }
        user_domain = UserDomain(**user_data)
        await insert_user(userDomain=user_domain, func=get_test_database_session)

        # create blog
        # user id will always be 1
        blog_data = {
            "title": "Async capabilities",
            "body": "With async we can write apis that scale",
            "user_id": 1
        }
        blog_domain = BlogDomain(**blog_data)
        await insert_blog(blogDomain=blog_domain, func=get_test_database_session)

        engagement_data = {"blog_id": 1, "user_id": 1, "isLiked": True}
        engagement_domain = EngagementDomain(**engagement_data)
        await insertEngagement(engagementDomain=engagement_domain,
                               func=get_test_database_session)

        query = select(Engagement).filter(Engagement.id == 1)
        session = get_test_database_session()

        result = await session.execute(query)
        engament: Engagement = result.scalar_one_or_none()
        await session.close()
        self.assertIsNotNone(engament)
        self.assertTrue(engament.isLiked)

        await drop_all_tables()
