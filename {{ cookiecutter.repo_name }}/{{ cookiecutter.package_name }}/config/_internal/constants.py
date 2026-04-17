"""Retrieve foundational values for enabling standard behaviour for {{ cookiecutter.project_name }}."""

from pathlib import Path

from platformdirs import user_config_path

from {{ cookiecutter.package_name }}._version import __version__


def get_default_config() -> Path:
{%- if cookiecutter.docstring_style != 'other' %}
    """Retrieve the default configuration path for {{ cookiecutter.project_name }}.
{%- if cookiecutter.docstring_style == 'numpy' %}

    Returns
    -------
    Path
        A Path object pointing to the User Config Path where configuration for
        {{ cookiecutter.project_name }} will be stored.
{%- elif cookiecutter.docstring_style == 'google' %}

    Returns:
        A Path object pointing to the User Config Path where configuration for
        {{ cookiecutter.project_name }} will be stored.
{%- else %}

    :return: A Path object pointing to the User Config Path where configuration for
        {{ cookiecutter.project_name }} will be stored.
    :rtype: Path
{%- endif %}
    """
{%- else %}
    """Retrieve the default configuration path for {{ cookiecutter.project_name }}."""
{%- endif %}
    return user_config_path("{{ cookiecutter.repo_name }}")


def generate_default_config_schema():
{%- if cookiecutter.docstring_style != 'other' %}
    """Create the default configuration schema for {{ cookiecutter.project_name }}.
{%- if cookiecutter.docstring_style == 'numpy' %}

    Returns
    -------
    dict
        A dictionary containing the keys and values for the vanilla {{ cookiecutter.project_name }}
        configuration, wrapped inside a function to avoid mutation issues.
{%- elif cookiecutter.docstring_style == 'google' %}

    Returns:
        A dictionary containing the keys and values for the vanilla {{ cookiecutter.project_name }}
        configuration, wrapped inside a function to avoid mutation issues.
{%- else %}

    :return: A dictionary containing the keys and values for the vanilla {{ cookiecutter.project_name }}
        configuration, wrapped inside a function to avoid mutation issues.
    :rtype: dict
{%- endif %}
    """
{%- else %}
    """Create the default configuration schema for {{ cookiecutter.project_name }}."""
{%- endif %}
{%- if cookiecutter.__app_group == 'tui' %}
    return {
        "VERSION": __version__,
        "THEME": "noctis",
        # UPDATEME with future default sections to be included
    }
{%- else %}
    # UPDATEME with future default sections to be included
    return {"VERSION": __version__}
{%- endif %}
