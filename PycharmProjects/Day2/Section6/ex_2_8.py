#8
# Operation: Optional Field with Default Value

from pydantic import BaseModel
from typing import Optional

class User(BaseModel):
    name: str
    age: int
    country: Optional[str] = None

# This will succeed, with default country as None
data = {"name": "Sejal", "age": 22}
user = User(**data)
print(user)
# Output: name='Sejal' age=22 country=None

# This will also succeed, with a custom country
data = {"name": "Sejal", "age": 22, "country": "India"}
user = User(**data)
print(user)
# Output: name='Sejal' age=22 country='India'

