from typing import Callable

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.model import get_database_session
from src.model.user import User
from src.util.security.password_util import verify_password_hash


async def login_user(email: str, password: str,
                     func: Callable[[], AsyncSession] = get_database_session):
    query = select(User).filter(User.email == email)
    async with func() as session:
        result = await session.execute(query)
        user = result.scalar_one_or_none()
        if not user:
            return False
        password_match = verify_password_hash(password=password, password_hash=user.password)
        if not password_match:
            return False
        return user
