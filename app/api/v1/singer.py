from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.singer import SingerCreate, SingerUpdate, SingerOut
from app.services.singer import get_all,create,get_by_id,update, delete
from app.db.session import get_db

router = APIRouter(prefix="/singers", tags=["Singers"])
