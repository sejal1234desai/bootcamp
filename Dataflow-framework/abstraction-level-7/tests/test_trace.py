# tests/test_trace.py
from app.trace import TraceStore
import unittest

class TestTraceStore(unittest.TestCase):
    def test_add_and_get(self):
        trace_store = TraceStore()
        trace_store.add_trace(['start', 'warn'])
        self.assertEqual(trace_store.get_traces(), [['start', 'warn']])

if __name__ == "__main__":
    unittest.main()
