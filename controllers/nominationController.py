from . import router
from services import nominationService
from dto.nominationDto import *
from depend import *
from sqlalchemy.ext.asyncio import AsyncSession


@router.post("/nominations", tags=["Nomination"], response_model=CreateNominationsResponseSchema)
async def CreateNominations(request: CreateNominationsRequestSchema, db: AsyncSession = Depends(GetDbSession)):
    nominations = await nominationService.CreateNominations(db, request.names)
    return CreateNominationsResponseDto(nominations)