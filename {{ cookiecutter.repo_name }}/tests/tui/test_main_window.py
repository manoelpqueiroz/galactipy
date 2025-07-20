# UPDATEME with additional tests for different interactions, see documentation at:
# https://textual.textualize.io/guide/testing/
{% if cookiecutter.use_bdd -%}
from pytest_bdd import scenario, given, when, then

from tests.utils.pytest_bdd_async import async_step
from tests.helpers.tui_helpers import AppInterface

{% else -%}
from {{ cookiecutter.package_name }}.tui.main_window import TerminalApp
{%- endif %}


{% if cookiecutter.use_bdd -%}
@scenario("main_window.feature", "Quit the interface")
def test_app_exit():
    pass


@given("the interface is running", target_fixture="interface_run")
def running_interface():
    return AppInterface()


@when("the user presses `Ctrl+Q`")
@async_step
async def press_ctrl_q(interface_run):
    async with interface_run.pilot as pilot:
        await pilot.press("ctrl+q")


@then("the program is terminated without errors")
def successful_termination(interface_run):
    assert interface_run.return_code == 0
{%- else -%}
async def test_app_exit():
    interface = TerminalApp()

    async with interface.run_test() as pilot:
        await pilot.press("ctrl+q")

        assert interface.return_code == 0
{%- endif %}
