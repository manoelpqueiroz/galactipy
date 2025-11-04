"""Custom logger formatting utilities for {{ cookiecutter.project_name }}."""

from {{ cookiecutter.package_name }}.logging.text_tools import LoggerFormatter

LOGGER_FORMATTER = LoggerFormatter()

_FILE_BASE_TEMPLATE = (
    "{time:%Y-%m-%d %H:%M:%S}.{time:SSS} | "
    "{elapsed} | "
    "{level:<8} | "  # Based on the default levels in Loguru (max. 8 in "CRITICAL")
    "{location_string} | "
    "{message:<60} ¶"
)

FILE_FORMATTER_WITH_EXTRA = _FILE_BASE_TEMPLATE + " {extra}\n{exception}"
FILE_FORMATTER_WITHOUT_EXTRA = _FILE_BASE_TEMPLATE + "\n{exception}"


def _format_location_string(record: dict) -> str:
    """Extract and format location information as `file:line`."""
    file_name = record["file"].name
    line_number = record["line"]
    padding = LOGGER_FORMATTER.get_location_padding()

    return f"{file_name}:{line_number}".ljust(padding)


def file_formatter(record: dict) -> str:
{%- if cookiecutter.docstring_style != 'other' %}
    """Define the default formatting for Loguru calls to be stored in the log files.
{%- if cookiecutter.docstring_style == 'numpy' %}

    Parameters
    ----------
    record : dict
        The Loguru record dictionary with the information about the logging context.

    Returns
    -------
    str
        A formatted string with standardised padding for the individual parts of the log
        entry.
{%- elif cookiecutter.docstring_style == 'google' %}

    Args:
        record: The Loguru record dictionary with the information about the logging
            context.

    Returns: A formatted string with standardised padding for the individual parts of
        the log entry.
{%- else %}

    :param record: The Loguru record dictionary with the information about the logging
        context.
    :type record: dict
    :return: A formatted string with standardised padding for the individual parts of
        the log entry.
    :rtype: str
{%- endif %}
    """
{%- else %}
    """Define the default formatting for Loguru calls to be stored in the log files."""
{%- endif %}
    record.update({"location_string": _format_location_string(record)})

    if record["extra"]:
        return FILE_FORMATTER_WITH_EXTRA

    return FILE_FORMATTER_WITHOUT_EXTRA
