#8. prefer_lbyl_isinstance

def upper_case(val):
    if isinstance(val, str):
        return val.upper()
    else:
        return "Not a string."

print(upper_case("hello"))  # Output: HELLO
print(upper_case(123))      # Output: Not a string.
