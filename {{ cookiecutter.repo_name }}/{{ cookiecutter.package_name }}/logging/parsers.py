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


def log_caster(groups: dict) -> dict:  # pragma: no cover
    groups["ts"] = datetime.strptime(groups["ts"], "%Y-%m-%d %H:%M:%S.%f")
    groups["line"] = int(groups["line"])
