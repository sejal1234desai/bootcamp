from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from pydantic import ValidationError
from define_user_model import User, UserSchema

engine = create_engine("sqlite:///example.db")
Session = sessionmaker(bind=engine)
session = Session()

# Example user input
data = {"name": "sejal", "email": "sejaldesai@gmail.com"}

try:
    validated_user = UserSchema(**data)
    new_user = User(name=validated_user.name, email=validated_user.email)
    session.add(new_user)
    session.commit()
    print("User inserted successfully.")
except ValidationError as e:
    print("Validation failed:", e)
