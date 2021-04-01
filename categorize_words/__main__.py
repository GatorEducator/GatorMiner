"""Command-line interface for the categorize_words program"""

import typer

from categorize_words import categorize_words

# main interface
def main(file: str = typer.Option(...), category: str = typer.Option(...)):
    """Prompt users for the name of the file that words will be categorized from, and the categories to put them in"""
    # display debugging output for the program's command-line arguments
    # welcome message
    typer.echo("Welcome to the Categorize Words program, using GatorMiner")
    typer.echo("")

    # prompt about file selection & command-line response
    typer.echo("What file would you like to select?")
    typer.echo("")
    typer.echo(f"The name of the selected file is {file}!")
    typer.echo("")

    # prompt about categories & command-line response
    typer.echo("What category would you like to group your files under?")
    typer.echo("")
    typer.echo(f"{category} is a category you would like to sort files by.")
    typer.echo(
        "Thank you for using our program, we hope that this was helpful for developing categories for assignments."
        )

if __name__ == "__main__":
    typer.run(main)