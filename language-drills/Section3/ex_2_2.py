#2. override_method

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def describe(self):
        return f"{self.title} by {self.author}"

class Novel(Book):
    def describe(self):
        return f"Novel: {self.title} by {self.author}"

novel = Novel("1984", "Orwell")
print(novel.describe())

# Output:
# Novel: 1984 by Orwell
