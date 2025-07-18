# UPDATEME With additional components in `tui/components/`
# See Textual documentation at:
# https://textual.textualize.io/tutorial/
from pathlib import Path

from art import text2art

from textual.app import App, ComposeResult
from textual.widgets import Footer, Label


class TerminalApp(App):
    """Textual app to serve as the {{ cookiecutter.project_name }} interface."""

    CSS_PATH = Path(__file__).parent / "css" / "demo.tcss"

    def compose(self) -> ComposeResult:
        """Create child widgets for the app."""
        # UPDATEME by replacing with your own widgets
        yield Label(text2art("{{ cookiecutter.project_name }}", "tarty1"), classes="title")
        yield Label("[i][b]{{ cookiecutter.project_description }}.[/]", classes="description")
        yield Footer()

    def on_mount(self) -> None:
        """Execute instructions when launching the interface."""
        self.theme = "nord"


if __name__ == "__main__":
    app = TerminalApp()
    app.run()
