import unittest
from aiounittest import async_test
from sqlalchemy import delete, select

from src.domain_logic.blog_domain import BlogDomain
from src.domain_logic.engagement_domain import EngagementDomain
from src.domain_logic.user_domain import UserDomain
from src.model.blog import Blog
from src.model.engagement import Engagement
from src.tests import create_all_tables, drop_all_tables, get_test_database_session
from src.usecases.insert.insert_blog import insert_blog
from src.usecases.insert.insert_engagement import insert_engagement
from src.usecases.insert.insert_user import insert_user


class DeleteBlogTestCase(unittest.TestCase):

    @async_test
    async def test_deleting_blog_deletes_engagement(self):
        await create_all_tables()

        user_data = {"username": "Mako",
                     "email": "mako@mako_mail.com",
                     "password": "Zu(|<erBerG"
                     }
        user_domain = UserDomain(**user_data)
        await insert_user(user_domain=user_domain, db_session_getter=get_test_database_session)

        blog_data = {
            "title": "Async capabilities",
            "body": "With async we can write apis that scale",
            "user_id": 1
        }
        blog_domain = BlogDomain(**blog_data)
        await insert_blog(blog_domain=blog_domain, db_session=get_test_database_session)

        engagement_data = {"blog_id": 1, "user_id": 1, "isLiked": True}
        engagement_domain = EngagementDomain(**engagement_data)
        await insert_engagement(engagement_domain=engagement_domain,
                                db_session_getter=get_test_database_session)



        await drop_all_tables()
