def process_file(input_file: str, pipeline: list, output_file: str):
    try:
        with open(input_file, "r") as file:
            lines = file.readlines()

        # Open output file for writing
        with open(output_file, "w") as output:
            for line in lines:
                for processor in pipeline:
                    line = processor(line.strip())
                output.write(line + "\n")  # Write processed line to the output file

    except FileNotFoundError:
        print(f"Error: The file {input_file} was not found.")
