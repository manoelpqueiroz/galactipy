"""Convert string inputs for CLI.

Typer doesn't support arguments or options with more than one type, requiring users to
address the limitation with their own solutions. Having been generated with Galactipy,
{{ cookiecutter.repo_name }} chooses to implement a simple API to do basic type conversions.

There are alternatives to this implementation:

1. A GitHub PR (https://github.com/fastapi/typer/pull/723) is currently open to
   integrate common Pydantic types natively into Typer, but has not been yet merged to
   the main branch;
2. `pydantic-typer` (https://github.com/pypae/pydantic-typer) is a plugin that enables
   Pydantic support for Typer.

"""
from ast import literal_eval
from typing import Any, Optional, Union

from nebulog import logger


class BasicConverter:
    """Converts string inputs to appropriate Python types.

    Parameters
    ----------
    value : str
        A string passed to a Typer CLI command for parsing.
    """

    BOOLEAN_VALUES = ("true", "false")
    NUMERIC_PREFIXES = "+-"
    CONTAINER_PREFIXES = "[{("
    CONTAINER_TYPES = (list, tuple, dict)

    def __init__(self, value: str) -> None:
        if not isinstance(value, str):  # pragma: no cover
            msg = (
                f"BasicConverter only accepts strings; got {type(value).__name__} "
                "instead"
            )
            raise ValueError(msg)

        self.input = value
        self.output = self._convert_value(self.input)

    def _convert_value(self, value: str) -> Any:
        if not value:  # Empty string
            return None

        if value.casefold() in self.BOOLEAN_VALUES:
            return literal_eval(value.capitalize())

        return self._parse_by_first_character(value)

    def _parse_by_first_character(self, value: str) -> Any:
        first_char = value[0]

        if first_char.isdigit() or first_char in self.NUMERIC_PREFIXES:
            return self._parse_numeric_value(value)

        if first_char in self.CONTAINER_PREFIXES:
            return self._parse_container_value(value)

        # Return as string if no other type matches
        return value

    def _parse_numeric_value(self, value: str) -> Optional[Union[int, float]]:
        # Try integer first (more specific check)
        if "." not in value and "e" not in value.lower():
            try:
                return int(value)

            except ValueError:
                pass

        # Try float
        try:
            return float(value)

        except ValueError:
            return value

    def _parse_container_value(self, value: str) -> Optional[Union[list, tuple, dict]]:
        try:
            result = literal_eval(value)

            if isinstance(result, set):
                logger.warning(
                    f"Parsed a {type(result).__name__} object, will convert to tuple"
                )
                return tuple(result)

            return result

        except (ValueError, SyntaxError):
            return None

    def __str__(self) -> str:
        return str(self.output)

    def __repr__(self) -> str:
        return repr(self.output)
