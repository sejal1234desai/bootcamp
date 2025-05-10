import sys
from main import main

if __name__ == "__main__":
    # Forward the command-line arguments to main.py
    sys.argv = sys.argv[1:]  # Remove the script name from sys.argv
    main()
