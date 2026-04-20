"""Retrieve foundational values for logging configuration for {{ cookiecutter.project_name }}."""

from pathlib import Path

from platformdirs import user_log_path


def get_default_log_path(filename: str | Path) -> Path:
{%- if cookiecutter.docstring_style != 'other' %}
    """Retrieve the default path to store {{ cookiecutter.project_name }} logs.
{%- if cookiecutter.docstring_style == 'numpy' %}

    Parameters
    ----------
    filename : str, Path
        Name of the file to be created inside the User Log Path.

    Returns
    -------
    Path
        A Path object pointing to the User Log Path where a file for {{ cookiecutter.project_name }} logs
        will be stored.
{%- elif cookiecutter.docstring_style == 'google' %}

    Args:
        filename: Name of the file to be created inside the User Log Path.

    Returns:
        A Path object pointing to the User Log Path where a file for {{ cookiecutter.project_name }} logs
        will be stored.
{%- else %}

    :param filename: Name of the file to be created inside the User Log Path.
    :type filename: str/Path
    :return: A Path object pointing to the User Log Path where a file for {{ cookiecutter.project_name }}
        logs will be stored.
    :rtype: Path
{%- endif %}
    """
{%- else %}
    """Retrieve the default path to store {{ cookiecutter.project_name }} logs."""
{%- endif %}
    return user_log_path("{{ cookiecutter.repo_name }}") / filename
