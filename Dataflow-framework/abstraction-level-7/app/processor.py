import time

class Processor:
    def __init__(self, name, metrics_store, trace_store):
        self.name = name
        self.metrics = metrics_store
        self.trace = trace_store

    def process(self, line):
        start_time = time.time()

        try:
            time.sleep(0.1)  # Simulate processing
            processed_line = line.upper()
            error_occurred = False
        except Exception:
            processed_line = line
            error_occurred = True

        time_taken_ms = (time.time() - start_time) * 1000

        # Log metrics and trace
        self.metrics.log_metric(self.name, time_taken_ms, error=error_occurred)
        self.trace.log_trace(self.name, input_data=line, output_data=processed_line)

        return processed_line
