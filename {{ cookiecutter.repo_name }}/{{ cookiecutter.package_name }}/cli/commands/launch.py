"""Launch the {{ cookiecutter.project_name }} interface."""

from typing import Annotated

from pathlib import Path

from nebulog import logger

import typer

from {{ cookiecutter.package_name }}.config import resolve_app_manager
from {{ cookiecutter.package_name }}.logging import setup_app_logging
from {{ cookiecutter.package_name }}.tui.main_window import TerminalApp

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
    ] = None,
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
) -> None:
    """:pager: Launch the {{ cookiecutter.project_name }} interface."""
    setup_app_logging(debug=debug)

    logger.info("Calling {{ cookiecutter.project_name }} via CLI")

    if config is not None:  # pragma: no cover
        logger.info("Using custom configuration file", config=config)

    app_manager = resolve_app_manager("settings", config)

    interface = TerminalApp(app_manager.settings.theme)

    interface.run()

    logger.debug("{{ cookiecutter.project_name }} exited successfully")
