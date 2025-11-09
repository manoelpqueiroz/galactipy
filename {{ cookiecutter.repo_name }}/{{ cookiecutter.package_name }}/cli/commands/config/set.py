"""Store or override values in the {{ cookiecutter.project_name }} configuration."""

from typing import Annotated

from pathlib import Path

from nebulog import logger

import typer

from {{ cookiecutter.package_name }}.cli.helpers import BasicConverter as Text
from {{ cookiecutter.package_name }}.config import (
    ConfigurationDomain,
    resolve_app_manager,
)
from {{ cookiecutter.package_name }}.logging import setup_app_logging

config_set_app = typer.Typer(no_args_is_help=True)


HELP_MSG = (
    ":floppy_disk: Store a key in the configuration file.\n\n"
    ":rotating_light: [bold red]NOTE:[/] To store a [b][i]negative[/i][/b] number in "
    "the configuration, you must pass the double dash separator to prevent the "
    "application from interpreting the value as a flag:\n\n"
    "[bold yellow]$[/] [green]{{ cookiecutter.repo_name }}[/] config set somekey "
    "[blue]--[/] -1"
)


@config_set_app.command(name="set", help=HELP_MSG)
def set_command(
    key: Annotated[
        str, typer.Argument(help=":key: The configuration key to be stored.")
    ],
    value: Annotated[
        Text,
        typer.Argument(
            help=":keycap_#: The value to be stored with the key.", parser=Text
        ),
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
) -> None:
    """Store a key in the configuration file."""
    setup_app_logging(debug=False)
    domain = ConfigurationDomain.from_flag(is_secret=secret)

    logger.info(
        "Storing configuration key via CLI",
        key=key,
        value=value.output,
        is_secret=secret,
    )

    if path is not None:  # pragma: no cover
        logger.info("Using custom configuration file", config=path)

    app_manager = resolve_app_manager(domain, path)

    if value.output is None:
        typer.echo(f'Could not parse the value "{value.input}"', err=True)

        raise typer.Exit(1)

    app_manager[domain.value, key] = value.output
    app_manager.save(domain.value)

    logger.debug("{{ cookiecutter.project_name }} exited successfully")
