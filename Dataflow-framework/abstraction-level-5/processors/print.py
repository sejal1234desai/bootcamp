class Print:
    def __init__(self, output_file):
        self.output_file = output_file
        self.file = open(self.output_file, 'w')  # Open file in write mode

    def __call__(self, inputs):
        for tag, line in inputs:
            print(f"Writing to file: {tag}: {line}")  # Print the output before writing
            self.file.write(f"{tag}: {line}\n")

    def close(self):
        self.file.close()
