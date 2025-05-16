## Operation: Frozen Dataclass (Immutable)

from dataclasses import dataclass

@dataclass(frozen=True)
class User:
    name: str
    age: int

u = User("Sejal", 22)
try:
    u.age = 25
except Exception as e:
    print("Modification Error:", e)
# Output: Modification Error: cannot assign to field 'age'
