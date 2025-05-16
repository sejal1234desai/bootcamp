# Operation: Use Inline Comments Sparingly

def calculate_area(radius):
    # Using the formula for area of a circle
    area = 3.14 * radius * radius
    return area

# Bad practice: Explaining what the code does
def calculate_area(radius):
    area = 3.14 * radius * radius  # Formula for area of a circle
    return area

# Output:
# The comment adds little value. Explain *why* the code does something, not *what* it does.
