"""Mapping objects for the {{ cookiecutter.project_name }} configuration manager."""

from enum import Enum


class EnvvarPrefix(Enum):
    """Environment variable prefixes for {{ cookiecutter.project_name }} configuration."""

    SETTINGS = "{{ cookiecutter.__envvar }}"
    SECRETS = "{{ cookiecutter.__envvar }}_SECRET"


class ConfigurationDomain(Enum):
    """Configuration domain identifiers."""

    SETTINGS = "settings"
    SECRETS = "secrets"

    @classmethod
    def from_flag(cls, *, is_secret: bool) -> "ConfigurationDomain":
{%- if cookiecutter.docstring_style != 'other' %}
        """Return the appropriate domain based on the secret flag.
{%- if cookiecutter.docstring_style == 'numpy' %}

        Parameters
        ----------
        is_secret : bool
            Whether the configuration is secret/sensitive.

        Returns
        -------
        ConfigurationDomain
            The corresponding configuration domain.
{%- elif cookiecutter.docstring_style == 'google' %}

        Args:
            is_secret: Whether the configuration is secret/sensitive.

        Returns:
            The corresponding configuration domain.
{%- else %}

        :param is_secret: Whether the configuration is secret/sensitive.
        :type path: bool
        :return: The corresponding configuration domain.
        :rtype: ConfigurationDomain
{%- endif %}
        """
{%- else %}
        """Return the appropriate domain based on the secret flag."""
{%- endif %}
        return cls.SECRETS if is_secret else cls.SETTINGS
