# app/trace.py
class TraceStore:
    def __init__(self):
        self.traces = []

    def log_trace(self, processor_name, input_data, output_data):
        self.traces.append({
            "processor": processor_name,
            "input": input_data,
            "output": output_data
        })

    def get_traces(self):
        return self.traces
