#8. inheritance_dataclass

from dataclasses import dataclass

@dataclass
class User:
    name: str
    age: int

@dataclass
class AdminUser(User):
    access_level: int

admin = AdminUser("Sejal", 25, 5)
print(admin)

# Output:
# AdminUser(name='Sejal', age=25, access_level=5)
