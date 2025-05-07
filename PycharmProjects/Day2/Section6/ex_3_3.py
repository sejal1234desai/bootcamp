# Operation: Title and Examples for Fields in Model

from pydantic import BaseModel, Field

class User(BaseModel):
    id: int = Field(..., title="User ID", examples=[1, 2, 3])
    name: str = Field(..., title="Full Name", examples=["Sejal", "Alice", "Bob"])

# Parsing data
data = {"id": 1, "name": "Sejal"}
user = User(**data)
print(user)
# Output: id=1 name='Sejal'
