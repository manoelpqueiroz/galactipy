# UPDATEME with additional tests for each command, see documentation at:
# https://typer.tiangolo.com/tutorial/testing/
from typer.testing import CliRunner

{% if cookiecutter.use_bdd -%}
from pytest_bdd import parsers, scenario, then, when
{% else -%}
import pytest
{%- endif %}

from {{ cookiecutter.package_name }}.cli.root_command import app

runner = CliRunner()


{% if cookiecutter.use_bdd -%}
@scenario("root_command.feature", "Check program version")
def test_cli_with_version_arg():
    pass


@when("the root program receives the `--version` option", target_fixture="cli_run")
def invoke_version_arg():
    return runner.invoke(app, args=["--version"])


@then("the terminal displays the program's version")
def version_display(cli_run, version_string):
    assert cli_run.stdout == version_string


@then("the program exits without errors")
def successful_termination(cli_run):
    assert cli_run.exit_code == 0


@scenario("root_command.feature", "Call invalid command")
def test_cli_with_invalid_command():
    pass


@when(
    parsers.parse("the {command} program receives no arguments"),
    target_fixture="cli_run",
)
def invoke_invalid_command(command):
    return runner.invoke(app, args=[command])


@then("the program exits with status 2")
def return_status_2(cli_run):
    assert cli_run.exit_code == 2


@scenario("root_command.feature", "Call valid command group")
def test_cli_with_valid_command():
    pass


@then(parsers.parse("the terminal displays the help menu for {command}"))
def valid_command_menu(cli_run, command):
    assert f"Usage: root {command}" in cli_run.output
    assert cli_run.exit_code == 0
{%- else -%}
@pytest.mark.cli
@pytest.mark.standard
def test_cli_with_version_arg(version_string):
    result = runner.invoke(app, args=["--version"])

    assert result.stdout == version_string
    assert result.exit_code == 0


@pytest.mark.cli
@pytest.mark.edge
@pytest.mark.parametrize("invalid", ["any", "some", "testing", "help", "run"])
def test_cli_with_invalid_command(invalid):
    result = runner.invoke(app, args=[invalid])

    assert result.exit_code == 2


# UPDATEME when new command groups are added to the CLI
@pytest.mark.cli
@pytest.mark.standard
@pytest.mark.parametrize("valid", ["config"])
def test_cli_with_valid_command(valid):
    result = runner.invoke(app, args=[valid])

    assert f"Usage: root {valid}" in result.output
    assert result.exit_code == 0
{%- endif %}
