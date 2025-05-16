#6. sort_lambda.

pairs = [(1, "b"), (2, "a")]
sorted_pairs = sorted(pairs, key=lambda x: x[1])
print(sorted_pairs)  # Output: [(2, 'a'), (1, 'b')]
