from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError
from user_post_model import User

engine = create_engine("sqlite:///example.db")
SessionLocal = sessionmaker(bind=engine)
session = SessionLocal()

users = [
    User(name="Alice", email="alice@example.com"),
    User(name="Bob", email="bob@example.com"),
    User(name="Charlie", email="charlie@example.com")
]

try:
    session.begin()
    session.add_all(users)
    session.commit()
    print("All users inserted successfully.")
except SQLAlchemyError as e:
    session.rollback()
    print("Transaction failed, rolled back:", str(e))
finally:
    session.close()
