"""Remove values from the {{ cookiecutter.project_name }} configuration."""

from typing import Annotated

from pathlib import Path

import typer

from {{ cookiecutter.package_name }}.config import resolve_app_manager

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
):
    """:fire: [red]Remove[/] a top-level key from the configuration."""
    config_type, APP_MANAGER = resolve_app_manager(secret, path)

    APP_MANAGER.unset(f"{config_type}.{key}")
    APP_MANAGER.save(config_type)

    raise typer.Exit
