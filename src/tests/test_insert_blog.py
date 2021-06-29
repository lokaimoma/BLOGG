import unittest
from sqlalchemy import select
from aiounittest import async_test
from . import get_test_database_session
from . import create_all_tables
from . import drop_all_tables
from src.domain_logic.user_domain import UserDomain
from src.domain_logic.blog_domain import BlogDomain
from src.usecases.insert_user import insert_user
from src.usecases.insert_blog import insert_blog
from src.model.blog import Blog


class InsertBlog(unittest.TestCase):

    @async_test
    async def test_insert_blog(self):
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

        query = select(Blog).filter(Blog.id == 1)
        session = get_test_database_session()
        result = await session.execute(query)
        blog: Blog = result.scalar_one_or_none()

        self.assertIsNotNone(blog)
        self.assertEqual(blog.title, "Async capabilities")
        self.assertEqual(blog.body, "With async we can write apis that scale")
        await drop_all_tables()


if __name__ == "__main__":
    unittest.main()
