from sqlalchemy import Column, Integer, String
from .database import Base

class PersonORM(Base):
    __tablename__ = "persons"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    email = Column(String, unique=True, nullable=False)
