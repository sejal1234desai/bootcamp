#6. multiple_inheritance

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

class AudioMixin:
    def play_audio(self):
        return "Playing audio version..."

class AudioBook(Book, AudioMixin):
    pass

ab = AudioBook("1984", "Orwell")
print(ab.play_audio())

# Output:
# Playing audio version...
