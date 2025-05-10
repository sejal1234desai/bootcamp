📁 Level 4 - Stream-Based Processors with State

Description:
This level introduces streaming processors that operate on line iterators. This allows:

Fan-in (many to one)

Fan-out (one to many)

Stateful transformations

Processor Signature Changed:

python
Copy code
ProcessorFn = Callable[[Iterator[str]], Iterator[str]]
Features:

Existing str -> str processors can be adapted using wrappers

Class-based processors can maintain internal state

Configuration can be passed to each processor (like min_length)

Examples of Stream Processors:

Line counter: prefixes each line with line number

Line merger: joins every 2 lines into one

Line splitter: splits a line into multiple based on a delimiter

Notes:

pipeline.yaml format is unchanged for now

Processors can now emit zero, one, or many lines

Design encourages testable, configurable logic

Challenges Solved:

Dynamic behavior

Stateful processing

Reusability of old processors with decorators

Next Steps:

Introduce branching, DAG-style pipelines

Add validation, logging, and plugin support

