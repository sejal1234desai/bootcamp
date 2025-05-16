#6. indexing_support

class Library:
    def __init__(self, books):
        self.books = books

    def __getitem__(self, index):
        return self.books[index]

lib = Library(["1984", "Brave New World"])
print(lib[0])

# Output:
# 1984
