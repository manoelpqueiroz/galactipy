"""Define logging capabilities for {{ cookiecutter.project_name }}."""

from {{ cookiecutter.package_name }}.logging.app_logger import setup_app_logging

__all__ = ["setup_app_logging"]
