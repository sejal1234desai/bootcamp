
import yaml

# Read input lines from file
def read_lines(input_file):
    with open(input_file, 'r') as f:
        return [(None, line.strip()) for line in f.readlines()]


# Base Pipeline class
class Pipeline:
    def __init__(self):
        self.processors = []  # Maintain order
        self.routes = []      # List of (from_tag, to_tag)

    def add_processor(self, processor):
        self.processors.append(processor)

    def add_route(self, from_tag, to_tag):
        self.routes.append((from_tag, to_tag))

    def run(self, input_data):
        data = input_data

        # Apply processors
        for processor in self.processors:
            data = list(processor(data)) if processor(data) is not None else []

        # Apply routing logic
        routed_data = {}
        for from_tag, to_tag in self.routes:
            routed_data[to_tag] = [line for tag, line in data if tag == from_tag]

        print("Processed and routed data:", routed_data)
        return routed_data


# Processor to print to file
class Print:
    def __init__(self, output_file):
        self.output_file = output_file
        self.file = open(self.output_file, 'w')

    def __call__(self, inputs):
        for tag, line in inputs:
            tag_str = tag if tag else "info"
            self.file.write(f"{tag_str}: {line}\n")
            yield tag_str, line  # Let it pass along for routing

    def close(self):
        self.file.close()


# Tag processor for errors
class TagError:
    def __call__(self, inputs):
        for tag, line in inputs:
            if "error" in line.lower():
                yield "tag_error", line
            else:
                yield tag, line


# Tag processor for warnings
class TagWarn:
    def __call__(self, inputs):
        for tag, line in inputs:
            if "warn" in line.lower():
                yield "tag_warn", line
            else:
                yield tag, line


# Main function
def main():
    input_file = 'input.txt'
    output_file = 'output.txt'
    config_file = 'config.yaml'

    # Optional: Read config if needed
    with open(config_file, 'r') as f:
        config = yaml.safe_load(f)

    pipeline = Pipeline()

    # Add processors
    pipeline.add_processor(TagError())
    pipeline.add_processor(TagWarn())
    printer = Print(output_file)
    pipeline.add_processor(printer)

    # Add routing (ensure tag matches processor output)
    pipeline.add_route('tag_error', 'archive')
    pipeline.add_route('tag_warn', 'tally')

    # Read and run
    input_data = read_lines(input_file)
    pipeline.run(input_data)

    # Close output file
    printer.close()


if __name__ == "__main__":
    main()
