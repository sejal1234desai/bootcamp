#5
# Operation: Custom Validator

from pydantic import BaseModel, validator

class User(BaseModel):
    name: str
    age: int

    @validator('name')
    def check_name_capitalization(cls, v):
        if not v[0].isupper():
            raise ValueError('Name must start with a capital letter')
        return v

# This will pass validation
data = {"name": "Sejal", "age": 22}
user = User(**data)
print(user)
# Output: name='Sejal' age=22

# This will fail validation for name
data = {"name": "sejal", "age": 22}
try:
    user = User(**data)
except ValidationError as e:
    print("Validation Error:", e)
# Output: Validation Error: 1 validation error for User
# name
#   Name must start with a capital letter (type=value_error)
