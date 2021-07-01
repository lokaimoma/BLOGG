import unittest
from aiounittest import async_test

from src.domain_logic.blog_domain import BlogDomain
from src.domain_logic.engagement_domain import EngagementDomain
from src.domain_logic.user_domain import UserDomain
from src.tests import create_all_tables, drop_all_tables, get_test_database_session
from src.usecases.getters.get_blog_details import get_blog_details
from src.usecases.insert.insert_blog import insert_blog
from src.usecases.insert.insert_engagement import insertEngagement
from src.usecases.insert.insert_user import insert_user


class GetBlogDetailTestCase(unittest.TestCase):

    @async_test
    async def test_get_blog__detail_current_user_id_none(self):
        await create_all_tables()

        user_data = {"username": "Mako",
                     "email": "mako@mako_mail.com",
                     "password": "Zu(|<erBerG"
                     }
        user_domain = UserDomain(**user_data)
        await insert_user(userDomain=user_domain, func=get_test_database_session)

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

        blog_domain_detail = await get_blog_details(blog_id=1, func=get_test_database_session)

        self.assertIsNotNone(blog_domain_detail)
        self.assertIsNone(blog_domain_detail.current_user_likes)
        self.assertEqual(blog_domain_detail.blog.title, blog_data["title"])
        await drop_all_tables()

    @async_test
    async def test_get_blog__detail_current_user_id_present(self):
        await create_all_tables()

        user_data = {"username": "Mako",
                     "email": "mako@mako_mail.com",
                     "password": "Zu(|<erBerG"
                     }
        user_domain = UserDomain(**user_data)
        await insert_user(userDomain=user_domain, func=get_test_database_session)

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

        blog_domain_detail = await get_blog_details(blog_id=1, current_user_id=1,
                                                    func=get_test_database_session)

        self.assertIsNotNone(blog_domain_detail)
        self.assertIsNotNone(blog_domain_detail.current_user_likes)
        self.assertTrue(blog_domain_detail.current_user_likes)
        self.assertEqual(blog_domain_detail.blog.title, blog_data["title"])
        await drop_all_tables()
