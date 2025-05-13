from sqlalchemy.ext.asyncio import AsyncSession
from model.nomination import Nomination

async def CreateNomination(db: AsyncSession, name: str) -> Nomination:
    newNomination = Nomination(name=name)
    db.add(newNomination)
    await db.commit()
    await db.refresh(newNomination)
    return newNomination

async def CreateNominations(db: AsyncSession, names: list[str]) -> list[Nomination]:
    nominations = [Nomination(name=name) for name in names]
    db.add_all(nominations)
    await db.commit()
    for nomination in nominations:
        await db.refresh(nomination)
    return nominations