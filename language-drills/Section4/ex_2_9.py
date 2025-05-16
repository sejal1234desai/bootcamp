#9. validate_args

def validate_args(func):
    def wrapper(self, *args):
        if all(isinstance(arg, int) for arg in args):
            return func(self, *args)
        else:
            print("Invalid argument types!")
    return wrapper

class Calculator:
    @validate_args
    def add(self, x, y):
        return x + y

calc = Calculator()
print(calc.add(5, 3))      # Valid
print(calc.add("5", "3"))  # Invalid
