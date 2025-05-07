#1. basic_dataclass

from dataclasses import dataclass

@dataclass
class User:
    name: str
    age: int

u = User("Sejal", 25)
print(u)

# Output:
# User(name='Sejal', age=25)
