"""Helper functions for streamlining {{ cookiecutter.project_name }} functionality."""

from orbittings import Nucleus

from {{ cookiecutter.package_name }}.config.manager import AppManager


def resolve_app_manager(is_secret=False, custom_path=None) -> Nucleus:
    config_type = "secrets" if is_secret else "settings"

    if custom_path is None:
        return config_type, AppManager.default()

    return config_type, AppManager.custom(custom_path, is_secret)
