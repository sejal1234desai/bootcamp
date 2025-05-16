#4. attribute_access_eafp

class User:
    def __init__(self, name):
        self.name = name

u = User("Sejal")
print(getattr(u, "email", "Not provided"))

# Output:
# Not provided
