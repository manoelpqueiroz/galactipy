{%- if cookiecutter.use_bdd %}
import asyncio

{%- endif %}
from rich.text import Text

import pytest


@pytest.fixture
def version_string():
    return Text.from_markup(":package:{{ cookiecutter.project_name}} 0.0.0\n").plain


{% if cookiecutter.use_bdd -%}
@pytest.fixture(scope="function")
def event_loop():
    """Create an instance of the default event loop for the test session."""
    loop = asyncio.new_event_loop()
    yield loop
    loop.close()
{%- endif %}
