from sqlalchemy import Column, Integer, String, ForeignKey
from database import Base
from sqlalchemy.orm import relationship

class Participant(Base):
    __tablename__ = "participants"

    id = Column(Integer, primary_key=True, index=True)
    nikName = Column(String, index=True)
    chatId = Column(Integer, unique=True, index=True)
    nominationId = Column(Integer, ForeignKey('nominations.id'), index=True)

    answers = relationship("Answer", back_populates="participant")
    nomination = relationship("Nomination", back_populates="participants", uselist=False)