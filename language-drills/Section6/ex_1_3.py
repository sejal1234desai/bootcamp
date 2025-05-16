#
# Operation: Post-Init Validation

from dataclasses import dataclass

@dataclass
class User:
    name: str
    age: int

    def __post_init__(self):
        if self.age < 0:
            raise ValueError("Age cannot be negative")

try:
    User("Sejal", -5)
except ValueError as e:
    print("Validation Error:", e)
# Output: Validation Error: Age cannot be negative
