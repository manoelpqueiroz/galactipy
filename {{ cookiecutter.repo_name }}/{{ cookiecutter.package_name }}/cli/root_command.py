# UPDATEME With subcommand apps in `cli/commands/`, see documentation at:
# https://typer.tiangolo.com/tutorial/
# See recommended configuration for multicommand applications at:
# https://typer.tiangolo.com/tutorial/one-file-per-command/#main-module-mainpy
"""{{ cookiecutter.project_description }}."""

from typing import Annotated
{% if cookiecutter.app_type == 'tui' %}
from pathlib import Path

{% endif -%}
import typer
from rich.console import Console

from {{ cookiecutter.package_name }} import __version__
from {{ cookiecutter.package_name }}.cli.commands.config import config_app
from {{ cookiecutter.package_name }}.cli.styles import AppCustomStyles
{%- if cookiecutter.app_type == 'tui' %}
from {{ cookiecutter.package_name }}.config import resolve_app_manager
from {{ cookiecutter.package_name }}.tui.main_window import TerminalApp

app = typer.Typer(rich_markup_mode="rich")
{%- elif cookiecutter.app_type == 'hybrid' %}
from {{ cookiecutter.package_name }}.cli.commands.launch import launch_app

app = typer.Typer(no_args_is_help=True, rich_markup_mode="rich")
app.add_typer(launch_app)
{%- elif cookiecutter.app_type == 'cli' %}

app = typer.Typer(no_args_is_help=True, rich_markup_mode="rich")
{%- endif %}
app.add_typer(config_app, name="config")


def version_callback(print_version: bool):
    if print_version:
        Console(theme=AppCustomStyles.NOCTIS).print(
            ":package:[declaration]{{ cookiecutter.project_name }}[/] "
            f"[bold fstring]{__version__}[/]"
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
{% elif cookiecutter.app_type == 'hybrid' or cookiecutter.app_type == 'cli' -%}
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
):
    {%- if cookiecutter.app_type == 'tui' %}
    """:pager: Launch the {{ cookiecutter.project_name }} interface."""
    if ctx.invoked_subcommand is None:
        _, APP_MANAGER = resolve_app_manager(False, config)

        interface = TerminalApp(APP_MANAGER.settings.theme)
        interface.run()
    {%- elif cookiecutter.app_type == 'hybrid' or cookiecutter.app_type == 'cli' %}
    """{{ cookiecutter.project_description }}.

    See below for commands and options.
    """
    pass
    {%- endif %}
