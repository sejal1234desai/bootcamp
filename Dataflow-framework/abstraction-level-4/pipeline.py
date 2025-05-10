from typing import Iterator, Callable, List

def build_pipeline(processors):
    def pipeline(input_lines):
        for processor in processors:
            input_lines = processor(input_lines)
        return input_lines
    return pipeline

