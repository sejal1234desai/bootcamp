#4# Operation: Field Constraints with conint and constr

from pydantic import BaseModel, conint, constr

class User(BaseModel):
    name: constr(min_length=3)
    age: conint(gt=0)

# This will succeed
data = {"name": "Sejal", "age": 22}
user = User(**data)
print(user)
# Output: name='Sejal' age=22

# This will fail validation for name (min_length=3)
data = {"name": "Se", "age": 22}
try:
    user = User(**data)
except ValidationError as e:
    print("Validation Error:", e)
# Output: Validation Error: 1 validation error for User
# name
#   ensure this value has at least 3 characters (type=value_error.any_str.min_length; limit_value=3)
