import argparse

def parse_args():
    parser = argparse.ArgumentParser(description="Stream-based line processor")
    parser.add_argument('--input', type=str, required=True, help="Input file path")
    parser.add_argument('--config', type=str, required=True, help="Dummy config path (unused)")
    parser.add_argument('--output-file', type=str, help="Output file path (optional)")
    return parser.parse_args()
