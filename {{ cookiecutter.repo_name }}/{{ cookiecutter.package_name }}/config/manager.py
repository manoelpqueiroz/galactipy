"""Configuration manager for {{ cookiecutter.project_name }}."""

from enum import Enum
from pathlib import Path

from orbittings import Nucleus

from {{ cookiecutter.package_name }}.config.constants import (
    generate_default_config_schema,
    get_default_config,
)


class EnvKeys(Enum):
    """Enum listing the environment variables prefixes for {{ cookiecutter.project_name }} settings."""

    SETTINGS = "{{ cookiecutter.__envvar }}"
    SECRETS = "{{ cookiecutter.__envvar }}_SECRET"


class AppManager(Nucleus):
    """Extend the Orbittings `Nucleus` class to manage {{ cookiecutter.project_name }} configuration.

    Creates an instance of a `Nucleus` object with preset default contents and base
    directory, both defined in the `constants` module.
    """

    def __init__(self):
        """Initialise the manager by calling the `Nucleus` superclass."""
        super().__init__(
            default_contents=generate_default_config_schema(),
            base_dir=get_default_config(),
        )

    @classmethod
    def default(cls):
        """Provide a `AppManager` instance with default settings and secrets files."""
        instance = cls()
        instance.add("settings", envvar_prefix=EnvKeys.SETTINGS.value)
        instance.add("secrets", envvar_prefix=EnvKeys.SECRETS.value)

        return instance

    @classmethod
    def custom(cls, path: Path, is_secret: bool):
{%- if cookiecutter.docstring_style != 'other' %}
        """Provide a manager instance with a single domain and custom definitions.
{%- if cookiecutter.docstring_style == 'numpy' %}

        Parameters
        ----------
        path : Path
            Path to a valid custom TOML configuration file for {{ cookiecutter.project_name }}.
        is_secret : bool
            Flag to treat the given `path` as a settings or secrets file.
{%- elif cookiecutter.docstring_style == 'google' %}

        Args:
            path: Path to a valid custom TOML configuration file for {{ cookiecutter.project_name }}.
            is_secret: Flag to treat the given `path` as a settings or secrets file.
{%- else %}

        :param path: Path to a valid custom TOML configuration file for {{ cookiecutter.project_name }}.
        :type path: Path
        :param is_secret: Flag to treat the given `path` as a settings or secrets file.
        :type is_secret: bool
{%- endif %}
        """
{%- else %}
        """Provide a manager instance with a single domain and custom definitions."""
{%- endif %}
        instance = cls()

        if is_secret:
            instance.add(
                "secrets", custom_config=path, envvar_prefix=EnvKeys.SECRETS.value
            )

        else:
            instance.add(
                "settings", custom_config=path, envvar_prefix=EnvKeys.SETTINGS.value
            )

        return instance
