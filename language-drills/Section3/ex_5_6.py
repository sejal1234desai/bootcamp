#6. invoke_static

class Book:
    @staticmethod
    def is_valid_isbn(isbn):
        return len(isbn) in (10, 13)

b = Book()
print(Book.is_valid_isbn("1234567890123"))
print(b.is_valid_isbn("1234567890"))

# Output:
# True
# True
