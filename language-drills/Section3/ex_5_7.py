#7. method_resolution

class Book:
    @classmethod
    def whoami(cls):
        return f"I am a {cls.__name__}"

class Novel(Book):
    @classmethod
    def whoami(cls):
        return f"Subclass says: {cls.__name__}"

print(Book.whoami())
print(Novel.whoami())

# Output:
# I am a Book
# Subclass says: Novel
