from sqlalchemy import Column, Integer, String
from app.db.base import Base

class Singer(Base):
    __tablename__= "singers"

    id= Column(Integer, primary_key=True, index=True)
    nombre= Column(String, nullable=False)
    edad = Column(String, nullable=False)
    genero = Column(String, nullable=False)