class Count:
    def __init__(self):
        self.count = 0

    def __call__(self, inputs):
        for tag, line in inputs:
            self.count += 1
            yield tag, f"Counted line #{self.count}: {line}"
