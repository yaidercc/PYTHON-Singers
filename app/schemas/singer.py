from pydantic import BaseModel, Field, validator
from typing import Optional

class SingerBase(BaseModel):
    name: str
    age: int
    genre: str
    
    @validator("genre")
    def normalize_genre(cls, v):
        return v.strip().lower()

class SingerCreate(SingerBase):
    name: str = Field(..., min_length=1)
    age: int = Field(..., gt=0)  
    genre: str = Field(..., min_length=3)

class SingerUpdate(SingerBase):
    name: Optional[str] = Field(None, min_length=1)
    age: Optional[int] = Field(None, gt=0)
    genre: Optional[str] = Field(None, min_length=3)


# Schema para los endpoints GET /responses
class SingerOut(SingerBase):
    id: int

    class Config:
        orm_mode = True
