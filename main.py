# main.py
import os
from typing import List, Optional

from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel, EmailStr
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker, Session
from dotenv import load_dotenv

# 1. Load environment variables
load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")
DATABASE_URL = "postgresql+psycopg://person_user:Sonakpr%40123@localhost:5432/persondb"


# 2. SQLAlchemy setup
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
Base = declarative_base()

# 3. Database model
class PersonORM(Base):
    __tablename__ = "persons"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    email = Column(String, unique=True, nullable=False)

# Create the table if it doesn’t exist
Base.metadata.create_all(bind=engine)

# 4. Pydantic models
class PersonCreate(BaseModel):
    name: str
    age: int
    email: EmailStr

class PersonRead(BaseModel):
    id: int
    name: str
    age: int
    email: EmailStr

    class Config:
        orm_mode = True

class PersonUpdate(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    email: Optional[EmailStr] = None

# 5. FastAPI app
app = FastAPI(title="Person CRUD API", version="1.0")

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Create
@app.post("/person/", response_model=PersonRead)
def add_person(person: PersonCreate, db: Session = Depends(get_db)):
    new_person = PersonORM(**person.dict())
    db.add(new_person)
    db.commit()
    db.refresh(new_person)
    return new_person

# Read all
@app.get("/persons/", response_model=List[PersonRead])
def get_all_persons(db: Session = Depends(get_db)):
    return db.query(PersonORM).all()

# Read one
@app.get("/person/{person_id}", response_model=PersonRead)
def get_person(person_id: int, db: Session = Depends(get_db)):
    person = db.get(PersonORM, person_id)
    if not person:
        raise HTTPException(status_code=404, detail="Person not found")
    return person

# Update
@app.put("/person/{person_id}", response_model=PersonRead)
def update_person(person_id: int, update: PersonUpdate, db: Session = Depends(get_db)):
    person = db.get(PersonORM, person_id)
    if not person:
        raise HTTPException(status_code=404, detail="Person not found")

    for key, value in update.dict(exclude_unset=True).items():
        setattr(person, key, value)

    db.commit()
    db.refresh(person)
    return person

# Delete
@app.delete("/person/{person_id}")
def delete_person(person_id: int, db: Session = Depends(get_db)):
    person = db.get(PersonORM, person_id)
    if not person:
        raise HTTPException(status_code=404, detail="Person not found")
    db.delete(person)
    db.commit()
    return {"message": f"Person {person_id} deleted successfully"}
