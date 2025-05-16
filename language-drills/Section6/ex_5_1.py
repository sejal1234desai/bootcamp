# Operation: Refactor Function for Clear Naming

def do_it(score, max_score):
    return (score / max_score) * 100

# Refactor to a more descriptive function name
def calculate_score(score, max_score):
    return (score / max_score) * 100

# Output:
# The function is now more readable and describes what it's doing.
