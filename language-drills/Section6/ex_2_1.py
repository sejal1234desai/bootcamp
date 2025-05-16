## Operation: Basic Model Definition and Parsing from Dict

from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int

# Parse a dict into a User object
data = {"name": "Sejal", "age": 22}
user = User(**data)
print(user)
# Output: name='Sejal' age=22
