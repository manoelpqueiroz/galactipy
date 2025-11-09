"""Remove values from the {{ cookiecutter.project_name }} configuration."""

from typing import Annotated

from pathlib import Path

from nebulog import logger

import typer

from {{ cookiecutter.package_name }}.config import ConfigurationDomain, resolve_app_manager
from {{ cookiecutter.package_name }}.logging import setup_app_logging

config_unset_app = typer.Typer(no_args_is_help=True)


@config_unset_app.command()
def unset(
    key: Annotated[
        str, typer.Argument(help=":key: The configuration key to be removed.")
    ],
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
) -> None:
    """:fire: [red]Remove[/] a top-level key from the configuration."""
    setup_app_logging(debug=False)
    domain = ConfigurationDomain.from_flag(is_secret=secret)

    logger.info("Removing configuration key via CLI", key=key, is_secret=secret)

    if path is not None:  # pragma: no cover
        logger.info("Using custom configuration file", config=path)

    app_manager = resolve_app_manager(domain, path)

    app_manager.unset(f"{domain.value}.{key}")
    app_manager.save(domain.value)

    logger.debug("{{ cookiecutter.project_name }} exited successfully")
