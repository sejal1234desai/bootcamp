from rich.console import Console
from rich.console import Console
from rich.text import Text
import typer

console = Console()

app = typer.Typer()

@app.command()
def say_hello(name: str = "world"):
    """Say hello to the provided name, or 'world' by default."""
    print(f"Received name: {name}")  # Debug line to ensure the argument is passed correctly
    text = Text(f"Hello, {name}!", style="bold green")
    console.print(text)

if __name__ == "__main__":
    app()
