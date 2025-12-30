# UPDATEME With subcommand apps in `cli/commands/`, see documentation at:
# https://typer.tiangolo.com/tutorial/
# See recommended configuration for multicommand applications at:
# https://typer.tiangolo.com/tutorial/one-file-per-command/#main-module-mainpy
"""{{ cookiecutter.project_description }}."""

from typing import Annotated
{%- if cookiecutter.app_type == 'tui' %}

from pathlib import Path

from nebulog import logger
{%- endif %}

import typer
from rich.console import Console

from {{ cookiecutter.package_name }}._version import __version__
from {{ cookiecutter.package_name }}.cli.commands.config import config_app
{%- if cookiecutter.app_type == 'tui' %}
from {{ cookiecutter.package_name }}.cli.styling import AppCustomThemes
from {{ cookiecutter.package_name }}.config import resolve_app_manager
from {{ cookiecutter.package_name }}.logging import setup_app_logging
from {{ cookiecutter.package_name }}.tui.main_window import TerminalApp

app = typer.Typer(rich_markup_mode="rich")
{%- elif cookiecutter.app_type == 'hybrid' %}
from {{ cookiecutter.package_name }}.cli.commands.launch import launch_app
from {{ cookiecutter.package_name }}.cli.styling import AppCustomThemes

app = typer.Typer(no_args_is_help=True, rich_markup_mode="rich")
app.add_typer(launch_app)
{%- elif cookiecutter.app_type == 'cli' %}
from {{ cookiecutter.package_name }}.cli.styling import AppCustomThemes

app = typer.Typer(no_args_is_help=True, rich_markup_mode="rich")
{%- endif %}
app.add_typer(config_app, name="config")


def version_callback(print_version: bool) -> None:
    """Print the program version in a Rich console with the Noctis theme."""
    if print_version:
        Console(theme=AppCustomThemes.NOCTIS).print(
            f":package:[declaration]{{ cookiecutter.project_name }}[/] [bold fstring]{__version__}[/]"
        )

        raise typer.Exit


{% if cookiecutter.app_type == 'tui' -%}
@app.callback(invoke_without_command=True)
def main(
    ctx: typer.Context,
    config: Annotated[
        Path,
        typer.Option(
            "--config",
            "-c",
            help=(
                ":bus_stop: Specify a custom configuration file to launch the "
                "application."
            ),
        ),
    ] = None,
{%- elif cookiecutter.app_type == 'hybrid' or cookiecutter.app_type == 'cli' -%}
@app.callback()
def main(
{%- endif %}
    version: Annotated[
        bool,
        typer.Option(
            "--version",
            "-v",
            help=":bulb: Print the current version of this program and exit.",
            callback=version_callback,
            is_eager=True,
        ),
    ] = False,
{%- if cookiecutter.app_type == 'tui' %}
    debug: Annotated[
        bool,
        typer.Option(
            "--debug",
            "-d",
            help=(
                ":bug: Log operations to the terminal at the "
                "[b][logging.level.debug]DEBUG[/logging.level.debug][/b] level."
            ),
        ),
    ] = False,
{%- endif %}
) -> None:
    {%- if cookiecutter.app_type == 'tui' %}
    """:pager: Launch the {{ cookiecutter.project_name }} interface."""
    setup_app_logging(debug=debug)

    if ctx.invoked_subcommand is None:
        logger.info("Calling {{ cookiecutter.project_name }} via CLI")

        if config is not None:  # pragma: no cover
            logger.info("Using custom configuration file", config=config)

        app_manager = resolve_app_manager("settings", config)

        interface = TerminalApp(app_manager.settings.theme)
        interface.run()

        logger.debug("{{ cookiecutter.project_name }} exited successfully")
    {%- elif cookiecutter.app_type == 'hybrid' or cookiecutter.app_type == 'cli' %}
    """{{ cookiecutter.project_description }}.

    See below for commands and options.
    """
    pass
    {%- endif %}
