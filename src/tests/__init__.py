from typing import Optional
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.asyncio import AsyncEngine
from sqlalchemy.orm import sessionmaker
from src.model import SQLAlchemyBase


__test_session_factory: Optional[sessionmaker] = None
__engine: Optional[AsyncEngine] = None


def __create_test_engine():
    global __engine
    database_url = "sqlite+aiosqlite:///:memory:"
    __engine = create_async_engine(url=database_url, echo=False)

    global __test_session_factory
    __test_session_factory = sessionmaker(
        bind=__engine, expire_on_commit=False, class_=AsyncSession)


def get_test_database_session() -> AsyncSession:
    global __test_session_factory

    if not __test_session_factory:
        __create_test_engine()

    return __test_session_factory()


def create_all_tables():
    global __engine
    if not __engine:
        __create_test_engine()
    import src.model.__all_models
    SQLAlchemyBase.metadata.create_all(__engine)


def drop_all_tables():
    global __engine
    if not __engine:
        __create_test_engine()
    import src.model.__all_models
    SQLAlchemyBase.metadata.drop_all(__engine)
