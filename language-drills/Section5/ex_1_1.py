## Operation: Group words by their first letter using defaultdict

from collections import defaultdict

words = ["apple", "banana", "avocado", "berry", "cherry", "apricot"]
grouped = defaultdict(list)

for word in words:
    grouped[word[0]].append(word)

print(dict(grouped))
# Output: {'a': ['apple', 'avocado', 'apricot'], 'b': ['banana', 'berry'], 'c': ['cherry']}
