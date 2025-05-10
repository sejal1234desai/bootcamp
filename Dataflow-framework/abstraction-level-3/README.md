📁 Level 3 - Dynamic Config-Driven Pipeline

Description:
Now the pipeline is fully dynamic, controlled by a pipeline.yaml file. Users can configure the processing steps without touching the code.

New Feature:
Dynamic loading of processors using dotted import paths.

Example pipeline.yaml:

yaml
Copy code
pipeline:
  - type: processors.snake.to_snakecase
  - type: processors.upper.to_uppercase


**Folder Structure:
abstraction-level-3/
├── main.py
├── cli.py
├── core.py
├── pipeline.py
├── types.py
├── processors/
│   ├── upper.py
│   └── snake.py
├── pipeline.yaml
Example Usage:

bash

python main.py --input input.txt --config pipeline.yaml
Notes:

Replaces static mode with dynamic config

All processors must follow str -> str signature

Helpful error messages if imports fail

Enables plugin-style flexibility

Highlights:

Configurable by users

Decoupled logic and behavior

Supports future extensibility

