#7. dynamic_attribute

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

book = Book("1984", "Orwell")
book.year = 1949
print(book.year)

# Output:
# 1949
