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