
#4. comparison_support

from dataclasses import dataclass

@dataclass
class User:
    name: str
    age: int

u1 = User("Sejal", 25)
u2 = User("Sejal", 25)
print(u1 == u2)

# Output:
# True
