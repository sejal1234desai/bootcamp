
🪢 Level 5 – DAG Routing and Conditional Flows
Welcome to Level 5 of the pipeline processing system. In this level, you're no longer tied to a linear pipeline — instead, you're building a flexible, data-driven engine where each line takes a dynamic path through a Directed Acyclic Graph (DAG) based on tags assigned by processors.

🚀 Goal
To design a configurable and scalable DAG-based routing engine where:

Each processor acts as a node.

Routing decisions are based on tags.

Each line can follow a unique path through the system.

Logic is defined declaratively in a config file.

🧩 Key Features
✅ Tag-based conditional flows
✅ DAG-based routing (no cycles)
✅ Fan-out: One tag → multiple downstream processors
✅ Fan-in: One processor receives input from multiple sources
✅ Config-driven routing logic
✅ Clean separation of routing and processing logic

📁 Project Structure
python
Copy code
abstraction-level-5/
├── cli.py
├── config.yaml           # DAG routing configuration
├── input.txt             # Input data
├── main.py               # Main engine to run the DAG
├── output.txt            # Final processed output
├── pipeline.py           # Core routing engine
├── processor/
│   ├── __init__.py
│   ├── archive.py        # Stores lines to archive
│   ├── count.py          # Counts error lines
│   ├── format.py         # Formats general lines
│   ├── print.py          # Prints to terminal
│   ├── splitter.py       # Splits tags to next processors
│   ├── tag_error.py      # Tags error lines
│   ├── tag_warn.py       # Tags warning lines
│   ├── tally.py          # Tally warnings
│   └── trim.py           # Trims whitespace
├── archive_error.txt     # Stores archived error lines
├── README.md             # You're here!
🛠️ How It Works
Input lines go through the trim processor first.

Lines are tagged using processors like tag_error.py or tag_warn.py.

Routing is determined based on these tags using splitter.py.

Each tag points to different branches:

"errors" → count, archive

"warnings" → tally

"general" → format, print

🧠 Processor Interface
Every processor must implement the following interface:

python
Copy code
def process(lines: Iterator[str]) -> Iterator[Tuple[str, str]]:
    ...
Input: Iterator of raw strings

Output: Iterator of (tag, line) tuples

🧾 Example config.yaml
yaml
Copy code
nodes:
  - name: trim
    type: processor.trim
    next: [tagger]

  - name: tagger
    type: processor.splitter
    next:
      errors: [count, archive]
      warnings: [tally]
      general: [format]

  - name: count
    type: processor.count

  - name: archive
    type: processor.archive

  - name: tally
    type: processor.tally

  - name: format
    type: processor.format
    next: [print]

  - name: print
    type: processor.print
🔄 Routing Logic
Each processor emits tagged lines.

Tags are matched to the next: mapping in the config file.

The engine uses this mapping to forward lines to the appropriate downstream processors.

No cycles are allowed — this is a strict DAG.

✅ Supported Flows:
Fan-out: A tag can route a line to multiple processors.

Fan-in: Multiple processors can emit lines to the same next node.

📌 Usage
CLI
bash
Copy code
python cli.py --config config.yaml --input input.txt
Output
Terminal output is written to output.txt

Archived errors are stored in archive_error.txt

✅ Checklist
 Lines are dynamically routed based on tags

 Routing is defined via config, not hardcoded

 Tags like errors, warnings, general drive flow

 Supports fan-in and fan-out

 Config is YAML and easy to modify

 Fully modular and ready for extension

🤔 Reflection
This architecture allows:

Routing based on content, not structure

Future use cases like error retries, parallel processing, conditional branching

Decoupled design that scales and is easy to test

📦 Next Steps
Move on to Level 6 to implement State-Based Routing with cycles and fully dynamic tag transitions, enabling even more flexible systems like workflow engines or real-time
