#4. sorted_with_key

pairs = [(1, 3), (2, 2), (3, 1)]

sorted_pairs = sorted(pairs, key=lambda x: x[1])
print(sorted_pairs)

# Output:
# [(3, 1), (2, 2), (1, 3)]
