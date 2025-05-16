#
# Operation: Automatic Type Conversion

from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int

# Automatic conversion from string "42" to int
data = {"name": "Sejal", "age": "42"}
user = User(**data)
print(user)
# Output: name='Sejal' age=42
