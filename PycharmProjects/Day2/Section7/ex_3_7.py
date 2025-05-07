#7
# Operation: Log call stack depth using an argument like level or indent

def recursive_function(n, level=0):
    print(f"{'  ' * level}Calling recursive_function with n={n}")
    if n > 0:
        recursive_function(n - 1, level + 1)
    print(f"{'  ' * level}Exiting recursive_function with n={n}")

# Example usage:
recursive_function(3)

# Output:
# Calling recursive_function with n=3
#   Calling recursive_function with n=2
#     Calling recursive_function with n=1
#       Calling recursive_function with n=0
#       Exiting recursive_function with n=0
#     Exiting recursive_function with n=1
#   Exiting recursive_function with n=2
# Exiting recursive_function with n=3
