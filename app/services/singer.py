from sqlalchemy.orm import Session
from app.models.singer import Singer
from app.schemas.singer import SingerCreate, SingerUpdate

def get_all(db: Session):
    return db.query(Singer).all()

def get_by_id(db: Session, singer_id: int):
    return db.query(Singer).filter(Singer.id==singer_id).first()

def create(db: Session, singer: SingerCreate):
    newSinger = Singer(**singer.dict())
    db.add(newSinger)
    db.commit()
    db.refresh(newSinger)
    
    return newSinger

def update(db:Session, singer_id: int ,data: SingerUpdate):
    singer = get_by_id(db, singer_id)
    if singer:
        for key, value in data.dict().items():
            setattr(singer, key, value)
        db.commit()
        db.refresh(singer)
    return singer

def delete(db: Session, singer_id: int):
    singer = get_by_id(db, singer_id)
    if singer:
        db.delete(singer)
        db.commit()
    return singer
