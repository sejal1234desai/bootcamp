#8. conditional_comprehension

result = ['even' if x % 2 == 0 else 'odd' for x in range(5)]
print(result)

# Output:
# ['even', 'odd', 'even', 'odd', 'even']
