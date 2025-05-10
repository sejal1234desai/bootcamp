class TagError:
    def __call__(self, inputs):
        for tag, line in inputs:
            if "error" in line.lower():
                yield "errors", line
            else:
                yield tag if tag else "info", line
