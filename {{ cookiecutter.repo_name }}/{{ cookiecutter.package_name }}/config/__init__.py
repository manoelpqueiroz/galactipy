"""Regulate the working composition for {{ cookiecutter.project_name }}."""

from {{ cookiecutter.package_name }}.config.helpers import resolve_app_manager
from {{ cookiecutter.package_name }}.config.manager import AppManager
from {{ cookiecutter.package_name }}.config.mappings import ConfigurationDomain

__all__ = ["AppManager", "ConfigurationDomain", "resolve_app_manager"]
