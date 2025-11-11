"""Provide helper functions for TUI testing."""

from {{ cookiecutter.package_name }}.tui.main_window import TerminalApp


class AppInterface:
    """Encapsulates the terminal interface test setup."""

    def __init__(self, theme):
        """Start a Textual test terminal interface."""
        self.instance = TerminalApp(theme)
        self.pilot = self.instance.run_test()

    @property
    def return_code(self) -> int:
        """Get the return code of the terminal application."""
        return self.instance.return_code
