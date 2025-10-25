"""Retrieve existing values from the {{ cookiecutter.project_name }} configuration."""

from typing import Annotated

from pathlib import Path

from nebulog import logger

import typer

from {{ cookiecutter.package_name }}.cli.helpers import pretty_print_setting
from {{ cookiecutter.package_name }}.config import resolve_app_manager

config_get_app = typer.Typer(no_args_is_help=True)


@config_get_app.command()
def get(
    key: Annotated[
        str, typer.Argument(help=":key: The configuration key to be retrieved.")
    ] = None,
    path: Annotated[
        Path, typer.Option(help=":bus_stop: Specify a custom configuration file.")
    ] = None,
    secret: Annotated[
        bool,
        typer.Option(
            "--secret",
            "-s",
            help=":lock: Retrieve configuration from the secret manager instead.",
        ),
    ] = False,
):
    """:inbox_tray: Retrieve a key from the configuration file."""
    logger.info("Retrieving configuration key via CLI", key=key, is_secret=secret)

    if path is not None:  # pragma: no cover
        logger.info("Using custom configuration file", config=path)

    config_type, APP_MANAGER = resolve_app_manager(secret, path)

    pretty_print_setting(APP_MANAGER, key, config_type)

    logger.debug("{{ cookiecutter.project_name }} exited successfully")
