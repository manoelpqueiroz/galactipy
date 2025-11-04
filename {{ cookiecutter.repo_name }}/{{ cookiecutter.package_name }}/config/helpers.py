"""Helper functions for streamlining {{ cookiecutter.project_name }} functionality."""

from orbittings import Nucleus

from {{ cookiecutter.package_name }}.config.manager import AppManager


def resolve_app_manager(is_secret=False, custom_path=None) -> Nucleus:
{%- if cookiecutter.docstring_style != 'other' %}
    """Resolve the Orbittings Manager to be used for other operations.
{%- if cookiecutter.docstring_style == 'numpy' %}

    Parameters
    ----------
    is_secret : bool, default False
        Name of the file to be created inside the User Log Path.
    custom_path : Path, optional
        A custom path to load a configuration from.

    Returns
    -------
    str
        The configuration type, either "settings" or "secrets".
    Nucleus
        A manager object for accessing global settings or secrets.
{%- elif cookiecutter.docstring_style == 'google' %}

    Args:
        is_secret: Name of the file to be created inside the User Log Path.
        custom_path: A custom path to load a configuration from.

    Returns:
        A tuple containing the configuration type, either "settings" or "secrets", along
        with a manager object for accessing global settings or secrets.
{%- else %}

    :param is_secret: Name of the file to be created inside the User Log Path.
    :type is_secret: bool
    :param custom_path: A custom path to load a configuration from.
    :type custom_path: Path/None
    :return: A tuple containing the configuration type, either "settings" or "secrets",
        along with a manager object for accessing global settings or secrets.
    :rtype: Nucleus
{%- endif %}
    """
{%- else %}
    """Resolve the Orbittings Manager to be used for other operations."""
{%- endif %}
    config_type = "secrets" if is_secret else "settings"

    if custom_path is None:
        return config_type, AppManager.default()

    return config_type, AppManager.custom(custom_path, is_secret)
