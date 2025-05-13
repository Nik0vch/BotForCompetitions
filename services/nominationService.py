from sqlalchemy.ext.asyncio import AsyncSession
from repository import nominationRepository

async def CreateNominations(db: AsyncSession, names: list[str]):
    return await nominationRepository.CreateNominations(db, names)