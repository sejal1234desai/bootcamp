from .core import to_uppercase, to_snakecase
from .processor_types import ProcessorFn

# Define a function that assembles the pipeline based on the mode
def get_pipeline(mode: str) -> list[ProcessorFn]:
    if mode == "uppercase":
        return [to_uppercase]
    elif mode == "snakecase":
        return [to_snakecase]
    else:
        return []  # Empty list for unsupported modes
