#3. frozen_dataclass

from dataclasses import dataclass

@dataclass(frozen=True)
class User:
    name: str
    age: int

u = User("Sejal", 25)
# u.age = 30  # Uncommenting this will raise a FrozenInstanceError

print(u)

# Output:
# User(name='Sejal', age=25)