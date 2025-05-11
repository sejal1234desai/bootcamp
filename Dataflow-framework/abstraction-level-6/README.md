🧩 Level 6 – State-Based Routing System
Welcome to Level 6 of the processing engine series. This level builds a flexible, tag-based routing system — a foundational abstraction for building event-driven, stateful, and dynamic workflows.

🚀 Overview
In this system, lines are routed not by fixed sequences but by tags that determine which processors handle them next. Each processor operates based on the tag it is registered with and may emit multiple new (tag, line) pairs for downstream processing.

This enables:

Dynamic routing

Fan-in & fan-out

Support for cycles

State-machine-like behavior

📁 File Structure

abstraction-level-6/
│
├── processors/
│   ├── start.py
│   ├── output/
│   │   ├── end.py
│   │   └── __init__.py
│   ├── formatters/
│   │   ├── general.py
│   │   └── __init__.py
│   ├── filters/
│   │   ├── error.py
│   │   ├── warn.py
│   │   └── __init__.py
│   └── __init__.py
│
├── config/
│   └── nodes.yaml
│
├── input/
│   └── input.txt
│
├── cli.py
├── main.py
├── state_engine.py
├── requirements.txt
└── README.md
🛠️ How It Works
Each line begins its journey with the start tag.

Processors are dynamically loaded from the config (config/nodes.yaml).

Each processor emits new (tag, line) tuples.

When a line is tagged with end, it exits the system.

Example configuration (config/nodes.yaml):

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
    type: processors.formatters.general
  - tag: end
    type: processors.output.end
🧠 Key Concepts
Routing Engine (state_engine.py): Core engine managing state transitions.

Dynamic Tags: Lines are routed based on their current tags.

Fan-out: One processor can emit multiple downstream tags.

Fan-in: Multiple processors can emit the same downstream tag.

Cycles Allowed: System supports cycles, but you can add limits or guards to prevent infinite loops.

⚙️ Setup Instructions
1. 🐍 Create a Virtual Environment
bash
Copy code
uv venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
3. 📦 Install Dependencies
bash
Copy code
pip install -r requirements.txt
▶️ Running the Project
bash
Copy code
python main.py --config config/nodes.yaml --input input/input.txt


🖥️ Example Output
Here’s how tagged lines route through processors and exit:


Copy code
Input Line: "Error: Something failed"
  -> start → error → end

Input Line: "Warning: Check this"
  -> start → warn → end

Input Line: "Info: All is well"
  -> start → general → end
  ✅ Features Checklist
 Start → End line routing

 Configurable processors via YAML

 Dynamic tags and transitions

 Supports fan-in and fan-out

 Optional cycle guards

 Modular design and CLI support

📌 Reflection
This level pushes you to think in systems, not scripts. You’ve built a foundation to handle:

Conditional logic

Complex workflows

Potential for distributed execution

🔎 Output Path
Output is printed directly in the console by the processors.output.end processor.

You can modify this processor to write to a file or database, if required.
