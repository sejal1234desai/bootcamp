import importlib
import yaml
from typing import Callable


# Function to load processors from a config file
def load_pipeline_from_config(config_file: str) -> list[Callable]:
    with open(config_file, "r") as file:
        config = yaml.safe_load(file)

    pipeline = []
    for step in config.get('pipeline', []):
        # Get the full import path of the processor function
        processor_path = step.get("type")
        if processor_path:
            module_name, function_name = processor_path.rsplit('.', 1)
            try:
                # Dynamically import the function
                module = importlib.import_module(module_name)
                processor_function = getattr(module, function_name)
                pipeline.append(processor_function)
            except (ModuleNotFoundError, AttributeError) as e:
                print(f"Error loading function {processor_path}: {e}")
                raise
    return pipeline
