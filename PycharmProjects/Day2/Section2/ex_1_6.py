#6. custom_getattr

class FlexibleObject:
    def __getattr__(self, name):
        return f"{name} is not defined, but handled!"

obj = FlexibleObject()
print(obj.hello)  # Output: hello is not defined, but handled!
print(obj.anything_else)  # Output: anything_else is not defined, but handled!
