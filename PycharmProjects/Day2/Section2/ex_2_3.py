#3. any_all_example

numbers = [1, 2, -3, 4]

print(any(n < 0 for n in numbers))  # Output: True
print(all(n > 0 for n in numbers))  # Output: False
