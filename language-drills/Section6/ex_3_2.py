## Operation: Field Aliases for Mapping JSON keys

from pydantic import BaseModel, Field

class User(BaseModel):
    id: int = Field(..., alias="user_id")
    name: str

# Parse with alias
data = {"user_id": 1, "name": "Sejal"}
user = User(**data)
print(user)
# Output: id=1 name='Sejal'
