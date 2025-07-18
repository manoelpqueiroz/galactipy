# UPDATEME With subcommand apps in `cli/commands/`, see documentation at:
# https://typer.tiangolo.com/tutorial/
# See recommended configuration for multicommand applications at:
# https://typer.tiangolo.com/tutorial/one-file-per-command/#main-module-mainpy
from typing_extensions import Annotated

import typer
from rich import print

from {{ cookiecutter.package_name }} import __version__
{%- if cookiecutter.app_type == 'tui' %}
from {{ cookiecutter.package_name }}.tui.main_window import TerminalApp

app = typer.Typer()
{%- elif cookiecutter.app_type == 'hybrid' %}
from {{ cookiecutter.package_name }}.cli.commands.launch import launch_app

app = typer.Typer(no_args_is_help=True)
app.add_typer(launch_app)
{%- elif cookiecutter.app_type == 'cli' %}

app = typer.Typer(no_args_is_help=True)
{%- endif %}


def version_callback(print_version: bool):
    if print_version:
        print(
            ":package:[yellow]{{ cookiecutter.project_name }}[/] "
            f"[bold green]{__version__}[/]"
        )

        raise typer.Exit()


{% if cookiecutter.app_type == 'tui' -%}
@app.callback(invoke_without_command=True)
def main(
    ctx: typer.Context,
{% elif cookiecutter.app_type == 'hybrid' or cookiecutter.app_type == 'cli' -%}
@app.callback()
def main(
{%- endif %}
    version: Annotated[
        bool,
        typer.Option(
            "--version",
            "-v",
            help="Print the current version of this program and exit.",
            callback=version_callback,
            is_eager=True,
        )
    ] = False,
):
    {%- if cookiecutter.app_type == 'tui' %}
    """Launch the {{ cookiecutter.project_name }} interface.
    """
    if ctx.invoked_subcommand is None:
        interface = TerminalApp()
        interface.run()
    {%- elif cookiecutter.app_type == 'hybrid' or cookiecutter.app_type == 'cli' %}
    """{{ cookiecutter.project_description }}.

    See below for commands and options.
    """
    pass
    {%- endif %}
