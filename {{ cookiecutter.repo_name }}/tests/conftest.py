{%- if cookiecutter.use_bdd %}
import asyncio

{%- endif %}
from rich.text import Text

import pytest


@pytest.fixture
def version_string():
    """Define the expected version string to be printed to STDOUT."""
    return Text.from_markup(":package:{{ cookiecutter.project_name}} 0.0.0\n").plain


@pytest.fixture
def valid_config_data():
    return {"VERSION": "0.0.0", "THEME": "noctis"}


{% if cookiecutter.use_bdd -%}
@pytest.fixture(scope="function")
def event_loop():
    """Create an instance of the default event loop for the test session."""
    loop = asyncio.new_event_loop()
    yield loop
    loop.close()
{%- endif %}
