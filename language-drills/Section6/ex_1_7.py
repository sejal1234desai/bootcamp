## Operation: Dataclass Comparison

from dataclasses import dataclass

@dataclass
class User:
    name: str
    age: int

u1 = User("Sejal", 22)
u2 = User("Sejal", 22)
print("Are users equal?", u1 == u2)
# Output: Are users equal? True
