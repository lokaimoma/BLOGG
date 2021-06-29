from typing import Callable
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy import func
from src.model import get_database_session
from src.domain_logic.user_domain import UserDomain
from src.model.user import User


async def insert_user(userDomain: UserDomain, func: Callable[[], AsyncSession] = get_database_session) -> bool:
    async with func() as session:
        isUserRegistered = await __check_if_user_exist(session=session, email=userDomain.email, username=userDomain.username)

        if not isUserRegistered:
            user = User(userDomain=userDomain)
            session.add(user)
            await session.commit()

        return (not isUserRegistered)


async def __check_if_user_exist(session: AsyncSession,
                                email: str, username: str) -> bool:
    queryUsernameExists = select(func.count(User.id)).filter(
        User.username == username)
    queryEmailExists = select(func.count(User.id)).filter(User.email == email)
    usernameExists = await session.execute(queryUsernameExists)
    emailExists = await session.execute(queryEmailExists)
    if usernameExists.scalar() == 1:
        return True

    if emailExists.scalar() == 1:
        return True

    return False
