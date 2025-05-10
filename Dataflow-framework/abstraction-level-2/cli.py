import typer
from .core import to_uppercase, to_snakecase
from .pipeline import get_pipeline
from .processor_types import ProcessorFn

app = typer.Typer()

# Define the CLI command
@app.command()
def process(
    input_file: str = typer.Option(..., help="Path to the input file"),
    output_file: str = typer.Option(..., help="Path to the output file"),
    mode: str = typer.Option(..., help="Mode for processing (uppercase or snakecase)"),
):
    # Read the input file
    with open(input_file, "r") as f:
        lines = f.readlines()

    # Get the pipeline based on the mode
    processors = get_pipeline(mode)

    # Apply each processor in the pipeline to each line
    processed_lines = []
    for line in lines:
        for processor in processors:
            line = processor(line.strip())  # Apply each processor
        processed_lines.append(line)

    # Write the output file
    with open(output_file, "w") as f:
        for line in processed_lines:
            f.write(line + "\n")

if __name__ == "__main__":
    app()
