"""Configuration manager for {{ cookiecutter.project_name }}."""

from enum import Enum
from pathlib import Path

from dynamanager import Dynamanager

from {{ cookiecutter.package_name }}.config.constants import (
    generate_default_config_schema,
    get_default_config,
)


class EnvKeys(Enum):
    SETTINGS = "{{ cookiecutter.__envvar }}"
    SECRETS = "{{ cookiecutter.__envvar }}_SECRET"


class AppManager(Dynamanager):
    """Manage configuration files and settings for {{ cookiecutter.project_name }}."""

    def __init__(self):
        """Initialize the manager.

        Creates an instance of a `Dynamanager` object with preset default contents and
        base directory, both defined in the `constants` module.
        """
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
        """Provide a `AppManager` instance with a single domain and custom definitions.

        Parameters
        ----------
        path : Path
            Path to a valid custom TOML configuration file for {{ cookiecutter.project_name }}.
        is_secret : bool
            Flag to treat the given `path` as a settings or secrets file.
        """
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
