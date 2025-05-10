from typing import Iterator

class JoinPairs:
    def __init__(self):
        self.buffer = []

    def __call__(self, lines: Iterator[str]) -> Iterator[str]:
        for line in lines:
            self.buffer.append(line)
            if len(self.buffer) == 2:
                yield f"{self.buffer[0]} {self.buffer[1]}"
                self.buffer = []
        if self.buffer:
            yield self.buffer[0]
