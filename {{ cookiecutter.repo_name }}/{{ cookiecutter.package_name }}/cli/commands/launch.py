import typer

from {{ cookiecutter.package_name }}.tui.main_window import TerminalApp

launch_app = typer.Typer()

@launch_app.command()
def launch():
    """Launch the {{ cookiecutter.project_name }} interface."""
    interface = TerminalApp("noctis")

    interface.run()
