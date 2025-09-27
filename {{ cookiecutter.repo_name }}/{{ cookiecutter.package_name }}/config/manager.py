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
    def __init__(self):
        super().__init__(
            default_contents=generate_default_config_schema(),
            base_dir=get_default_config(),
        )

    @classmethod
    def default(cls):
        instance = cls()
        instance.add("settings", envvar_prefix=EnvKeys.SETTINGS.value)
        instance.add("secrets", envvar_prefix=EnvKeys.SECRETS.value)

        return instance

    @classmethod
    def custom(cls, path: Path, is_secret: bool):
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
