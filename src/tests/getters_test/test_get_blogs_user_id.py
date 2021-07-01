import unittest
from aiounittest import async_test

from src.domain_logic.blog_domain import BlogDomain
from src.domain_logic.user_domain import UserDomain
from src.tests import create_all_tables, drop_all_tables, get_test_database_session
from src.usecases.getters.get_blogs_by_user_id import get_blogs_by_user_id
from src.usecases.insert.insert_blog import insert_blog
from src.usecases.insert.insert_user import insert_user


class GetBlogsByUserIdTestCase(unittest.TestCase):

    @async_test
    async def test_get_blogs_by_user_id(self):
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

        blog_data1 = {
            "title": "Python Language",
            "body": "The python language though not the fastest, is one of the fastes is "
                    "one of the coolest languages you can learn.",
            "user_id": 1
        }
        blog_domain1 = BlogDomain(**blog_data1)
        await insert_blog(blogDomain=blog_domain1, func=get_test_database_session)

        blog_data2 = {
            "title": "Python And Kotlin",
            "body": "Python and Kotlin all have some things in common. And I do love"
                    " using them both",
            "user_id": 1
        }
        blog_domain2 = BlogDomain(**blog_data2)
        await insert_blog(blogDomain=blog_domain2, func=get_test_database_session)

        blog_list = await get_blogs_by_user_id(user_id=1, func=get_test_database_session)

        self.assertIsNotNone(blog_list)
        self.assertEqual(len(blog_list), 3)

        await drop_all_tables()
