from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from define_user_model import User

engine = create_engine("sqlite:///example.db")
Session = sessionmaker(bind=engine)
session = Session()

old_email = "sejaldesai@gmail.com"
new_email = "sejal2001new@gmail.com"

user = session.query(User).filter_by(email=old_email).first()
if user:
    user.email = new_email
    session.commit()
    print("Email updated.")
else:
    print("User not found.")
