import unittest
from aiounittest import async_test

from src.domain_logic.blog_domain import BlogDomain
from src.domain_logic.user_domain import UserDomain
from src.tests import create_all_tables, drop_all_tables, get_test_database_session
from src.usecases.getters.get_all_blogs import get_all_blogs
from src.usecases.insert.insert_blog import insert_blog
from src.usecases.insert.insert_user import insert_user


class GeAllBlogsTestCase(unittest.TestCase):

    @async_test
    async def test_get_all_blogs(self):
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
        await insert_blog(blog_domain=blog_domain, func=get_test_database_session)

        blog_data1 = {
            "title": "Python Language",
            "body": "The python language though not the fastest, is one of the fastest is "
                    "one of the coolest languages you can learn.",
            "user_id": 1
        }
        blog_domain1 = BlogDomain(**blog_data1)
        await insert_blog(blog_domain=blog_domain1, func=get_test_database_session)

        blog_data2 = {
            "title": "Python And Kotlin",
            "body": "Python and Kotlin all have some things in common. And I do love"
                    " using them both",
            "user_id": 1
        }
        blog_domain2 = BlogDomain(**blog_data2)
        await insert_blog(blog_domain=blog_domain2, func=get_test_database_session)

        result = await get_all_blogs(func=get_test_database_session)

        self.assertIsNotNone(result)
        self.assertEqual(len(result), 3)
        self.assertEqual(result[2].title, blog_data2["title"])
        self.assertEqual(result[1].title, blog_data1["title"])

        await drop_all_tables()
