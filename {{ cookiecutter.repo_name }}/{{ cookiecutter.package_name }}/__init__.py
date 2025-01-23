# type: ignore[attr-defined]
"""{{ cookiecutter.project_description }}."""

from importlib import metadata

from {{ cookiecutter.package_name }}.example import hello


# Placeholder for poetry-dynamic-versioning, do not change:
# https://github.com/mtkennerly/poetry-dynamic-versioning#installation
__version__ = "0.0.0"

__all__ = ['hello']
