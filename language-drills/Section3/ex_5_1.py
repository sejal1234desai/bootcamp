#1. static_method_isbn

class Book:
    @staticmethod
    def is_valid_isbn(isbn):
        return isinstance(isbn, str) and len(isbn) in (10, 13)

print(Book.is_valid_isbn("1234567890"))  # True

# Output:
# True
