## Operation: Basic Dataclass
from dataclasses import dataclass

@dataclass
class User:
    name: str
    age: int

u = User("Sejal", 22)
print(u)
# Output: User(name='Sejal', age=22)
