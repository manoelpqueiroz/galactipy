# UPDATEME with additional tests for each command, see documentation at:
# https://typer.tiangolo.com/tutorial/testing/
from typer.testing import CliRunner

from {{ cookiecutter.package_name }}.cli.root_command import app

{% if cookiecutter.use_bdd -%}
from pytest_bdd import scenario, when, then, parsers
{% else -%}
import pytest
{%- endif %}

runner = CliRunner()


{% if cookiecutter.use_bdd -%}
@scenario("root_command.feature", "Invoke with version argument")
def test_app_with_version_arg():
    pass


@when("the program is called with the `--version` argument", target_fixture="app_run")
def invoke_version_arg():
    return runner.invoke(app, args=["--version"])


@then("the program's version is displayed")
def version_display(app_run, version_string):
    assert app_run.stdout == version_string


@then("the program is terminated without errors")
def successful_termination(app_run):
    assert app_run.exit_code == 0


# TODO replace scenario when new commands are added to the CLI
@scenario("root_command.feature", "Invoke any command")
def test_app_with_any_command():
    pass


@when(
    parsers.parse("the program is called with the {invalid} command"),
    target_fixture="app_run",
)
def invoke_invalid_command(invalid):
    return runner.invoke(app, args=[invalid])


@then("the program is terminated with status 2")
def return_status_2(app_run):
    assert app_run.exit_code == 2
{%- else -%}
def test_app_with_version_arg(version_string):
    result = runner.invoke(app, args=["--version"])

    assert result.stdout == version_string
    assert result.exit_code == 0


# TODO replace this test when new commands are added to the CLI
@pytest.mark.parametrize("invalid", ["any", "some", "testing", "help", "run"])
def test_app_with_any_command(invalid):
    result = runner.invoke(app, args=[invalid])

    assert result.exit_code == 2
{%- endif %}
