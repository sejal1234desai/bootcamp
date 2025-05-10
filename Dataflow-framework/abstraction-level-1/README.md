📁 Level 1 - CLI Interface with Parameters

Description:
This version turns the basic script into a CLI tool using typer. It accepts command-line arguments and supports different processing modes.

Features:

CLI built using typer

Accepts --input (required), --output (optional), --mode (optional)

Uses .env file for default mode

Supports 2 modes:

uppercase: converts to uppercase

snakecase: replaces spaces with underscores and converts to lowercase

Functions Introduced:

read_lines(path)

transform_line(line, mode)

write_output(lines, output_path)

Example Usage:

bash
Copy code
python process.py --input input.txt
python process.py --input input.txt --mode snakecase
python process.py --input input.txt --output result.txt
.env Example:

ini
Copy code
MODE=uppercase
Notes:

The script is still in a single file but modularized with small functions.

Output goes to stdout by default unless --output is specified.


