## Operation: Use Slots to Reduce Memory

from dataclasses import dataclass

@dataclass(slots=True)
class User:
    name: str
    age: int

u = User("Sejal", 22)
print(u)
# Output: User(name='Sejal', age=22)
