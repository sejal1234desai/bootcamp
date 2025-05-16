# tuple_immutable_error

t = (1, 2, 3)
try:
    t[0] = 10   # TypeError expected
except TypeError as e:
    print("Error:", e)
