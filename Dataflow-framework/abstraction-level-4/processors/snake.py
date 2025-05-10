from .decorator import stream_adapter

@stream_adapter
def to_snakecase(line: str) -> str:
    return line.strip().lower().replace(" ", "_")
