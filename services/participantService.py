from sqlalchemy.ext.asyncio import AsyncSession
from repository import participantRepository

async def CreateUser(db: AsyncSession, name: str, chatId: int):
    await participantRepository.CreateUser(db, name, chatId)