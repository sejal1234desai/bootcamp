#8. polymorphism_in_action

class Book:
    def describe(self):
        return "This is a book."

class Novel(Book):
    def describe(self):
        return "This is a novel."

items = [Book(), Novel()]

for item in items:
    print(item.describe())

# Output:
# This is a book.
# This is a novel.
