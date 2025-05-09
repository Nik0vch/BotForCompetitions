from pydantic import BaseModel
from typing import List

class ModelTrainingCityRequest(BaseModel):
    data: List[str]
