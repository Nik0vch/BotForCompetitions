from sqlalchemy import Column, Integer, String
from database import Base
from sqlalchemy.orm import relationship

class Question(Base):
    __tablename__ = "questions"

    id = Column(Integer, primary_key=True, index=True)
    question = Column(String, index=True)
    columnName = Column(String, index=True)
    columnDescription = Column(String, index=True)
    
    answers = relationship("Answer", back_populates="questions")