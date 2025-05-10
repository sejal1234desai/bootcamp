
#!/bin/bash

# A simple script to run the file processor in different modes

# Default to Watch Mode
MODE="watch"

while [[ $# -gt 0 ]]; do
  case "$1" in
    --input)
      MODE="input"
      INPUT_FILE="$2"
      shift 2
      ;;
    --watch)
      MODE="watch"
      shift
      ;;
    *)
      echo "Unknown option $1"
      exit 1
      ;;
  esac
done

# Run in Single File Mode
if [ "$MODE" == "input" ]; then
  if [ -z "$INPUT_FILE" ]; then
    echo "Please provide a file to process with --input"
    exit 1
  fi
  python main.py --input "$INPUT_FILE"

# Run in Watch Mode
elif [ "$MODE" == "watch" ]; then
  python main.py --watch
fi
