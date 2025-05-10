# tests/test_processor.py
from app.processor import Processor
import unittest

class TestProcessor(unittest.TestCase):
    def test_process_line(self):
        processor = Processor('start')
        result = processor.process('hello')
        self.assertEqual(result, 'HELLO')

if __name__ == "__main__":
    unittest.main()
