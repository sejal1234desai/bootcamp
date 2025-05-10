📁 Level 2 - Modular Structure and Processors

Description:
This level breaks the monolithic script into reusable modules. Each processor follows a standardized function signature.

Folder Structure:

pgsql
Copy code
abstraction-level-2/
├── main.py
├── cli.py
├── core.py
├── pipeline.py
├── types.py
Processor Interface:
Each processor is a function that takes a string and returns a string:

python
Copy code
ProcessorFn = Callable[[str], str]
Defined Processors in core.py:

to_uppercase(line)

to_snakecase(line)

Pipeline:
In pipeline.py, mode decides which list of processors to apply.

Example Usage:

bash

python main.py --input input.txt --mode snakecase
Highlights:

Clear separation of concerns

Easy to add new processors

Logic flows: CLI ➜ Pipeline ➜ Core ➜ I/O

Note:
This is a major improvement in maintainability and structure.
