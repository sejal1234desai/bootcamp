from typing import Iterator

class Splitter:
    def __init__(self, delimiter: str = ","):
        self.delimiter = delimiter

    def __call__(self, lines: Iterator[str]) -> Iterator[str]:
        for line in lines:
            for part in line.strip().split(self.delimiter):
                yield part
