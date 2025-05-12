# 04_json_deserialize_book.py

import json

class Book:
    def __init__(self, title, author, year, genre):
        self.title = title
        self.author = author
        self.year = year
        self.genre = genre

    @classmethod
    def from_json(cls, json_string):
        data = json.loads(json_string)
        return cls(**data)

    def __str__(self):
        return f"'{self.title}' by {self.author} ({self.year}) - Genre: {self.genre}"

# Read JSON from file
with open("book_data.json", "r") as f:
    json_data = f.read()

# Convert JSON string to Book object
book = Book.from_json(json_data)

# Print the book details
print("Deserialized Book object:")
print(book)
