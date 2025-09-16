from sqlalchemy import Column, Integer, String
from app.db.base import Base

class Singer(Base):
    __tablename__= "singers"

    id= Column(Integer, primary_key=True, index=True)
    name= Column(String, nullable=False)
    age = Column(String, nullable=False)
    genre = Column(String, nullable=False)