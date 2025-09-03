from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from . import schemas, services
from .database import SessionLocal

router = APIRouter()

# Dependency for DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/person/", response_model=schemas.PersonRead)
def add_person(person: schemas.PersonCreate, db: Session = Depends(get_db)):
    return services.create_person(db, person)

@router.get("/persons/", response_model=List[schemas.PersonRead])
def read_all_persons(db: Session = Depends(get_db)):
    return services.get_all_persons(db)

@router.get("/person/{person_id}", response_model=schemas.PersonRead)
def read_person(person_id: int, db: Session = Depends(get_db)):
    person = services.get_person(db, person_id)
    if not person:
        raise HTTPException(status_code=404, detail="Person not found")
    return person

@router.put("/person/{person_id}", response_model=schemas.PersonRead)
def update_person_route(person_id: int, update: schemas.PersonUpdate, db: Session = Depends(get_db)):
    person = services.update_person(db, person_id, update)
    if not person:
        raise HTTPException(status_code=404, detail="Person not found")
    return person

@router.delete("/person/{person_id}")
def delete_person_route(person_id: int, db: Session = Depends(get_db)):
    person = services.delete_person(db, person_id)
    if not person:
        raise HTTPException(status_code=404, detail="Person not found")
    return {"message": f"Person {person_id} deleted successfully"}
