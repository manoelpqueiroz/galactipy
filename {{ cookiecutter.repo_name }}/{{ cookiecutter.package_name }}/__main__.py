{%- if cookiecutter.app_type == 'tui' or cookiecutter.app_type == 'hybrid' %}
from {{ cookiecutter.package_name }}.tui.main_window import TerminalApp

app = TerminalApp()
app.run()
{%- elif cookiecutter.app_type == 'cli' %}
from {{ cookiecutter.package_name }}.cli.root_command import app

app(prog_name="{{ cookiecutter.repo_name }}-mod")
{%- endif %}
