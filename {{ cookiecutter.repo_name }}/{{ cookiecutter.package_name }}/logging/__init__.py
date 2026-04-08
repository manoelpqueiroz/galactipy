"""Define logging capabilities for {{ cookiecutter.project_name }}."""

from {{ cookiecutter.package_name }}.logging.app_logger import setup_app_logging
from {{ cookiecutter.package_name }}.logging.parsers import FILE_PARSER, log_caster

__all__ = ["FILE_PARSER", "log_caster", "setup_app_logging"]
