import os
from typing import Optional
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker


SQLAlchemyBase = declarative_base()
__session_factory: Optional[sessionmaker] = None
# Crash In Case DATABASE_URL is not set in environmental variables
DATABASE_URL = os.environ["DATABASE_URL"]


def __create_engine():
    global __session_factory
    engine = create_async_engine(url=DATABASE_URL, echo=False)
    __session_factory = sessionmaker(
        bind=engine, class_=AsyncSession, expire_on_commit=False)


def get_database_session():
    global __session_factory
    if not __session_factory:
        __create_engine()

    return __session_factory()
