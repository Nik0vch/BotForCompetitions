from os import getenv
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = f"postgresql+asyncpg://{getenv("DB_USER")}:{getenv("DB_PASS")}@localhost:5432/{getenv("DB_NAME")}"

engine = create_async_engine(DATABASE_URL, echo=True)
AsyncSessionLocal = sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)

Base = declarative_base()

async def Db_Connect():
    from model import TABLES_FOR_AUTOCREATION #Для автоматического создания таблиц их всех необходимо импортировать
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

async def Db_Disconnect():
    await engine.dispose()