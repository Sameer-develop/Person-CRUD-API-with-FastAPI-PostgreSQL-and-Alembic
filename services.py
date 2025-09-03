from sqlalchemy.orm import Session
from . import models, schemas

def create_person(db: Session, person: schemas.PersonCreate):
    new_person = models.PersonORM(**person.dict())
    db.add(new_person)
    db.commit()
    db.refresh(new_person)
    return new_person

def get_all_persons(db: Session):
    return db.query(models.PersonORM).all()

def get_person(db: Session, person_id: int):
    return db.get(models.PersonORM, person_id)

def update_person(db: Session, person_id: int, update: schemas.PersonUpdate):
    person = db.get(models.PersonORM, person_id)
    if not person:
        return None
    for key, value in update.dict(exclude_unset=True).items():
        setattr(person, key, value)
    db.commit()
    db.refresh(person)
    return person

def delete_person(db: Session, person_id: int):
    person = db.get(models.PersonORM, person_id)
    if not person:
        return None
    db.delete(person)
    db.commit()
    return person
