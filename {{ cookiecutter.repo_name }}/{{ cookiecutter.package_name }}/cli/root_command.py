# UPDATEME With subcommand apps in `cli/commands/`, see documentation at:
# https://typer.tiangolo.com/tutorial/
# See recommended configuration for multicommand applications at:
# https://typer.tiangolo.com/tutorial/one-file-per-command/#main-module-mainpy
from typing_extensions import Annotated

import typer
from rich import print

from {{ cookiecutter.package_name }} import __version__

app = typer.Typer(no_args_is_help=True)


def version_callback(print_version: bool):
    if print_version:
        print(
            ":package: [yellow]{{ cookiecutter.project_name }}[/] "
            f"[bold green]{__version__}[/]"
        )

        raise typer.Exit()


@app.callback()
def main(
    version: Annotated[
        bool,
        typer.Option(
            "--version",
            "-v",
            help="Print the current version of this program and exit.",
            callback=version_callback,
            is_eager=True,
        )
    ] = False,
):
    """{{ cookiecutter.project_description }}

    See usage below for commands and options.
    """
    pass
