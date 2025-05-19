from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from define_user_model import User, UserSchema

engine = create_engine("sqlite:///example.db")
Session = sessionmaker(bind=engine)
session = Session()

users = session.query(User).all()
result = [UserSchema(name=u.name, email=u.email).model_dump() for u in users]

print(result)
