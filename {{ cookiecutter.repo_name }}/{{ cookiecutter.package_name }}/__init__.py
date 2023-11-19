# type: ignore[attr-defined]
"""{{ cookiecutter.project_description }}"""

from importlib import metadata, PackageNotFoundError


def _get_version() -> str:
    try:
        return metadata.version("{{ cookiecutter.project_name }}")
    except ModuleNotFoundError:  # pragma: no cover
        return "unknown"


__version__ = _get_version()
