from sqlalchemy import Column, Integer, String, ForeignKey
from database import Base
from sqlalchemy.orm import relationship

class Answer(Base):
    __tablename__ = "answers"

    id = Column(Integer, primary_key=True, index=True)
    participantId = Column(Integer, ForeignKey('participants.id'), index=True)
    questionId = Column(Integer, ForeignKey('questions.id'), index=True)
    answer = Column(String, index=True)

    participant = relationship("Participant", back_populates="answers")
    questions = relationship("Question", back_populates="answers")