#3. use_super

class Book:
    def describe(self):
        return "Generic book description"

class Novel(Book):
    def describe(self):
        return f"Novel detail: {super().describe()}"

novel = Novel()
print(novel.describe())

# Output:
# Novel detail: Generic book description
