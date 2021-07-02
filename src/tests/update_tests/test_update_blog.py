import unittest
from aiounittest import async_test
from sqlalchemy import select

from src.domain_logic.blog_domain import BlogDomain
from src.domain_logic.user_domain import UserDomain
from src.model.blog import Blog
from src.tests import get_test_database_session, create_all_tables, drop_all_tables
from src.usecases.insert.insert_blog import insert_blog
from src.usecases.insert.insert_user import insert_user
from src.usecases.update.update_blog import update_blog


class UpdateBlogTestCase(unittest.TestCase):

    @async_test
    async def test_update_blog(self):
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

        updated_blog = {"title": "Wonders of async",
                        "body": "Scalablilty is a main factor for embracing "
                                "async into project now adays. Though there "
                                "are other interesting reasons why you would "
                                "want to use it.",
                        "user_id": 1
                        }
        updated_blog_domain = BlogDomain(**updated_blog)
        await update_blog(blog_id=1, blog_info=updated_blog_domain,
                          func=get_test_database_session)

        query = select(Blog).filter(Blog.id == 1)
        session = get_test_database_session()
        result = await session.execute(query)
        blog: Blog = result.scalar_one_or_none()
        await session.close()
        self.assertIsNotNone(blog)
        self.assertEqual(blog.title, updated_blog["title"])
        self.assertEqual(blog.body, updated_blog["body"])

        await drop_all_tables()


if __name__ == '__main__':
    unittest.main()
