class Tally:
    def __init__(self):
        self.tally = 0  # Initialize the tally counter

    def __call__(self, inputs):
        for tag, line in inputs:
            self.tally += 1  # Increment the tally count for each line
            yield tag, f"Tally count: {self.tally} | Line: {line}"  # Yield the tally with the line
