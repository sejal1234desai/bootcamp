import argparse
import yaml
from state_machine import StateMachine

def load_config(config_file):
    with open(config_file, 'r') as file:
        return yaml.safe_load(file)

def load_input(input_file):
    with open(input_file, 'r') as file:
        return file.readlines()

def main():
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description='State-based routing system.')
    parser.add_argument('--input', type=str, required=True, help='Path to the input file')
    parser.add_argument('--config', type=str, required=True, help='Path to the configuration file')
    args = parser.parse_args()

    # Load the configuration and input
    config = load_config(args.config)
    input_lines = load_input(args.input)

    # Initialize the state machine
    state_machine = StateMachine(config)

    # Run the state machine starting from the 'start' tag
    state_machine.run(start_tag='start', lines=input_lines)

if __name__ == "__main__":
    main()
