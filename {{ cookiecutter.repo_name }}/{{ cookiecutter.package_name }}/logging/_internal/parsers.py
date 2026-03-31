"""Parse custom loggers defined for {{ cookiecutter.project_name }}."""

import re
from datetime import datetime

FILE_PARSER = re.compile(
    r"""
        (?P<ts>\d{4}-\d{2}-\d{2}\s\d{2}:\d{2}:\d{2}.\d{3})
        \s\|\s
        \d:\d{2}:\d{2}.\d{6}
        \s\|\s
        (?P<level>\w+)
        \s+\|\s
        (?P<module>\w+)\.py:(?P<line>\d+)
        \s+\|\s
        (?P<message>\S.*?)
        \s*¶  # Extra is deliberately omitted, use JSON serialised logger instead
    """,
    re.VERBOSE,
)


def log_caster(groups: dict) -> None:  # pragma: no cover
{%- if cookiecutter.docstring_style != 'other' %}
    """Convert the parts of a parsed log record line into convenient Python types.
{%- if cookiecutter.docstring_style == 'numpy' %}

    Parameters
    ----------
    groups : dict
        The Loguru record dictionary with the information about the logging context.
{%- elif cookiecutter.docstring_style == 'google' %}

    Args:
        groups: The Loguru record dictionary with the information about the logging
            context.
{%- else %}

    :param groups: The Loguru record dictionary with the information about the logging
        context.
    :type groups: dict
{%- endif %}
    """
{%- else %}
    """Convert the parts of a parsed log record line into convenient Python types."""
{%- endif %}
    groups["ts"] = datetime.strptime(groups["ts"], "%Y-%m-%d %H:%M:%S.%f")
    groups["line"] = int(groups["line"])
