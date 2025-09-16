from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.singer import SingerCreate, SingerUpdate, SingerOut
from app.services.singer import get_all
from app.db.session import get_db

router = APIRouter(prefix="/singers", tags=["Singers"])

@router.get("/", response_model=List[SingerOut])
def getAllSingers(db: Session = Depends(get_db)):
    return get_all(db)