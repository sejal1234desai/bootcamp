#set_comprehension
text = "hello world"
vowels = {char for char in text if char in 'aeiou'}
print(vowels)  #  {'e', 'o'}
