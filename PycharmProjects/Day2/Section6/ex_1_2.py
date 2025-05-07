#
# Operation: Dataclass with Default Value

from dataclasses import dataclass

@dataclass
class User:
    name: str
    age: int
    country: str = "India"

u = User("Sejal", 22)
print(u)
# Output: User(name='Sejal', age=22, country='India')
