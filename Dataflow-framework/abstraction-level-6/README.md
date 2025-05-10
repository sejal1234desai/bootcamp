Level 6 – State-Based Routing System
In this level, the pipeline is no longer linear or defined by a DAG. Instead, routing is determined dynamically using tags that each line carries.

Each processor is registered under a tag. A processor receives all lines tagged with its name, processes them, and emits (tag, line) pairs that are routed to the corresponding downstream processor(s).

Lines tagged with 'end' are considered complete and exit the system.

Requirements
Lines enter with the 'start' tag.

Each tag corresponds to a registered processor.

A processor:

Receives lines with a specific tag

Emits one or more (tag, line) pairs

Routing is dynamic and supports:

Fan-out: a line may emit multiple tags

Fan-in: a tag may be emitted from multiple sources

Cycles (with optional safeguards)

The system stops when no lines remain to be processed.

Configuration Format
Processors are defined in a config file:

yaml
Copy code
nodes:
  - tag: start
    type: processors.start.tag_lines
  - tag: error
    type: processors.filters.only_error
  - tag: warn
    type: processors.filters.only_warn
  - tag: general
    type: processors.formatters.snakecase
  - tag: end
    type: processors.output.terminal
Design Notes
Use a dictionary or graph (e.g., networkx.DiGraph) to map tag-to-processor routes.

Each processor implements:
process(lines: Iterator[str]) -> Iterator[Tuple[str, str]]

Validate all emitted tags are registered.

Add optional loop detection or iteration limits.

Example Flow
Line enters at 'start'

Processor emits: ('warn', line)

Line goes to warn processor

Processor emits: ('end', line)

Line exits system

Goals
Decouple routing from processors

Support complex workflows with branching and loops

Prepare system for distributed or stateful extensions