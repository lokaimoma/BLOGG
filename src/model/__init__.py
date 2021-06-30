import os
from typing import Optional
import sqlalchemy as sa
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker


SQLAlchemyBase = declarative_base()
__session_factory: Optional[sessionmaker] = None
# Crash In Case DATABASE_URL is not set in environmental variables
DATABASE_URL = os.environ["DATABASE_URL"]


def __create_engine():
    """
        This function takes care of creating the engine
        for establishing the database connection.No need
        to call the function yourself.
    """
    global __session_factory
    engine = create_async_engine(url=DATABASE_URL, echo=False)
    __session_factory = sessionmaker(
        bind=engine, class_=AsyncSession, expire_on_commit=False)
    import src.model.__all_models
    global SQLAlchemyBase


def get_database_session() -> AsyncSession:
    """
        This function returns an AsyncSession
        object for performing asynchronous 
        database operations.
    """
    global __session_factory
    if not __session_factory:
        __create_engine()

    return __session_factory()
