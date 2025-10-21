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

class BasicConverter:
    def __init__(self, value: str):
        self.input = value
        self.output = self.coalesce(self.input)

    def coalesce(self, value: str):
        if not isinstance(value, str):
            return value

        if len(value) == 0:
            return None

        if value.casefold() in ["true", "false"]:
            return literal_eval(value.capitalize())

        first_char = value[0]

        if first_char.isdigit() or first_char in "+-":
            result = self._parse_numeric_value(value)

        elif first_char in "[{(":
            result = self._parse_container_value(value)

        elif first_char in "'\"":
            result = self._parse_quoted_string(value)

        else:
            return value

        return result

    def _parse_numeric_value(self, value: str):
        # Try integer first
        if "." not in value and "e" not in value.lower():
            try:
                return int(value)

            except ValueError:
                pass

        # Try float
        try:
            return float(value)

        except ValueError:
            pass

        return None

    def _parse_container_value(self, value: str):
        try:
            result = literal_eval(value)

            if isinstance(result, (list, tuple, dict, set, frozenset)):
                return result

        except (ValueError, SyntaxError):
            pass

        return None

    def _parse_quoted_string(self, value: str):
        try:
            result = literal_eval(value)

            if isinstance(result, str):
                return result

        except (ValueError, SyntaxError):
            pass

        return None

    def __str__(self):
        return str(self.output)

    def __repr__(self):
        return repr(self.output)


def parse_converter(value: str):
    return BasicConverter(value)
