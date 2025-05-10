from pipeline import build_pipeline
from processors.snake import to_snakecase
from processors.line_counter import LineCounter
from processors.splitter import Splitter
from processors.join_pairs import JoinPairs
from cli import parse_args
from typing import Iterator
import os


def get_lines(input_path: str) -> Iterator[str]:
    if os.path.exists(input_path):
        with open(input_path, 'r') as f:
            for line in f:
                yield line.strip()
    else:
        print(f"Input file {input_path} not found. Using default lines.")
        yield "Hello World"
        yield "This is a default line."


def write_output(output_lines: Iterator[str], output_path: str = None):
    if output_path:
        with open(output_path, 'w') as f:
            for line in output_lines:
                f.write(line + '\n')
    else:
        for line in output_lines:
            print(line)


if __name__ == "__main__":
    args = parse_args()

    processors = [
        to_snakecase,
        Splitter(delimiter="_"),
        JoinPairs(),
        LineCounter(),
    ]

    pipeline = build_pipeline(processors)
    input_lines = get_lines(args.input)
    output_lines = pipeline(input_lines)
    write_output(output_lines, args.output_file)
