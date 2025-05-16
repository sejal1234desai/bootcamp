#7. compose_func

def compose(f, g):
    return lambda x: f(g(x))

def add_one(x): return x + 1
def square(x): return x * x

h = compose(square, add_one)
print(h(3))  # Output: 16 → (3 + 1)^2
