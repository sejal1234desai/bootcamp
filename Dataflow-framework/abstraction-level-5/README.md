Level 5 – DAG Routing and Conditional Flows
In this level, the pipeline supports dynamic routing using a DAG (Directed Acyclic Graph). Each processor can emit tagged lines, and routing is based on these tags rather than a fixed sequence.

This enables each input line to take a different path through the system depending on its content or assigned tags.

Requirements
Each processor is defined as a node in a DAG.

The system routes lines based on the (tag, line) output of each processor.

The routing graph is defined in a config file.

A processor can:

Emit multiple tags (fan-out)

Receive lines from multiple processors (fan-in)

The DAG must not contain cycles.

Processor Interface
Each processor implements:

python
Copy code
def process(lines: Iterator[str]) -> Iterator[Tuple[str, str]]:
    ...
Processors receive untagged lines as input, and emit (tag, line) pairs for routing.

Configuration Format
yaml
Copy code
nodes:
  - name: trim
    type: processors.base.trim
    next: [tagger]

  - name: tagger
    type: processors.tagging.tag_error_warn
    next:
      errors: [count, archive]
      warnings: [tally]
      general: [format]

  - name: count
    type: processors.metrics.counter

  - name: archive
    type: processors.output.store

  - name: tally
    type: processors.metrics.tally

  - name: format
    type: processors.formatters.snakecase
    next: [print]

  - name: print
    type: processors.output.terminal
Routing Rules
The engine uses next: mappings in the config to determine downstream nodes.

Tags emitted by a processor must match a next: key.

Routing supports branching and merging paths.

Goals
Handle conditional flows based on line content or tags.

Separate processing logic from routing logic.

Support real-world pipelines with mixed data types.