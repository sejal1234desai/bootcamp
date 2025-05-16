#nested_function_access

def outer():
    message = "Hello from outer!"

    def inner():
        print(message)

    inner()

outer()
