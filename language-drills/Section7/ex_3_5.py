#5# Operation: Issue a non-fatal warning using warnings.warn()

import warnings

def process_data(data):
    if not data:
        warnings.warn("No data provided, using default values.")
    return data or "Default data"

# Example usage:
process_data([])

# Output:
# Warning: No data provided, using default values.
