"""Define logging capabilities for {{ cookiecutter.project_name }}."""

from nebulog import install, logger

from {{ cookiecutter.package_name }}.config.constants import get_default_log_path
from {{ cookiecutter.package_name }}.logging.formatters import file_formatter


def setup_app_logging(*, debug: bool = False) -> None:
{%- if cookiecutter.docstring_style != 'other' %}
    """Configure the available loggers at {{ cookiecutter.project_name }} runtime.
{%- if cookiecutter.docstring_style == 'numpy' %}

    Parameters
    ----------
    debug : bool, default False
        Define whether logs will be called at the DEBUG level or a higher level
        depending on the type of logger.
{%- elif cookiecutter.docstring_style == 'google' %}

    Args:
        debug: Define whether logs will be called at the DEBUG level or a higher level
        depending on the type of logger.
{%- else %}

    :param debug: Define whether logs will be called at the DEBUG level or a higher
        level depending on the type of logger.
    :type debug: bool
{%- endif %}
    """
{%- else %}
    """Configure the available loggers at {{ cookiecutter.project_name }} runtime."""
{%- endif %}
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

    # Special log file for bug reporting, containing only the last run produced
    logger.add(
        get_default_log_path("report.log"),
        format=file_formatter,
        level="TRACE",
        mode="w",
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
