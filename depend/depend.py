from database import AsyncSessionLocal
from sqlalchemy.ext.asyncio import AsyncSession
from typing import AsyncGenerator

async def GetDbSession() -> AsyncGenerator[AsyncSession, None]:
    db = AsyncSessionLocal()  # Создание новой сессии
    try:
        yield db  # Возврат сессии для использования
    finally:
        await db.close()  # Закрытие сессии после использования