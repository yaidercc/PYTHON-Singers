from sqlalchemy import create_engine;
from sqlalchemy.orm import sessionmaker;

DATABASE_URL = "sqlite:///./singers.db"

# Engine to connect to the database
engine = create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False }
)

# autocommit=False -> avoid saving changes automatically
# autoflush=False -> avoid sending pending data to database (drafts)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()