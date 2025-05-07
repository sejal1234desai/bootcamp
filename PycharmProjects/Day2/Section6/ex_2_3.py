#3# Operation: Nested Models

from pydantic import BaseModel

class Profile(BaseModel):
    bio: str
    website: str

class User(BaseModel):
    name: str
    age: int
    profile: Profile

# Nested dict parsing
data = {
    "name": "Sejal",
    "age": 22,
    "profile": {"bio": "Developer", "website": "https://sejal.com"}
}

user = User(**data)
print(user)
# Output: name='Sejal' age=22 profile=Profile(bio='Developer', website='https://sejal.com')
