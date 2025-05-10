# tests/test_metrics.py
from app.metrics import MetricsStore
import unittest

class TestMetricsStore(unittest.TestCase):
    def test_record_and_get(self):
        metrics = MetricsStore()
        metrics.record('start', 0.1)
        self.assertEqual(metrics.get_metrics()['start']['count'], 1)
        self.assertEqual(metrics.get_metrics()['start']['time'], 0.1)

if __name__ == "__main__":
    unittest.main()
