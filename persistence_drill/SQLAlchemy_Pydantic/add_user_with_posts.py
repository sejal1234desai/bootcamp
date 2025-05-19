from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, User, Post

engine = create_engine("sqlite:///example.db")
Session = sessionmaker(bind=engine)
session = Session()

Base.metadata.create_all(engine)

# Create a user
user = User(name="Saurabh", email="SaurabhBharade@gmail.com")
session.add(user)
session.commit()

# Add posts for this user
post1 = Post(title="First Post", content="This is my first post.", user_id=user.id)
post2 = Post(title="Second Post", content="This is my second post.", user_id=user.id)

session.add_all([post1, post2])
session.commit()

print(f"User and posts added with user_id = {user.id}")
