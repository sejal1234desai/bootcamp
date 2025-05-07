# Operation: Preview Field Descriptions in Editors

from pydantic import BaseModel, Field

class User(BaseModel):
    name: str = Field(..., description="User's full name")
    email: str = Field(..., description="User's email address")
    age: int = Field(..., description="User's age")

# You would see these descriptions as tooltips in VS Code or PyCharm when inspecting fields
data = {"name": "Sejal", "email": "sejal@example.com", "age": 22}
user = User(**data)
print(user)
# Output: name='Sejal' email='sejal@example.com' age=22

