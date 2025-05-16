#4. ordering_support

class Book:
    def __init__(self, title):
        self.title = title

    def __lt__(self, other):
        return self.title < other.title

books = [Book("Brave New World"), Book("1984")]
books.sort()
for b in books:
    print(b.title)

# Output:
# 1984
# Brave New World
