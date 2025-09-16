from pydantic import BaseModel

class SingerBase(BaseModel):
    nombre: str
    edad: int
    genero: str
    

class SingerCreate(SingerBase):
    pass

class SingerUpdate(SingerBase):
    pass

# This schema is for the get endpoints
class SingerOut(SingerBase):
    id: int

    # parse an object from SQLAlchemy to a dictionary
    class Config:
        orm_mode = True