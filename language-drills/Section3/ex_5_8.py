#8. hybrid_method_example

class Library:
    books = []

    def __init__(self, name):
        self.name = name

    @staticmethod
    def is_open(hour):
        return 9 <= hour <= 17

    @classmethod
    def add_book(cls, book):
        cls.books.append(book)

    def describe(self):
        return f"{self.name} has {len(self.books)} books."

Library.add_book("1984")
print(Library.is_open(10))  # True
lib = Library("City Library")
print(lib.describe())       # City Library has 1 books.

# Output:
# True
# City Library has 1 books.
