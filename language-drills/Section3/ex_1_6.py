#6. init_with_defaults

class Book:
    def __init__(self, title="Untitled", author="Unknown"):
        self.title = title
        self.author = author

book1 = Book("1984", "Orwell")
book2 = Book()

print(book1.title, "-", book1.author)
print(book2.title, "-", book2.author)

# Output:
# 1984 - Orwell
# Untitled - Unknown
