🔹 Daily Log

🗓  Date: May 2, 2025

📚 What I Learned Today:
-Set up GitHub repo bootcamp and added SSH keys for password-less push/pull.
-Installed Python 3.11 & 3.13 using uv and created a virtual env with 3.13.
-Working on WSL (Ubuntu on Windows).
-Set up GCP VM as server; ran a basic web server showing name and photo.
-Faced difficulty in the tools section while uploading files to the server

🗓️  Date: : May 5, 2025

📚 What I Learned Today:
-Studied Python application development lifecycle and best practices like using type hints, modular code, meaningful names, and pyproject.toml.
-Initialized a CLI app using uv, typer, and rich, and published it on TestPyPI.
-Practiced IDE features: type checking, linting, refactoring, and navigation in VS Code.
-Faced difficulty uploading files in Tools section due to WSL and Windows setup differences

🗓️  Date: May 6, 2025
📚 What I Learned Today:
- How to use MkDocs and the Material theme to build documentation sites.
- The structure and purpose of files like README.md, design-doc.md, and login-flow.md.
- Mermaid syntax fo creating sequence diagrams in Markdown.
- Importance of writing clear and simple documentation for your projects.

🤔 What Confused Me:
- At first, it was unclear where each Markdown file should be placed.
- Mermaid syntax was new, especially the sequenceDiagram format.
- Unsure whether I had to recreate README.md or just move it.

💡 How I Resolved It:
- Asked questions and reviewed instructions.
- Practiced by creating simple diagrams first.
- Verified file structure inside the "docs/" folder and used "mkdocs serve" to test.

🧠 Summary:
Today was productive. I understood how to structure project documentation and started seeing the value of writing docs alongside code. It’s not just about writing—it’s about explaining ideas clearly.

📌 Next Goals:
- Update diagrams with more complex flows.
- Improve design-doc with more detailed options and tradeoffs.
- Add more pages like FAQs or Troubleshooting.

🗓  Date: May 7

📚 What I Learned Today:
-Python Practice & Best Practices
-Practiced core Python concepts, CLI with Typer, and package publishing.
-Implemented logging best practices: levels, formatting, contextual info, file logging.
-Improved code clarity: clear naming, small functions, meaningful constants.
-Explored profiling tools: timeit, cProfile, memory_profiler.
-Used debugging tools: pdb, breakpoint(), structured logging.
-Applied design for observability: contextual logs, performance tracking.
-Managed packaging with pyproject.toml, entry points, versioning.


🗓  Date: May 8


📚 What I Learned Today:
Dataflow Framework Progress (Levels 0-8)

Levels 0-6:
-Built core routing engine with tag-based processing
-Implemented processor registration and dynamic flow
-Added config file support for pipeline definitions
-Basic validation for tag-processor mappings

Level 7 (Design Challenges):
-Struggled with infinite cycle detection in routing graphs
-Difficulty visualizing complex flows with networkx
-Tag validation edge cases (orphaned tags, missing targets)
-State management across fan-out/fan-in scenarios

Level 8:
-Focused on observability features
-Implemented metrics counting (lines processed per node)
-Added execution tracing with journey logging
-Basic web dashboard for monitoring

Key Takeaways:
Level 7 exposed gaps in graph theory understanding, especially around cycle detection and dynamic routing validation. The transition from linear processing (levels 0-6) to complex DAGs required significant design iteration.



🗓  Date: May 13

📚 What I Learned Today:

-Persistence & Databases Learning (May 13)
-Core Concepts Covered:

Serialization Techniques:
-Pickle (Person object)
-JSON (Book object)
-YAML (Car object)
-Advanced: Custom serialization, cyclic references, versioning

SQLite Fundamentals:
-CRUD operations
-Transactions & ACID properties
-Batch inserts (500 records)
-Banking/inventory transaction simulations

Advanced Python:
-SQLAlchemy + Pydantic ORM
-Async database operations
-Schema migrations
-Model-API separation

Key Challenges:
-Handling cyclic references in serialization
-Transaction rollback edge cases
-ORM performance with large datasets

Outcome:
Built modular systems for data persistence with file/DB backends, ready for distributed applications.


