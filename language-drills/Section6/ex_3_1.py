#1
## Operation: Field Descriptions for Readability

from pydantic import BaseModel, Field

class User(BaseModel):
    name: str = Field(..., description="User's full name")
    email: str = Field(..., description="User's email address")
    age: int = Field(..., description="User's age")

# Parsing data
data = {"name": "Sejal", "email": "sejal@example.com", "age": 22}
user = User(**data)
print(user)
# Output: name='Sejal' email='sejal@example.com' age=22
