from typing import Callable
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy import func
from src.model import get_database_session
from src.domain_logic.user_domain import UserDomain
from src.model.user import User


async def insert_user(userDomain: UserDomain, func = get_database_session) -> bool:
    async with func() as session:
        isUserRegistered = await __check_if_user_exist(session=session, email=userDomain.email, username=userDomain.username)

        if not isUserRegistered:
            user = User(userDomain=userDomain)
            session.add(user)
            await session.commit()

        return (not isUserRegistered)


async def __check_if_user_exist(session: AsyncSession,
                                email: str, username: str) -> bool:
    query = select(func.count(User.id)).filter(
        User.username == username, User.email == email)
    result = await session.execute(query)
    result = result.scalar()
    return (result == 1)
