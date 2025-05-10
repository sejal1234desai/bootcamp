import re
from .processor_types import ProcessorFn

# Processor to convert line to uppercase
def to_uppercase(line: str) -> str:
    return line.upper()

# Processor to convert line to snake_case
def to_snakecase(line: str) -> str:
    # Convert any non-alphanumeric characters to underscores and make all lowercase
    return re.sub(r'(?<=\w)([A-Z])', r'_\1', line).lower()
