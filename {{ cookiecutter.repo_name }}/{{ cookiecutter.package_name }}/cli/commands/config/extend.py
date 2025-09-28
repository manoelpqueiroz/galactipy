"""Append values to existing arrays in the {{ cookiecutter.project_name }} configuration."""

from typing import Annotated

from ast import literal_eval
from pathlib import Path

import typer

from {{ cookiecutter.package_name }}.config import resolve_app_manager

config_extend_app = typer.Typer(no_args_is_help=True)


@config_extend_app.command(name="extend")
def extend_command(
    key: Annotated[str, typer.Argument(help="The configuration key to be extended.")],
    value: Annotated[str, typer.Argument(help="The value to be appended to the key.")],
    path: Annotated[
        Path, typer.Option(help="Specify a custom configuration file.")
    ] = None,
    secret: Annotated[
        bool,
        typer.Option(
            "--secret", "-s", help="Store configuration in the secret manager instead."
        ),
    ] = False,
    create: Annotated[
        bool,
        typer.Option(
            "--create-on-missing",
            "-c",
            help=(
                "Add the provided value in an array if the setting is not set. Will "
                "raise an error otherwise."
            ),
        ),
    ] = False,
):
    """Extend an array key in the configuration file.

    If no setting exists for the key, will create an array with the single value
    provided.
    """
    config_type, APP_MANAGER = resolve_app_manager(secret, path)

    try:
        parsed_value = literal_eval(value)

    except ValueError:
        parsed_value = value

    except (TypeError, SyntaxError):
        typer.echo(f'Could not parse the value "{value}"', err=True)

        raise typer.Exit(1)

    current_setting = APP_MANAGER.get(f"{config_type}.{key}")

    if current_setting is None and create:
        APP_MANAGER[config_type, key] = [parsed_value]

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
        current_setting.append(parsed_value)
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

    raise typer.Exit(exit_code)
