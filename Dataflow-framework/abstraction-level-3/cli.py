import typer
from pipeline import load_pipeline_from_config
from core import process_file


app = typer.Typer()

@app.command()
def main(input_file: str, config: str):
    pipeline = load_pipeline_from_config(config)
    process_file(input_file, pipeline,output_file)

if __name__ == "__main__":
    app()
