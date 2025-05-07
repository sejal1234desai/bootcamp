#2# Operation: Catch Validation Error

from pydantic import BaseModel, ValidationError

class User(BaseModel):
    name: str
    age: int

# Trying to pass a string as age
data = {"name": "Bob", "age": "not a number"}

try:
    user = User(**data)
except ValidationError as e:
    print("Validation Error:", e)
# Output: Validation Error: 1 validation error for User
# age
#   value is not a valid integer (type=type_error.integer)
