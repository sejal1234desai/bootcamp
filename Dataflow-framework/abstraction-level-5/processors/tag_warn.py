class TagWarn:
    def __call__(self, inputs):
        for tag, line in inputs:
            if "warn" in line.lower():
                yield "warnings", line
            else:
                yield tag if tag else "info", line
