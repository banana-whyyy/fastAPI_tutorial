# Подключение к базе данных и создание асинхронных сессий
from .models import Base, Book, Author, User
from .config import settings
from collections.abc import AsyncGenerator
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine, AsyncSession
from fastapi import Depends
from fastapi_users.db import SQLAlchemyUserDatabase


DATABASE_URL = (
    f"postgresql+asyncpg://{settings.db_user}:"
    f"{settings.db_password}@{settings.db_host}:"
    f"{settings.db_port}/{settings.db_name}"
)

engine = create_async_engine(DATABASE_URL)
async_session_maker = async_sessionmaker(engine, expire_on_commit=False)


async def create_db_and_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

async def get_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session

async def get_user_db(session: AsyncSession = Depends(get_session)):
    yield SQLAlchemyUserDatabase(session, User)
