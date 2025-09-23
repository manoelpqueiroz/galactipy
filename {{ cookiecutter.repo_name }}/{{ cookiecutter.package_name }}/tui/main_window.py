# UPDATEME With additional components in `tui/components/`
# See Textual documentation at:
# https://textual.textualize.io/tutorial/
from pathlib import Path

from art import text2art

from textual.app import App, ComposeResult
from textual.widgets import Footer, Label

from {{ cookiecutter.package_name }}.tui.themes import AppCustomThemes


CSS_DIRECTORY = Path(__file__).parent / "css"

class TerminalApp(App):
    """Textual app to serve as the {{ cookiecutter.project_name }} interface."""

    CSS_PATH = [
        CSS_DIRECTORY / "demo.tcss", # UPDATEME by removing when no longer needed
        CSS_DIRECTORY / "noctis.tcss",
    ]

    def __init__(self, theme: str):
        super().__init__()
        self.default_theme = theme

    def compose(self) -> ComposeResult:
        """Create child widgets for the app."""
        # UPDATEME by replacing with your own widgets
        yield Label(text2art("{{ cookiecutter.project_name }}", "tarty1"), classes="title")
        yield Label("[i][b]{{ cookiecutter.project_description }}.[/]", classes="description")
        yield Footer()

    def on_mount(self) -> None:
        """Execute instructions when launching the interface."""
        for theme in AppCustomThemes:
            self.register_theme(theme.value)

        self.theme = self.default_theme


if __name__ == "__main__":
    app = TerminalApp("noctis")
    app.run()
