# sejal_hello/main.py

import typer
from rich.console import Console
from rich.text import Text

# Initialize the Typer app
app = typer.Typer()

# Initialize the Rich console for printing colorful text
console = Console()


@app.command()
def hello(name: str):
    """
    Function to print a greeting message with the variable name
    in green and bold using Rich.
    """
    # Create a Text object for the name with green and bold formatting
    name_text = Text(name, style="bold green")

    # Print the message using Rich
    console.print(f"Hello ", name_text, "!", style="bold")


if __name__ == "__main__":
    app()
