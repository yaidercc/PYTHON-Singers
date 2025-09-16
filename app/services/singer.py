from sqlalchemy.orm import Session
from app.models.singer import Singer
from app.schemas.singer import SingerCreate, SingerUpdate

def get_all(db: Session):
    return db.query(Singer).all()
