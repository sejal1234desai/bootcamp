#5. custom_method

from dataclasses import dataclass

@dataclass
class User:
    name: str
    age: int

    def is_adult(self):
        return self.age >= 18

u = User("Sejal", 17)
print(u.is_adult())

# Output:
# False
