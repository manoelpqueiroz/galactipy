from ast import literal_eval
from pathlib import Path
from typing import Annotated

import typer

from {{ cookiecutter.package_name }}.config import resolve_app_manager

config_set_app = typer.Typer(no_args_is_help=True)

@config_set_app.command(name="set")
def set_command(
    key: Annotated[str, typer.Argument(help="The configuration key to be stored.")],
    value: Annotated[str, typer.Argument(help="The value to be stored with the key.")],
    path: Annotated[
        Path, typer.Option(help="Specify a custom configuration file.")
    ] = None,
    secret: Annotated[
        bool,
        typer.Option(
            "--secret",
            "-s",
            help="Store configuration in the secret manager instead."
        ),
    ] = False,
):
    """Store a key in the configuration file."""
    config_type, APP_MANAGER = resolve_app_manager(secret, path)

    try:
        parsed_value = literal_eval(value)

    except ValueError:
        parsed_value = value

    except (TypeError, SyntaxError):
        typer.echo(f'Could not parse the value "{value}"', err=True)

        raise typer.Exit(1)

    try:  # Used to convert "true" and "false" strings to boolean variables
        parsed_value = literal_eval(value.capitalize())

    except ValueError:
        parsed_value = value

    APP_MANAGER[config_type, key] = parsed_value
    APP_MANAGER.save(config_type)

    raise typer.Exit
