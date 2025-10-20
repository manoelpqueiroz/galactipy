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


def _format_location_string(record: dict, justify_left: bool) -> str:
    """Extract and format location information as `file:line`."""
    file_name = record["file"].name
    line_number = record["line"]
    padding = LOGGER_FORMATTER.get_location_padding()

    if justify_left:
        return f"{file_name}:{line_number}".ljust(padding)

    return f"{file_name}:{line_number}".rjust(padding)


def file_formatter(record: dict) -> str:
    """Define the default formatting for Loguru calls to be stored in the log files.

    Parameters
    ----------
    record : dict
        The Loguru record dictionary with the information about the logging context.
    """
    record.update({"location_string": _format_location_string(record, True)})

    if record["extra"]:
        return FILE_FORMATTER_WITH_EXTRA

    return FILE_FORMATTER_WITHOUT_EXTRA
