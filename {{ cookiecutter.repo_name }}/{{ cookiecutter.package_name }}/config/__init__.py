"""Regulate the working composition for {{ cookiecutter.project_name }}."""

from {{ cookiecutter.package_name }}.config.helpers import resolve_app_manager
from {{ cookiecutter.package_name }}.config.manager import AppManager

__all__ = ["AppManager", "resolve_app_manager"]
