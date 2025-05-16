#8. ensure_cleanup

class Resource:
    def __enter__(self):
        print("Acquiring resource")
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Releasing resource")

try:
    with Resource():
        print("Inside")
        raise ValueError("Oops")
except ValueError as e:
    print("Caught error:", e)

# Output:
# Acquiring resource
# Inside
# Releasing resource
# Caught error: Oops
