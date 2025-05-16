# Operation: Model Docstrings for Purpose Clarification

from pydantic import BaseModel

class User(BaseModel):
    """
    A model representing a user in the system.
    It contains essential information such as name, email, and age.
    """
    name: str
    email: str
    age: int

# Parsing data
data = {"name": "Sejal", "email": "sejal@example.com", "age": 22}
user = User(**data)
print(user)
# Output: name='Sejal' email='sejal@example.com' age=22
