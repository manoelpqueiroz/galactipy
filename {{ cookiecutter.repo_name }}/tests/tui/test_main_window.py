# UPDATEME with additional tests for different interactions, see documentation at:
# https://textual.textualize.io/guide/testing/
from {{ cookiecutter.package_name }}.tui.main_window import TerminalApp

{% if cookiecutter.use_bdd -%}
import pytest
from pytest_bdd import scenario, when, then, parsers
{% else -%}
import pytest
{%- endif %}


{% if cookiecutter.use_bdd -%}
@scenario("main_window.feature", "Quit the interface")
@pytest.mark.asyncio
async def test_app_exit():
    pass

@given("the interface is running")
@pytest.mark.asyncio
def running_interface(target_fixture="interface_run"):
    interface = TerminalApp()

    yield interface.run_test()

@when("the user presses `Ctrl+Q`")
@pytest.mark.asyncio
def press_ctrl_q(interface_run):
    async with interface_run as pilot:
        await pilot.press("ctrl+q")

@then("the program is terminated without errors")
@pytest.mark.asyncio
def successful_termination(interface_run):
    assert interface_run.return_code == 0
{%- else -%}
@pytest.mark.asyncio
async def test_app_exit():
    interface = TerminalApp()

    async with interface.run_test() as pilot:
        await pilot.press("ctrl+q")

        assert interface.return_code == 0
{%- endif %}
