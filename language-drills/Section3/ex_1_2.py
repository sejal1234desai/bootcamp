#2. create_object
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

book = Book("1984", "Orwell")
print(book.title)
print(book.author)

# Output:
# 1984
# Orwell
