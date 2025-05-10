# processors/upper.py
# processors/upper.py (after wrapping)
from processors.decorator import stream_adapter

@stream_adapter
def to_uppercase(line: str) -> str:
    return line.upper()
