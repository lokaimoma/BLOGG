import asyncio
import unittest
from aiounittest import async_test
from . import get_test_database_session
from . import create_all_tables
from . import drop_all_tables
from src.domain_logic.user_domain import UserDomain
from src.usecases.insert_user import insert_user


class InsertUser(unittest.TestCase):
    @async_test
    async def setUp(self):
        super(InsertUser, self).setUp()
        self.session = get_test_database_session()
        await create_all_tables()

    @async_test
    async def tearDown(self):
        super(InsertUser, self).tearDown()
        await drop_all_tables()

    @async_test
    async def test_insert_user(self):
        user_data = {"username": "Mako",
                     "email": "mako@mako_mail.com",
                     "password": "Zu(|<erBerG"
                     }
        user_domain = UserDomain(**user_data)
        result = await insert_user(userDomain=user_domain, func=get_test_database_session)
        self.assertTrue(result)

    # @async_test
    # async def test_insert_duplicate_user(self):
    #     user_data = {"username": "Mako",
    #                  "email": "mako@mako_mail.com",
    #                  "password": "Zu(|<erBerG"
    #                  }
    #     user_domain = UserDomain(**user_data)
    #     result = await insert_user(userDomain=user_domain, func=get_test_database_session)
    #     user_data = {"username": "Mako",
    #                  "email": "mako@mako_mail.com",
    #                  "password": "Zu(|<erBerG"
    #                  }


if __name__ == "__main__":
    unittest.main(verbosity=2)
