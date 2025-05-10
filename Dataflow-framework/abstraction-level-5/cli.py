import argparse

def parse_args():
    parser = argparse.ArgumentParser(description="Run the dataflow pipeline.")
    parser.add_argument("--input", required=True, help="Path to input file")
    parser.add_argument("--config", required=True, help="Path to config YAML file")
    return parser.parse_args()
