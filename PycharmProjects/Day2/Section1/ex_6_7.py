#7. generator_expression

evens = (x for x in range(10) if x % 2 == 0)
for e in evens:
    print(e)

# Output:
# 0
# 2
# 4
# 6
# 8
