#4. static_no_self_cls

class Book:
    @staticmethod
    def info():
        return "Static method: no access to self or cls"

print(Book.info())
b = Book()
print(b.info())

# Output:
# Static method: no access to self or cls
# Static method: no access to self or cls
