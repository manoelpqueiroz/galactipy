from rich.text import Text

import pytest


@pytest.fixture
def version_string():
    return Text.from_markup(":package:{{ cookiecutter.project_name}} 0.0.0\n").plain
