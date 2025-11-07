# UPDATEME with additional tests for each command, see documentation at:
# https://typer.tiangolo.com/tutorial/testing/
from typer.testing import CliRunner

{% if cookiecutter.use_bdd -%}
from pytest_bdd import parsers, scenario, then, when
{% else -%}
import pytest
{%- endif %}

from {{ cookiecutter.package_name }}.cli.commands.root_command import app

runner = CliRunner()


{% if cookiecutter.use_bdd -%}
{% if cookiecutter.app_type == 'tui' -%}
@scenario("root_command.feature", "Launch application from CLI")
def test_launch_app():
    pass


@when("the program receives no arguments", target_fixture="results")
def launch_application(mocker, sandbox_config_file):
    mock_interface = mocker.patch(
        "python_project.cli.commands.root_command.TerminalApp"
    ).return_value

    results = runner.invoke(app, args=["--config", sandbox_config_file])

    return {"cli_run": results, "interface": mock_interface}


@then("the terminal launches the TUI interface")
def ensure_launch_tui(results):
    results["interface"].run.assert_called_once()


@then("the program exits successfully")
def successful_termination_results(results):
    assert results["cli_run"].exit_code == 0


{% endif -%}
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
def successful_termination_run(cli_run):
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
{% if cookiecutter.app_type == 'tui' -%}
@pytest.mark.cli
@pytest.mark.frontend
@pytest.mark.standard
def test_launch_app(mocker, setup_sample_manager):
    manager, file = setup_sample_manager.values()

    mock_interface = mocker.patch(
        "python_project.cli.commands.root_command.TerminalApp"
    ).return_value

    results = runner.invoke(app, args=["--config", file])

    mock_interface.run.assert_called_once()
    results.exit_code == 0


{% endif -%}
@pytest.mark.cli
@pytest.mark.standard
def test_cli_with_version_arg(version_string):
    result = runner.invoke(app, args=["--version"])

    assert result.stdout == version_string
    assert result.exit_code == 0


@pytest.mark.cli
@pytest.mark.edge
@pytest.mark.parametrize("invalid", ("any", "some", "testing", "help", "run"))
def test_cli_with_invalid_command(invalid):
    result = runner.invoke(app, args=[invalid])

    assert result.exit_code == 2


# UPDATEME when new command groups are added to the CLI
@pytest.mark.cli
@pytest.mark.standard
@pytest.mark.parametrize("valid", ("config",))
def test_cli_with_valid_command(valid):
    result = runner.invoke(app, args=[valid])

    assert f"Usage: root {valid}" in result.output
    assert result.exit_code == 0
{%- endif %}
