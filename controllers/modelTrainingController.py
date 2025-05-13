from . import router
from dto.modelTrainingDto.modelTrainingCityDto import ModelTrainingCityRequest
from neural import spacyModel

@router.post("/training", tags=["Training"])
async def Train():
    spacyModel.LoadTrainData()
    return
