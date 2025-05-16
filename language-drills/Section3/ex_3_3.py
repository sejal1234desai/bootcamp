#3. hashing_support

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __eq__(self, other):
        return (self.title, self.author) == (other.title, other.author)

    def __hash__(self):
        return hash((self.title, self.author))

book_set = {Book("1984", "Orwell"), Book("1984", "Orwell")}
print(len(book_set))

# Output:
# 1
