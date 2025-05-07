# Operation: Keep Functions Small

# Bad practice: Large function
def process_data(data):
    # logic to clean data
    # logic to transform data
    # logic to filter data
    return processed_data

# Improved with small functions
def clean_data(data):
    # logic to clean data
    return cleaned_data

def transform_data(data):
    # logic to transform data
    return transformed_data

def filter_data(data):
    # logic to filter data
    return filtered_data

def process_data(data):
    cleaned_data = clean_data(data)
    transformed_data = transform_data(cleaned_data)
    return filter_data(transformed_data)

# Output:
# Each function does one thing, is less than 10 lines, and is easy to understand.
