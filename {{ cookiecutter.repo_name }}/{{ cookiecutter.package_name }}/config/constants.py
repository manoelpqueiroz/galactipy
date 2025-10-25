"""Retrieve foundational values for enabling standard behaviour for {{ cookiecutter.project_name }}."""

from platformdirs import user_config_path, user_log_path

from {{ cookiecutter.package_name }} import __version__


def get_default_config():
    """Retrieve the default configuration path for {{ cookiecutter.project_name }}."""
    return user_config_path("{{ cookiecutter.repo_name }}")


def get_default_log_path(filename):
    """Retrieve the default path to store {{ cookiecutter.project_name }} logs."""
    return user_log_path("{{ cookiecutter.repo_name }}") / filename


def generate_default_config_schema():
    """Create the default configuration structure for {{ cookiecutter.project_name }}.

    Returns a new dict instance to avoid mutation issues.

    """
    return {
        "VERSION": __version__,
{%- if cookiecutter.app_type in ['tui', 'hybrid'] %}
        "THEME": "noctis",
{%- endif %}
        # UPDATEME with future default sections to be included
    }
