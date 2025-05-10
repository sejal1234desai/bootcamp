class Splitter:
    def __call__(self, inputs):
        for line in inputs:
            line = line.strip()
            if line:  # skip empty lines
                yield None, line
