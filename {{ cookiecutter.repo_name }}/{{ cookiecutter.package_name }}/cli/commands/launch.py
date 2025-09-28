"""Launch the {{ cookiecutter.project_name }} interface."""

from pathlib import Path
from typing import Annotated

import typer

from {{ cookiecutter.package_name }}.tui.main_window import TerminalApp
from {{ cookiecutter.package_name }}.config import resolve_app_manager

launch_app = typer.Typer(rich_markup_mode="rich")

@launch_app.command()
def launch(
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
    ] = None
):
    """:pager: Launch the {{ cookiecutter.project_name }} interface."""
    _, APP_MANAGER = resolve_app_manager(False, config)

    interface = TerminalApp(APP_MANAGER.settings.theme)

    interface.run()
