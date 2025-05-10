class Trim:
    def __init__(self):
        pass

    def __call__(self, inputs):
        for tag, line in inputs:
            trimmed_line = line.strip()
            yield tag, trimmed_line
