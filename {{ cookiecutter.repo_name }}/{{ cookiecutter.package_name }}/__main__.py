# type: ignore[attr-defined]
from typing import Optional

from enum import Enum
from random import choice

import typer
from rich.console import Console

from {{ cookiecutter.package_name }} import __version__
from {{ cookiecutter.package_name }}.example import hello


class Color(Enum):
    BLACK = "black"
    WHITE = "white"
    RED = "red"
    CYAN = "cyan"
    MAGENTA = "magenta"
    YELLOW = "yellow"
    GREEN = "green"


app = typer.Typer(
    name="{{ cookiecutter.repo_name }}",
    help="{{ cookiecutter.project_description }}",
    add_completion=False,
)
colour_option = typer.Option(
    None,
    "-c",
    "--color",
    "--colour",
    case_sensitive=False,
    help="Color for print. If not specified then choice will be random.",
)

console = Console()


def version_callback(print_version: bool) -> None:  # noqa: FBT001
    """Print the version of the package.

    """
    if print_version:
        console.print(f"[yellow]{{ cookiecutter.project_name }}[/] version: [bold blue]{__version__}[/]")
        raise typer.Exit


@app.command(name="")
def main(
    name: str = typer.Option(..., help="Person to greet."),
    color: Optional[Color] = colour_option,
    print_version: bool = typer.Option(  # noqa: ARG001, FBT001
        None,
        "-v",
        "--version",
        callback=version_callback,
        is_eager=True,
        help="Prints the version of the {{ cookiecutter.project_name }} package.",
    ),
) -> None:
    """Print a greeting with a giving name.

    """
    if color is None:
        color = choice(list(Color))  # noqa: S311

    greeting = hello(name)
    console.print(f"[bold {color.value}]{greeting}[/]")


if __name__ == "__main__":
    app()
