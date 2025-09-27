from typing import Annotated

from pathlib import Path

import typer
from rich import print

from {{ cookiecutter.package_name }}.config import resolve_app_manager

config_get_app = typer.Typer(no_args_is_help=True)


@config_get_app.command()
def get(
    key: Annotated[
        str, typer.Argument(help="The configuration key to be retrieved.")
    ] = None,
    path: Annotated[
        Path, typer.Option(help="Specify a custom configuration file.")
    ] = None,
    secret: Annotated[
        bool,
        typer.Option(
            "--secret",
            "-s",
            help="Retrieve configuration from the secret manager instead.",
        ),
    ] = False,
):
    """Retrieve a key from the configuration file."""
    config_type, APP_MANAGER = resolve_app_manager(secret, path)

    if key is None:
        print(APP_MANAGER[config_type].to_dict())

    else:
        print(APP_MANAGER[config_type, key])

    raise typer.Exit
