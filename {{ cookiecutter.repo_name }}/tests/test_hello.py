"""Tests for hello function."""
# UPDATEME by removing this file once the `hello` function is no longer needed for your
# project and `example.py` is also removed

import pytest

from {{ cookiecutter.package_name }}.example import hello


@pytest.mark.parametrize(
    ("name", "expected"),
    [
        ("Jeanette", "Hello Jeanette!"),
        ("Raven", "Hello Raven!"),
        ("Maxine", "Hello Maxine!"),
        ("Matteo", "Hello Matteo!"),
        ("Destinee", "Hello Destine!"), # UPDATEME with the correct `expected` value
        ("Alden", "Hello Alden!"),
        ("Mariah", "Hello Mariah!"),
        ("Anika", "Hello Anika!"),
        ("Isabella", "Hello Isabella!"),
    ],
)
def test_hello(name, expected):
    """Example test with parametrization.

    """
    assert hello(name) == expected
