{% if cookiecutter.use_bdd -%}
import asyncio

{%- endif %}
from rich.text import Text

import pytest
{%- if cookiecutter.use_bdd %}
from pytest_bdd import given
{%- endif %}

from {{ cookiecutter.package_name }}.config.manager import AppManager


@pytest.fixture
def version_string():
    """Define the expected version string to be printed to STDOUT."""
    return Text.from_markup(":package:{{ cookiecutter.project_name}} 0.0.0\n").plain


@pytest.fixture
def mock_config_path(mocker, tmp_path):
    """Mock platformdirs across tests for the configuration file."""
    config_dir = tmp_path / ".config" / "{{ cookiecutter.repo_name }}"
    config_dir.mkdir(parents=True)

    mocker.patch(
        "{{ cookiecutter.package_name }}.config.manager.get_default_config",
        return_value=config_dir
    )

    return config_dir


@pytest.fixture
def valid_config_data():
    return {"VERSION": "0.0.0", "THEME": "noctis"}


@pytest.fixture
{%- if cookiecutter.use_bdd %}
@given("a valid configuration file", target_fixture="valid_config_manager")
{%- endif %}
def generate_test_config(mock_config_path):
    manager = AppManager.default()

    settings_file = mock_config_path / "settings.toml"
    secrets_file = mock_config_path / "secrets.toml"

    assert settings_file.exists()
    assert secrets_file.exists()

    return {"instance": manager, "file": settings_file}
{%- if cookiecutter.use_bdd %}


@pytest.fixture
def sandbox_manager(valid_config_manager):
    return valid_config_manager["instance"]


@pytest.fixture
def sandbox_config_file(valid_config_manager):
    return valid_config_manager["file"]
{%- endif %}


{% if cookiecutter.use_bdd -%}
@pytest.fixture(scope="function")
def event_loop():
    """Create an instance of the default event loop for the test session."""
    loop = asyncio.new_event_loop()

    yield loop

    loop.close()


{% else -%}
@pytest.fixture
def setup_sample_manager(generate_test_config):
    manager = generate_test_config["instance"]
    manager["settings", "test"] = "somevalue"

    manager.save_all()
    manager.reload_all()

    assert manager["settings", "test"] == "somevalue"

    return {"instance": manager, "file": generate_test_config["file"]}


@pytest.fixture
def sample_log():
    return (
        "2025-10-23 18:56:00.000 | 0:00:00.000000 | {} | test.py:{}    | This is a "
        "test message for the parser      {}"
)
{%- endif %}
