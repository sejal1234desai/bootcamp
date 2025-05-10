from typing import Callable, Iterator

def stream_adapter(fn: Callable[[str], str]) -> Callable[[Iterator[str]], Iterator[str]]:
    def wrapped(lines: Iterator[str]) -> Iterator[str]:
        for line in lines:
            result = fn(line)
            if result is not None:
                yield result
    return wrapped
