"""Helper functions for streamlining {{ cookiecutter.project_name }} functionality."""

from typing import Literal, TYPE_CHECKING

from pathlib import Path

from {{ cookiecutter.package_name }}.config.manager import AppManager

if TYPE_CHECKING:
    from orbittings import Nucleus


def resolve_app_manager(
    domain: Literal["settings", "secrets"], custom_path: Path | None = None
) -> "Nucleus":
{%- if cookiecutter.docstring_style != 'other' %}
    """Resolve the Orbittings Manager to be used for other operations.
{%- if cookiecutter.docstring_style == 'numpy' %}

    Parameters
    ----------
    domain : {"settings", "secrets"}
        Flag to treat the given `path` as a settings or secrets file.
    custom_path : Path, optional
        A custom path to load a configuration from.

    Returns
    -------
    Nucleus
        A manager object for accessing global settings or secrets.
{%- elif cookiecutter.docstring_style == 'google' %}

    Args:
        domain: Flag to treat the given `path` as a settings or secrets file.
        custom_path: A custom path to load a configuration from.

    Returns:
        A manager object for accessing global settings or secrets.
{%- else %}

    :param domain: Flag to treat the given `path` as a settings or secrets file.
    :type domain: Literal["settings", "secrets"]
    :param custom_path: A custom path to load a configuration from.
    :type custom_path: Path/None
    :return: A manager object for accessing global settings or secrets.
    :rtype: Nucleus
{%- endif %}
    """
{%- else %}
    """Resolve the Orbittings Manager to be used for other operations."""
{%- endif %}
    if custom_path is None:
        return AppManager.default()

    return AppManager.custom(custom_path, domain)
