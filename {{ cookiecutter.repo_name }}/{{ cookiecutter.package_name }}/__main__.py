{%- if cookiecutter.app_type == 'tui' or cookiecutter.app_type == 'hybrid' %}
"""Launch the {{ cookiecutter.project_name }} interface as a module script."""

from {{ cookiecutter.package_name }}.config import AppManager
from {{ cookiecutter.package_name }}.tui.main_window import TerminalApp

APP_MANAGER = AppManager.default()

app = TerminalApp(APP_MANAGER.settings.theme)
app.run()
{%- elif cookiecutter.app_type == 'cli' %}
"""Run the {{ cookiecutter.project_name }} commands in a module script."""

from {{ cookiecutter.package_name }}.cli.root_command import app

app(prog_name="{{ cookiecutter.repo_name }}-mod")
{%- endif %}
