from fastapi import FastAPI
from app.api.v1 import singer
from app.db.base import Base
from app.db.session import engine

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Singers Api")

app.include_router(singer.router)