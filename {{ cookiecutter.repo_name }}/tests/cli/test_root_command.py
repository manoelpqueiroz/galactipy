# UPDATEME with additional tests for each command, see documentation at:
# https://typer.tiangolo.com/tutorial/testing/
from typer.testing import CliRunner
from rich.text import Text

from {{ cookiecutter.package_name }}.cli.root_command import app

runner = CliRunner()

def test_version():
    result = runner.invoke(app, ["--version"])
    assertion_string = Text.from_markup(
        ":package: {{ cookiecutter.project_name}} 0.0.0\n"
    )

    assert result.exit_code == 0
    assert result.stdout == assertion_string.plain
