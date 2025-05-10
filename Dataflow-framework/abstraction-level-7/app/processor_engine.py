from app.processor import Processor
from app.metrics import MetricsStore
from app.trace import TraceStore

class ProcessorEngine:
    def __init__(self, metrics_store, trace_store):
        self.metrics_store = metrics_store
        self.trace_store = trace_store

        self.processors = {
            'start': Processor('start', self.metrics_store, self.trace_store),
            'error': Processor('error', self.metrics_store, self.trace_store),
            'warn': Processor('warn', self.metrics_store, self.trace_store),
            'general': Processor('general', self.metrics_store, self.trace_store)
        }

    def process_line(self, line):
        line = self.processors['start'].process(line)
        line = self.processors['general'].process(line)
        return line

    def process_lines(self, lines):
        return [self.process_line(line) for line in lines]
