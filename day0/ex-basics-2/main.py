from rich.console import Console
from rich.text import Text

console = Console()

def say_hello(name: str = "world"):
    text = Text(f"Hello, {name}!", style="bold green")
    console.print(text)
