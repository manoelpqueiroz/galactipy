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

from nebulog import logger

PrimitiveTypes = str | int | float | bool | list | tuple | dict
NonBooleanPrimitives = str | int | float | list | tuple | dict


class BasicConverter:
{%- if cookiecutter.docstring_style != 'other' %}
    """Convert string inputs to appropriate Python types.
{%- if cookiecutter.docstring_style == 'numpy' %}

    Parameters
    ----------
    value : str
        A string passed to a Typer CLI command for parsing.
{%- elif cookiecutter.docstring_style == 'google' %}

    Args:
        value: A string passed to a Typer CLI command for parsing.
{%- else %}

    :param value: A string passed to a Typer CLI command for parsing.
    :type value: str
{%- endif %}
    """
{%- else %}
    """Convert string inputs to appropriate Python types."""
{%- endif %}

    BOOLEAN_VALUES = ("true", "false")
    NUMERIC_PREFIXES = "+-"
    CONTAINER_PREFIXES = "[{("
    CONTAINER_TYPES = (list, tuple, dict)

    def __init__(self, value: str) -> None:
        """Initialise the converter, storing input value and converted output value."""
        self.input = value
        self.output = self._convert_value(self.input)

    def _convert_value(self, value: str) -> PrimitiveTypes | None:
        """Parse a string into a boolean, numeric or container type."""
        if not value:  # Empty string
            return None

        if value.casefold() in self.BOOLEAN_VALUES:
            return literal_eval(value.capitalize())

        return self._parse_by_first_character(value)

    def _parse_by_first_character(self, value: str) -> NonBooleanPrimitives | None:
        """Parse a string by its first character, either a numeric or container type."""
        first_char = value[0]

        if first_char.isdigit() or first_char in self.NUMERIC_PREFIXES:
            return self.parse_numeric_value(value)

        if first_char in self.CONTAINER_PREFIXES:
            return self.parse_container_value(value)

        # Return as string if no other type matches
        return value

    @staticmethod
    def parse_numeric_value(value: str) -> str | int | float | None:
        """Parse a string into a numeric value, whether integer, float or scientific."""
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

    @staticmethod
    def parse_container_value(value: str) -> list | tuple | dict | None:
        """Parse a string into a valid container value.

        Will parse strings into lists, tuples and dictionaries as-is, but will convert
        sets into tuples, as sets are not valid for TOML configuration files.
        """  # noqa: DOC201
        try:
            result = literal_eval(value)

        except (ValueError, SyntaxError):
            return None

        else:
            if isinstance(result, set):
                logger.warning(
                    f"Parsed a {type(result).__name__} object, will convert to tuple"
                )
                return tuple(result)

            return result

    def __str__(self) -> str:
        """Return the string representation of the parsed value for printing."""
        return str(self.output)

    def __repr__(self) -> str:
        """Return the string representation of the parsed value."""
        return repr(self.output)
