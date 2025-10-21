"""Store or override values in the {{ cookiecutter.project_name }} configuration."""

from typing import Annotated

from ast import literal_eval
from pathlib import Path

from nebulog import logger

import typer

from {{ cookiecutter.package_name }}.config import resolve_app_manager
from {{ cookiecutter.package_name }}.logging import setup_app_logging

config_set_app = typer.Typer(no_args_is_help=True)


@config_set_app.command(name="set")
def set_command(
    key: Annotated[
        str, typer.Argument(help=":key: The configuration key to be stored.")
    ],
    value: Annotated[
        str, typer.Argument(help=":keycap_#: The value to be stored with the key.")
    ],
    path: Annotated[
        Path, typer.Option(help=":bus_stop: Specify a custom configuration file.")
    ] = None,
    secret: Annotated[
        bool,
        typer.Option(
            "--secret",
            "-s",
            help=":lock: Store configuration in the secret manager instead.",
        ),
    ] = False,
):
    """:floppy_disk: Store a key in the configuration file."""
    setup_app_logging(debug=False)

    logger.info(
        "Storing configuration key via CLI", key=key, value=value, is_secret=secret
    )

    if path is not None:
        logger.info("Using custom configuration file", config=path)

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

    logger.debug("{{ cookiecutter.project_name }} exited successfully")
