import networkx as nx
import importlib

import importlib


class StateMachine:
    def __init__(self, config):
        self.processors = {}

        for node in config['nodes']:
            # Get module and class name from the 'type' field
            module_name, class_name = node['type'].rsplit('.', 1)
            module = importlib.import_module(module_name)
            processor_class = getattr(module, class_name)

            # Store processor class in a dictionary by tag name
            self.processors[node['tag']] = processor_class()

    def run(self, start_tag, lines):
        # This is just an example of how to run the state machine
        current_tag = start_tag
        current_lines = lines

        while current_tag != "end":
            processor = self.processors[current_tag]
            next_lines = processor.process(current_lines)

            # Collect next tags from the processor output
            for next_tag, line in next_lines:
                current_tag = next_tag
                current_lines = [line]  # Assuming each tag processes a single line at a time

            # If we don't have the next tag, we stop
            if current_tag == "end":
                break
