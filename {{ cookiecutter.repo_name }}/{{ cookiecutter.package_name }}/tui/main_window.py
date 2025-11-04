# UPDATEME With additional components in `tui/components/`
# See Textual documentation at:
# https://textual.textualize.io/tutorial/
"""Assemble a Textual application for a terminal user interface."""

from pathlib import Path

from nebulog import logger

from textual.app import App, ComposeResult
from textual.widgets import Footer, Label

from art import text2art

from {{ cookiecutter.package_name }}.tui.themes import AppCustomThemes

CSS_DIRECTORY = Path(__file__).parent / "css"


class TerminalApp(App):
{%- if cookiecutter.docstring_style != 'other' %}
    """Textual app to serve as the {{ cookiecutter.project_name }} interface.
{%- if cookiecutter.docstring_style == 'numpy' %}

    Parameters
    ----------
    theme : str
        Theme name to launch the application with.
{%- elif cookiecutter.docstring_style == 'google' %}

    Args:
        theme: Theme name to launch the application with.
{%- else %}

    :param theme: Theme name to launch the application with.
    :type theme: str
{%- endif %}
    """
{%- else %}
    """Textual app to serve as the {{ cookiecutter.project_name }} interface."""
{%- endif %}

    CSS_PATH = [
        CSS_DIRECTORY / "demo.tcss",  # UPDATEME by removing when no longer needed
        CSS_DIRECTORY / "noctis.tcss",
    ]

    def __init__(self, theme: str):
        """Initialise the Terminal User Interface."""
        super().__init__()

        logger.info("Launching {{ cookiecutter.project_name }} TUI", theme=theme)
        self.default_theme = theme

    def compose(self) -> ComposeResult:
        """Create child widgets for the app."""
        # UPDATEME by replacing with your own widgets
        yield Label(text2art("{{ cookiecutter.project_name }}", "tarty1"), classes="title")
        yield Label("[i][b]{{ cookiecutter.project_description }}.[/]", classes="description")
        yield Footer()

    def on_mount(self) -> None:
        """Execute instructions when launching the interface."""
        logger.info("Mounting the application interface")

        for theme in AppCustomThemes:
            self.register_theme(theme.value)

        self.theme = self.default_theme


if __name__ == "__main__":
    app = TerminalApp("noctis")
    app.run()
