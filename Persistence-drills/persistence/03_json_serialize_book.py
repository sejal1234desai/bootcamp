# 03_json_serialize_book.py

import json

class Book:
    def __init__(self, title, author, year, genre):
        self.title = title
        self.author = author
        self.year = year
        self.genre = genre

    def to_json(self):
        return json.dumps(self.__dict__, indent=4)

# Create a book instance
book = Book(
    title="Mastering Python Persistence",
    author="Sejal Desai",
    year=2025,
    genre="Educational / Programming"
)

# Convert to JSON string
json_data = book.to_json()

# Print the JSON
print("Book object in JSON format:")
print(json_data)

# Save JSON to file
with open("book_data.json", "w") as f:
    f.write(json_data)
