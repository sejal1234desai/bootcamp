#7. callability

class Greeter:
    def __call__(self, name):
        return f"Hello, {name}!"

g = Greeter()
print(g("Sejal"))

# Output:
# Hello, Sejal!
