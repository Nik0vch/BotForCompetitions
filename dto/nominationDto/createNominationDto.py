from pydantic import BaseModel
from typing import List
from model import Nomination

class NominationSchema(BaseModel):
    id: int
    name: str

class CreateNominationsRequestSchema(BaseModel):
    names: List[str]

class CreateNominationsResponseSchema(BaseModel):
    data: List[NominationSchema]


class NominationDto:    
    id: int
    name: str

    def __init__(self, nomination: Nomination):
        self.id = nomination.id
        self.name = nomination.name

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name
        }

class CreateNominationsResponseDto:
    data: list[NominationDto]

    def __init__(self, nominations: list[Nomination]):
        self.data = [NominationDto(nomination) for nomination in nominations]

    def to_dict(self):
        return {
            "data": self.data
        }
