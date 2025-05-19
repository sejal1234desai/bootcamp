from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from define_user_model import User

engine = create_engine("sqlite:///example.db")
Session = sessionmaker(bind=engine)
session = Session()

email = "sejal2001new@gmail.com"
user = session.query(User).filter_by(email=email).first()

if user:
    session.delete(user)
    session.commit()
    print("User deleted.")
else:
    print("User not found.")
