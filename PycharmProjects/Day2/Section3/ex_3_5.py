#5. custom_container_len

class Library:
    def __init__(self):
        self.books = []

    def add(self, book):
        self.books.append(book)

    def __len__(self):
        return len(self.books)

lib = Library()
lib.add("1984")
lib.add("Brave New World")
print(len(lib))

# Output:
# 2
