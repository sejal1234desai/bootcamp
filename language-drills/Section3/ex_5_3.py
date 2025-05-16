#3. classmethod_with_subclass

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    @classmethod
    def from_string(cls, s):
        title, author = s.split("|")
        return cls(title, author)

class Novel(Book):
    def __init__(self, title, author, genre="Fiction"):
        super().__init__(title, author)
        self.genre = genre

n = Novel.from_string("Dune|Herbert")
print(isinstance(n, Novel), n.title, n.genre)

# Output:
# True Dune Fiction
