import unittest
from aiounittest import async_test
from src.tests import get_test_database_session
from src.tests import create_all_tables
from src.tests import drop_all_tables
from src.domain_logic.user_domain import UserDomain
from src.usecases.insert.insert_user import insert_user


class InsertUser(unittest.TestCase):
    # Using setup and teardown functions was throwing exceptions
    # from aiounittest library. So had to create and drop tables
    # after each test.

    @async_test
    async def test_insert_user(self):
        await create_all_tables()
        user_data = {"username": "Mako",
                     "email": "mako@mako_mail.com",
                     "password": "Zu(|<erBerG"
                     }
        user_domain = UserDomain(**user_data)
        result = await insert_user(userDomain=user_domain, func=get_test_database_session)
        self.assertTrue(result)
        await drop_all_tables()

    @async_test
    async def test_insert_duplicate_email_user(self):
        await create_all_tables()
        user_data = {"username": "Mako",
                     "email": "mako@mako_mail.com",
                     "password": "Zu(|<erBerG"
                     }
        user_domain = UserDomain(**user_data)
        result = await insert_user(userDomain=user_domain, func=get_test_database_session)

        user_data = {"username": "Sam",
                     "email": "mako@mako_mail.com",
                     "password": "Zu(|<erBerG"
                     }

        user_domain = UserDomain(**user_data)
        result = await insert_user(userDomain=user_domain, func=get_test_database_session)
        self.assertFalse(result)
        await drop_all_tables()

    @async_test
    async def test_insert_duplicate_username_user(self):
        await create_all_tables()
        user_data = {"username": "Mako",
                     "email": "mako@mako_mail.com",
                     "password": "Zu(|<erBerG"
                     }
        user_domain = UserDomain(**user_data)
        result = await insert_user(userDomain=user_domain, func=get_test_database_session)

        user_data = {"username": "Mako",
                     "email": "mako@mako_mail1.com",
                     "password": "Zu(|<erBerG"
                     }

        user_domain = UserDomain(**user_data)
        result = await insert_user(userDomain=user_domain, func=get_test_database_session)
        self.assertFalse(result)
        await drop_all_tables()

    @async_test
    async def test_insert_duplicate__user(self):
        await create_all_tables()
        user_data = {"username": "Mako",
                     "email": "mako@mako_mail.com",
                     "password": "Zu(|<erBerG"
                     }
        user_domain = UserDomain(**user_data)
        result = await insert_user(userDomain=user_domain, func=get_test_database_session)

        user_data = {"username": "Mako",
                     "email": "mako@mako_mail.com",
                     "password": "Zu(|<erBerG"
                     }

        user_domain = UserDomain(**user_data)
        result = await insert_user(userDomain=user_domain, func=get_test_database_session)
        self.assertFalse(result)
        await drop_all_tables()


if __name__ == "__main__":
    unittest.main(verbosity=2)
