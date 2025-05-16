#filter_even_length_strings

words = ["hi", "hello", "bye"]
even_words = [word for word in words if len(word) % 2 == 0]
print(even_words)  # ['hi']
