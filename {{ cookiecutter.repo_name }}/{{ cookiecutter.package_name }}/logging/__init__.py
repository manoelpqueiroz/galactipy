import sys

from nebulog import install, logger

from {{ cookiecutter.package_name }}.config.constants import get_default_log_path
from {{ cookiecutter.package_name }}.logging.formatters import file_formatter


def setup_app_logging(*, debug: bool = False):
    file_log_level = "DEBUG" if debug else "INFO"
    shell_log_level = "DEBUG" if debug else "WARNING"

    install(level=shell_log_level)

    logger.enable("")

    logger.add(
        get_default_log_path("app.log"),
        format=file_formatter,
        level=file_log_level,
        rotation="10 MB",
        retention="30 days",
        backtrace=False,
    )

    logger.add(
        get_default_log_path("app.jsonl"),
        serialize=True,
        rotation="10 MB",
        retention="30 days",
        backtrace=False,
    )


__all__ = ["file_formatter", "setup_app_logging"]
