#scope_error

def broken():
    # print(msg)  # Uncommenting this line causes UnboundLocalError
    msg = "Hello"
    print(msg)

broken()
