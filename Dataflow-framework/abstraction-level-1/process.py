import typer
from typing import Optional, Iterator
from dotenv import load_dotenv
import os

app = typer.Typer()

def read_lines(path: str) -> Iterator[str]:
    with open(path, 'r') as file:
        for line in file:
            yield line.strip()

def transform_line(line: str, mode: str) -> str:
    if mode == "uppercase":
        return line.upper()
    elif mode == "snakecase":
        return line.lower().replace(" ", "_")
    else:
        raise ValueError(f"Unsupported mode: {mode}")

def write_output(lines: Iterator[str], output_path: Optional[str]) -> None:
    if output_path:
        with open(output_path, 'w') as file:
            for line in lines:
                file.write(line + '\n')
    else:
        for line in lines:
            print(line)

@app.command()
def process(
    input: str = typer.Option(..., help="Input file path"),
    output: Optional[str] = typer.Option(None, help="Output file path (optional)"),
    mode: Optional[str] = typer.Option(None, help="Processing mode: uppercase or snakecase")
):
    load_dotenv()
    mode = mode or os.getenv("MODE", "uppercase")

    lines = read_lines(input)
    transformed = (transform_line(line, mode) for line in lines)
    write_output(transformed, output)

if __name__ == "__main__":
    app()
