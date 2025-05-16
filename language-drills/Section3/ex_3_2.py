#2. equality_check

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __eq__(self, other):
        return isinstance(other, Book) and self.title == other.title and self.author == other.author

b1 = Book("1984", "Orwell")
b2 = Book("1984", "Orwell")
print(b1 == b2)

# Output:
# True
