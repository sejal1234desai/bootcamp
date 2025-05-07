#name_shadowing

len = 5
# print(len("test"))  # TypeError: 'int' object is not callable

# To fix:
del len
print(len("test"))  # Now it works
