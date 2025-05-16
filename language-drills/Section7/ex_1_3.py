#
# Operation: Profile a script using cProfile

# Save this script as 'yourscript.py' and run with: python -m cProfile yourscript.py

def example_function():
    sum(range(1000000))

if __name__ == '__main__':
    example_function()

# Output:
# Running `python -m cProfile yourscript.py` will produce a detailed report with function call counts and execution time.
