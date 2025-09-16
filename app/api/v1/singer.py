from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.singer import SingerCreate, SingerUpdate, SingerOut
from app.services.singer import get_all, get_by_id,create
from app.db.session import get_db

router = APIRouter(prefix="/singers", tags=["Singers"])

@router.get("/", response_model=List[SingerOut])
def getAllSingers(db: Session = Depends(get_db)):
    return get_all(db)


@router.get("/{singer_id}", response_model=SingerOut)
def getSinger(singer_id:int,db: Session = Depends(get_db)):
    singer = get_by_id(db,singer_id)
    if not singer:
        raise HTTPException(status_code=404, detail="Singer not found")
    return singer

@router.post("/", response_model=SingerOut)
def createSinger(singer: SingerCreate, db: Session = Depends(get_db)):
    return create(db,singer)
