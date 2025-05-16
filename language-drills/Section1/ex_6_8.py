#8. compare_generators_lists


# List comprehension
lst = [x for x in range(5) if x % 2 == 0]
print("List:", lst)

# Generator expression
gen = (x for x in range(5) if x % 2 == 0)
print("Generator:", list(gen))  # Convert to list for display

# Output:
# List: [0, 2, 4]
# Generator: [0, 2, 4]
