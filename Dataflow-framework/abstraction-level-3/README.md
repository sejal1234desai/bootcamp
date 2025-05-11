
📁 Level 3 – Dynamic Config-Driven Pipeline

Description:
In this level, your task is to fully decouple pipeline logic from code. The pipeline will be controlled by a pipeline.yaml file, allowing users to specify their desired line-processing steps without needing to touch the source code.

This unlocks extensibility, enabling users to create and reuse their own processors without altering the program’s source code.

📝 Task:
Created a pipeline.yaml file that defines the processing steps using import paths:

yaml
Copy code
pipeline:
  - type: processors.snake.to_snakecase
  - type: processors.upper.to_uppercase
Write a function that:

Parses the pipeline.yaml config file

Dynamically loads each function from its import path

Returns a list of ProcessorFn functions

Replace your static pipeline from Level 2 with this dynamic list.

Update your CLI to accept --config pipeline.yaml instead of --mode.

📂 Folder Structure:
plaintext
Copy code
abstraction-level-3/
├── main.py               # Main entry point for pipeline execution
├── cli.py                # Handles CLI interaction and argument parsing
├── core.py               # Core logic for managing pipeline flow
├── pipeline.py           # Loads pipeline dynamically from YAML
├── types.py              # Type definitions and utility functions
├── processors/           # Folder containing processor modules
│   ├── upper.py          # Processor that converts text to uppercase
│   └── snake.py          # Processor that converts text to snake_case
└── pipeline.yaml         # Configuration file defining the pipeline steps
💡 Example Usage:
Run the pipeline with your input file and the configuration file:

bash
Copy code
python main.py --input input.txt --config pipeline.yaml



✅ Checklist – Level 3: Dynamic Config-Driven Pipeline
 CLI updated to accept a config file
The CLI now accepts --config pipeline.yaml instead of --mode.

 Program dynamically imports and composes processor functions from YAML
The program loads each processor function dynamically based on the import path specified in the pipeline.yaml file.

 All processors conform to str -> str
All processor functions follow the str -> str signature, ensuring that each one processes a line of text and returns a processed line.

 Import errors are handled cleanly
If the import path is incorrect or the processor function is not found, the program provides helpful error messages to guide the user.

 pipeline.yaml specifies functions using full dotted import paths
The pipeline.yaml file correctly uses full dotted import paths to specify processor functions, such as processors.snake.to_snakecase and processors.upper.to_uppercase.

