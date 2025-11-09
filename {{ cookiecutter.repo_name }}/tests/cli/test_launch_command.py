from typer.testing import CliRunner

{% if cookiecutter.use_bdd -%}
from pytest_bdd import scenario, then, when
{%- else -%}
import pytest
{%- endif %}

from {{ cookiecutter.package_name }}.cli.commands.launch import launch_app

runner = CliRunner()


{% if cookiecutter.use_bdd -%}
@scenario("launch_command.feature", "Launch application from CLI")
def test_launch_app():
    pass


@when("the launch program receives no arguments", target_fixture="results")
def launch_application(mocker, sandbox_config_file):
    mock_interface = mocker.patch(
        "python_project.cli.commands.launch.TerminalApp"
    ).return_value

    results = runner.invoke(launch_app, args=["--config", sandbox_config_file])

    return {"cli_run": results, "interface": mock_interface}


@then("the terminal launches the TUI interface")
def ensure_launch_tui(results):
    results["interface"].run.assert_called_once()


@then("the program exits without errors")
def successful_termination(results):
    assert results["cli_run"].exit_code == 0
{%- else -%}
@pytest.mark.cli
@pytest.mark.frontend
@pytest.mark.standard
def test_launch_app(mocker, setup_sample_manager):
    _, file = setup_sample_manager.values()

    mock_interface = mocker.patch(
        "python_project.cli.commands.launch.TerminalApp"
    ).return_value

    results = runner.invoke(launch_app, args=["--config", file])

    mock_interface.run.assert_called_once()
    assert results.exit_code == 0
{%- endif %}
