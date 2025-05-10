from . import router
from dto.modelTrainingDto.modelTrainingCityDto import ModelTrainingCityRequest
from services import spacyService

@router.post("/training/city", tags=["Training"])
async def TrainByCity(request: ModelTrainingCityRequest):
    spacyService.TrainingByCity(request.data)
    return

@router.post("/training/region", tags=["Training"])
async def TrainByRegion(request: ModelTrainingCityRequest):
    spacyService.TrainingByRegion(request.data)
    return

@router.post("/training/university", tags=["Training"])
async def TrainByUniversity(request: ModelTrainingCityRequest):
    spacyService.TrainingByUniversity(request.data)
    return

@router.post("/training/nomination", tags=["Training"])
async def TrainByNomination(request: ModelTrainingCityRequest):
    spacyService.TrainingByNominations(request.data)
    return

@router.post("/training", tags=["Training"])
async def Train():
    spacyService.LoadTrainData()
    return
