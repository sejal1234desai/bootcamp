📘 Level 4 – Stream Processing and Stateful Processors
Welcome to Level 4 of your pipeline abstraction journey! This level transforms your system from simple, stateless string processors to a stream-based processing engine capable of handling real-world data complexity through:

Streaming

Stateful logic

Fan-in/Fan-out

Reusability of earlier processors

🚀 What’s New in Level 4
✅ Streaming Interface
Processors now handle streams of lines:

python
Copy code
from typing import Iterator

def process(lines: Iterator[str]) -> Iterator[str]:
    ...
This shift enables:

Emitting zero, one, or many lines per input

Maintaining internal state across lines

Composing more complex transformations

🔧 Key Features
🧠 Stateful Processors
Processors can now remember information across lines (e.g., counters, buffers).

🔀 Fan-in and Fan-out
Fan-in: Combine multiple lines into one (e.g., join_pairs)

Fan-out: Split one line into many (e.g., splitter)

⚙️ Configurable Initialization
Processors accept parameters like min_length=5 via configuration injection.

♻️ Legacy Support via Decorators
You can reuse existing str -> str processors by wrapping them:

python
Copy code
@stream_adapter
def to_upper(line: str) -> str:
    return line.upper()
🛠 Folder Structure
bash
Copy code
abstraction-level-4/
│
├── cli.py                 # Command-line interface
├── input.txt              # Sample input file
├── main.py                # Entry point
├── output.txt             # Output after processing
├── pipeline.py            # Core pipeline logic
├── pipeline.yaml          # Processor configuration
├── README.md              # You're reading it!
│
├── processors/            # All processors
│   ├── __init__.py
│   ├── decorator.py       # Wrapper for old processors
│   ├── join_pairs.py      # Fan-in processor
│   ├── line_counter.py    # Stateful processor
│   ├── snake.py           # Snake_case formatter
│   ├── splitter.py        # Fan-out processor
│   └── upper.py           # Uppercase processor
│
└── test/                  # Unit tests
    └── test_processors.py
⚗️ Example Processors
line_counter.py (stateful)
Prefixes each line with its line number.

join_pairs.py (fan-in)
Combines every two lines into one.

splitter.py (fan-out)
Splits a line into words (or by delimiter).

upper.py and snake.py (stateless)
Transform text to uppercase or snake_case.

🔧 Config File (pipeline.yaml)
yaml
Copy code
pipeline:
  - name: line_counter
    type: processors.line_counter.LineCounter

  - name: splitter
    type: processors.splitter.LineSplitter
    config:
      delimiter: " "

  - name: upper
    type: processors.upper.to_upper
✅ Implementation Checklist
 All processors now use Iterator[str] -> Iterator[str]

 Decorator to wrap legacy str -> str functions

 At least one stateful processor (e.g., LineCounter)

 At least one processor with fan-in or fan-out

 Config injection to processors

 Unit tests for processors

 Works with unchanged pipeline.yaml

🧪 Testability
Each processor can be tested independently using standard Python unit tests.

python
Copy code
from processors.line_counter import LineCounter

def test_line_counter():
    lines = iter(["hello", "world"])
    processor = LineCounter()
    output = list(processor.process(lines))
    assert output == ["1: hello", "2: world"]
⏭️ What's Next
Level 5: DAG-based dynamic routing with tagged output

Flexible pipelines where each line can take its own path

Real-world routing logic based on content or type
