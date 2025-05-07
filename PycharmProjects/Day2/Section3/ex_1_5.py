#5. update_object_state

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def update_title(self, new_title):
        self.title = new_title

book = Book("1984", "Orwell")
print("Before:", book.title)
book.update_title("Animal Farm")
print("After:", book.title)

# Output:
# Before: 1984
# After: Animal Farm
