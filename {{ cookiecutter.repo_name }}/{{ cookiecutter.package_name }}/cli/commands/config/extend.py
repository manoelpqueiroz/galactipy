"""Append values to existing arrays in the {{ cookiecutter.project_name }} configuration."""

from typing import Annotated

from pathlib import Path

from nebulog import logger

import typer

from {{ cookiecutter.package_name }}.cli.helpers import BasicConverter as Text
from {{ cookiecutter.package_name }}.config import resolve_app_manager

config_extend_app = typer.Typer(no_args_is_help=True)


HELP_MSG = (
    ":straight_ruler: Extend an array key in the configuration file.\n\n"
    "If no setting exists for the key, you cancreate an array with the single value "
    "provided.\n\n"
    ":rotating_light: [bold red]NOTE:[/] To extend a value in the configuration with a "
    "[b][i]negative[/i][/b] number, you must pass the double dash separator to prevent "
    "the application from interpreting it as a flag:\n\n"
    "[bold yellow]$[/] [green]{{ cookiecutter.repo_name }}[/] config extend somekey "
    "[blue]--[/] -1"
)


@config_extend_app.command(name="extend", help=HELP_MSG)
def extend_command(
    key: Annotated[
        str, typer.Argument(help=":key: The configuration key to be extended.")
    ],
    value: Annotated[
        Text,
        typer.Argument(
            help=":keycap_#: The value to be stored with the key.",
            parser=Text,
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
    create: Annotated[
        bool,
        typer.Option(
            "--create-on-missing",
            "-c",
            help=(
                ":new: Add the provided value in an array if the setting is not set. "
                "Will raise an error otherwise."
            ),
        ),
    ] = False,
):
    """Extend an array key in the configuration file."""
    logger.info(
        "Extending array key via CLI", key=key, value=value.output, is_secret=secret
    )

    if path is not None:  # pragma: no cover
        logger.info("Using custom configuration file", config=path)

    config_type, APP_MANAGER = resolve_app_manager(secret, path)

    if value.output is None:
        typer.echo(f'Could not parse the value "{value.input}"', err=True)

        raise typer.Exit(1)

    current_setting = APP_MANAGER.get(f"{config_type}.{key}")

    if current_setting is None and create:
        APP_MANAGER[config_type, key] = [value.output]

        APP_MANAGER.save(config_type)
        exit_code = 0

    elif current_setting is None:
        typer.echo(
            f"Setting `{key}` was not found, if you wish to update the configuration, "
            "run the command with the `--create-on-missing` option",
            err=True,
        )
        exit_code = 1

    elif isinstance(current_setting, list):
        current_setting.append(value.output)
        APP_MANAGER[config_type, key] = current_setting

        APP_MANAGER.save(config_type)
        exit_code = 0

    else:
        typer.echo(
            f"To extend settings, the value for `{key}` must be an array, got "
            f"{current_setting} instead",
            err=True,
        )
        exit_code = 1

    if exit_code != 0:
        logger.debug("{{ cookiecutter.project_name }} exited successfully")

    else:
        logger.debug("{{ cookiecutter.project_name }} exited with an error")

    raise typer.Exit(exit_code)
