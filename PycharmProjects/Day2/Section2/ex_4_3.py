#3. custom_class_context

class Logger:
    def __enter__(self):
        print("Entering context")
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Exiting context")

with Logger():
    print("Inside the block")

# Output:
# Entering context
# Inside the block
# Exiting context
