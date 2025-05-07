#2. classmethod_from_string

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    @classmethod
    def from_string(cls, s):
        title, author = s.split("|")
        return cls(title, author)

b = Book.from_string("1984|Orwell")
print(b.title, b.author)

# Output:
# 1984 Orwell
