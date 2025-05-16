#positional_only_args

def divide(x, y, /):
    return x / y

print(divide(10, 2))
# divide(x=10, y=2)  # This will raise a TypeError
