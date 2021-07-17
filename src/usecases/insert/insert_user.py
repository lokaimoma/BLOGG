from typing import Callable
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy import func
from src.model import get_database_session
from src.domain_logic.user_domain import UserDomain
from src.model.user import User
from . import UserInsert


async def insert_user(user_domain: UserDomain,
                      db_session_getter: Callable[[], AsyncSession] = get_database_session) -> UserInsert:
    async with db_session_getter() as session:
        is_user_registered = await __check_if_user_exist(session=session,
                                                         email=user_domain.email,
                                                         username=user_domain.username)

        if not is_user_registered:
            user = User(user_domain=user_domain)
            session.add(user)
            await session.commit()

        return UserInsert(not is_user_registered, user)


async def __check_if_user_exist(session: AsyncSession,
                                email: str, username: str) -> bool:
    query_username_exists = select(func.count(User.id)).filter(
        User.username == username)
    query_email_exists = select(func.count(User.id)).filter(User.email == email)
    username_exists = await session.execute(query_username_exists)
    email_exists = await session.execute(query_email_exists)
    if username_exists.scalar() == 1:
        return True

    if email_exists.scalar() == 1:
        return True

    return False
