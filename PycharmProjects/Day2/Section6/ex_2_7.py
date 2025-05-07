#7# Operation: Export to Dict and JSON

from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int

user = User(name="Sejal", age=22)

# Convert to dictionary
user_dict = user.dict()
print("Dict:", user_dict)
# Output: Dict: {'name': 'Sejal', 'age': 22}

# Convert to JSON
user_json = user.json()
print("JSON:", user_json)
# Output: JSON: {"name": "Sejal", "age": 22}
