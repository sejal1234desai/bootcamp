## Operation: Add a Custom Method

from dataclasses import dataclass

@dataclass
class User:
    name: str
    age: int

    def is_adult(self) -> bool:
        return self.age >= 18

u = User("Sejal", 22)
print("Is adult?", u.is_adult())
# Output: Is adult? True
