#2. default_values

from dataclasses import dataclass

@dataclass
class User:
    name: str
    age: int = 0

u = User("Anonymous")
print(u)

# Output:
# User(name='Anonymous', age=0)
