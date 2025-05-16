#7. isinstance_inheritance

class Book:
    pass

class Novel(Book):
    pass

novel = Novel()
print(isinstance(novel, Book))

# Output:
# True
