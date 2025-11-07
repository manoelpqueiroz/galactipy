"""Configuration manager for {{ cookiecutter.project_name }}."""

from typing import Self

from pathlib import Path

from orbittings import Nucleus

from {{ cookiecutter.package_name }}.config.constants import (
    generate_default_config_schema,
    get_default_config,
)
from {{ cookiecutter.package_name }}.config.mappings import (
    ConfigurationDomain,
    EnvvarPrefix,
)


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
    def default(cls) -> Self:
        """Provide an `AppManager` instance with default settings and secrets files."""
        instance = cls()
        instance.add("settings", envvar_prefix=EnvvarPrefix.SETTINGS.value)
        instance.add("secrets", envvar_prefix=EnvvarPrefix.SECRETS.value)

        return instance

    @classmethod
    def custom(cls, path: Path, domain: str | ConfigurationDomain) -> Self:
{%- if cookiecutter.docstring_style != 'other' %}
        """Provide a manager instance with a single domain and custom definitions.
{%- if cookiecutter.docstring_style == 'numpy' %}

        Parameters
        ----------
        path : Path
            Path to a valid custom TOML configuration file for {{ cookiecutter.project_name }}.
        domain : {"settings", "secrets"}
            Flag to treat the given `path` as a settings or secrets file.

        Returns
        -------
        AppManager
            A manager instance with a single domain and custom definitions.
{%- elif cookiecutter.docstring_style == 'google' %}

        Args:
            path: Path to a valid custom TOML configuration file for {{ cookiecutter.project_name }}.
            domain: Flag to treat the given `path` as a settings or secrets file.

        Returns: A manager instance with a single domain and custom definitions.
{%- else %}

        :param path: Path to a valid custom TOML configuration file for {{ cookiecutter.project_name }}.
        :type path: Path
        :param domain: Flag to treat the given `path` as a settings or secrets file.
        :type domain: Literal["settings", "secrets"]
        :return: A manager instance with a single domain and custom definitions.
        :rtype: AppManager
{%- endif %}
        """
{%- else %}
        """Provide a manager instance with a single domain and custom definitions."""
{%- endif %}
        instance = cls()
        domain = ConfigurationDomain(domain)

        if domain == ConfigurationDomain.SETTINGS:
            instance.add(
                domain.value,
                custom_config=path,
                envvar_prefix=EnvvarPrefix.SETTINGS.value,
            )

        else:
            instance.add(
                domain.value,
                custom_config=path,
                envvar_prefix=EnvvarPrefix.SECRETS.value,
            )

        return instance
