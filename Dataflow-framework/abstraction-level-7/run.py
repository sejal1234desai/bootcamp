# run.py
# run.py

import threading
from app.metrics import MetricsStore
from app.trace import TraceStore
from app.processor_engine import ProcessorEngine
from dashboard.app import run_dashboard, init_dashboard

def run():
    # Shared metrics and trace stores
    metrics_store = MetricsStore()
    trace_store = TraceStore()

    # Initialize dashboard with shared stores
    init_dashboard(metrics_store, trace_store)

    # Start the processor engine
    processor_engine = ProcessorEngine(metrics_store, trace_store)

    # Process some lines
    lines = ["line 1", "line 2", "line 3"]
    processor_engine.process_lines(lines)

    # Start FastAPI dashboard
    processing_thread = threading.Thread(target=run_dashboard)
    processing_thread.start()

if __name__ == "__main__":
    run()
