import argparse
import yaml
import importlib
import os


def load_processors(config_file):
    # Read the pipeline config from YAML file
    with open(config_file, 'r') as file:
        config = yaml.safe_load(file)

    processors = []

    # Dynamically load processor functions based on the YAML config
    for item in config.get('pipeline', []):
        module_path = item.get('type')
        if module_path:
            try:
                # Split the import path into module and function names
                module_name, function_name = module_path.rsplit('.', 1)
                module = importlib.import_module(module_name)
                processor_fn = getattr(module, function_name)
                processors.append(processor_fn)
            except (ImportError, AttributeError) as e:
                print(f"Error loading processor function: {module_path}")
                raise e

    return processors


def process_file(input_file, output_file, processors):
    # Read the input file content
    with open(input_file, 'r') as f:
        content = f.read()

    # Apply all processors in the pipeline
    for processor in processors:
        content = processor(content)

    # Write the processed content to the output file
    with open(output_file, 'w') as f:
        f.write(content)


def main():
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Process text files using a dynamic pipeline.")
    parser.add_argument('--input', required=True, help="Path to the input file")
    parser.add_argument('--output-file', required=True, help="Path to the output file")
    parser.add_argument('--config', required=True, help="Path to the YAML configuration file for the pipeline")

    args = parser.parse_args()

    # Load processors from config file
    processors = load_processors(args.config)

    # Process the file
    process_file(args.input, args.output_file, processors)
    print(f"Processing complete. Output written to {args.output_file}")


if __name__ == "__main__":
    main()
