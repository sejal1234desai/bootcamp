# app/metrics.py
from collections import defaultdict

class MetricsStore:
    def __init__(self):
        self.metrics = {}

    def log_metric(self, processor_name, time_taken_ms, error=False):
        if processor_name not in self.metrics:
            self.metrics[processor_name] = {
                "processed": 0,
                "errors": 0,
                "total_time": 0.0
            }

        self.metrics[processor_name]["processed"] += 1
        self.metrics[processor_name]["total_time"] += time_taken_ms
        if error:
            self.metrics[processor_name]["errors"] += 1

    def get_metrics(self):
        result = {}
        for processor, stats in self.metrics.items():
            avg_time = (stats["total_time"] / stats["processed"]) if stats["processed"] else 0.0
            result[processor] = {
                "processed": stats["processed"],
                "errors": stats["errors"],
                "avg_time_ms": round(avg_time, 2)
            }
        return result
