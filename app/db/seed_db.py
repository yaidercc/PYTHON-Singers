from app.db.session import SessionLocal, engine
from app.db.base import Base
from app.models.singer import Singer

def seed():
    db = SessionLocal()
    try:
        Base.metadata.create_all(bind=engine)

        singers = [
            Singer(name="Shakira", age=46, genre="pop"),
            Singer(name="The Weeknd", age=35, genre="pop"),
            Singer(name="Michael Jackson", age=50, genre="pop"),
            Singer(name="Adele", age=37, genre="soul"),
            Singer(name="Eminem", age=52, genre="hiphop"),
        ]

        if db.query(Singer).count() == 0:
            db.add_all(singers)
            db.commit()
            print("Database seeded ")
        else:
            print("Database already has data")
    finally:
        db.close()

if __name__ == "__main__":
    seed()
