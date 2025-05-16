#1. str_vs_repr

class Book:
    def __init__(self, title):
        self.title = title

    def __str__(self):
        return f"Book: {self.title}"

    def __repr__(self):
        return f"Book('{self.title}')"

book = Book("1984")
print(book)         # Uses __str__
print(repr(book))   # Uses __repr__

# Output:
# Book: 1984
# Book('1984')
