#4. class_vs_instance_variable

class Book:
    category = "Fiction"

    def __init__(self, title, author):
        self.title = title
        self.author = author

book = Book("1984", "Orwell")
print(book.category)

# Output:
# Fiction
