"""Mapping objects for the {{ cookiecutter.project_name }} configuration manager."""

from typing import Self

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
    def from_flag(cls, *, is_secret: bool) -> Self:
        """Return the appropriate domain based on the secret flag.

        Parameters
        ----------
        is_secret : bool
            Whether the configuration is secret/sensitive.

        Returns
        -------
        ConfigurationDomain
            The corresponding configuration domain.
        """
        return cls.SECRETS if is_secret else cls.SETTINGS
