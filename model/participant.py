from sqlalchemy import Column, Integer, String
from database import Base

class Participant(Base):
    __tablename__ = "participant"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    chatId = Column(Integer, unique=True, index=True)