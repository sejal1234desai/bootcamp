#5. use_str

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"Book: '{self.title}' by {self.author}"

book = Book("1984", "Orwell")
print(book)

# Output:
# Book: '1984' by Orwell
