#
# Operation: Count character frequencies in a string

from collections import Counter

text = "hello world"
count = Counter(text)

print(count)
# Output: Counter({'l': 3, 'o': 2, 'h': 1, 'e': 1, ' ': 1, 'w': 1, 'r': 1, 'd': 1})
