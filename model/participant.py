from sqlalchemy import Column, Integer, String
from database import Base
from sqlalchemy.orm import relationship

class Participant(Base):
    __tablename__ = "participants"

    id = Column(Integer, primary_key=True, index=True)
    nikName = Column(String, index=True)
    chatId = Column(Integer, unique=True, index=True)

    answers = relationship("Answer", back_populates="participant")