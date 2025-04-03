from sqlalchemy.ext.asyncio import AsyncSession
from model.participant import Participant

async def CreateUser(db: AsyncSession, name: str, chatId: int):
    newUser = Participant(name=name, chatId=chatId)
    db.add(newUser)
    await db.commit()
    await db.refresh(newUser)
    return newUser