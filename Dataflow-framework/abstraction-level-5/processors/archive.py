class Archive:
    def __init__(self):
        self.archived = []  # This will store all the lines that are archived

    def __call__(self, inputs):
        for tag, line in inputs:
            self.archived.append(line)  # Add line to the archived list
            yield tag, f"Archived: {line}"  # Yield the archived version of the line
