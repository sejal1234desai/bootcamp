
📁 Level 2 - Modular Structure and Standardized Processing

Description:
This level breaks the monolithic script into reusable modules. Each processor follows a standardized function signature.

📝 Task
Split the code into modules:

main.py - Handles reading input and writing output.

cli.py - Manages the CLI with typer.

core.py - Contains processors that perform specific transformations.

pipeline.py - Assembles the processor list based on the selected mode.

types.py - Defines the ProcessorFn type.

📂 Folder Structure
plaintext
Copy code
abstraction-level-2/
├── main.py         # Reads input, writes output
├── cli.py          # Handles CLI via Typer
├── core.py         # Applies a list of processors to each line
├── pipeline.py     # Assembles the processor list based on mode
└── types.py        # Defines ProcessorFn types
💡 Example Usage:
bash
Copy code
python main.py --input input.txt --mode snakecase
