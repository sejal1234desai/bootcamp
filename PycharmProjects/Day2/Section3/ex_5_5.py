#5. multiple_factory_methods

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    @classmethod
    def from_json(cls, json_data):
        return cls(json_data["title"], json_data["author"])

    @classmethod
    def from_dict(cls, data):
        return cls(data["title"], data["author"])

b1 = Book.from_json({"title": "Inferno", "author": "Dan Brown"})
b2 = Book.from_dict({"title": "Origin", "author": "Dan Brown"})
print(b1.title, b2.title)

# Output:
# Inferno Origin
