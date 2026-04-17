"""Utility functions to read step arguments with pytest-bdd's `parsers.parse`."""

def boolean_parser(string: str) -> bool:
{%- if cookiecutter.docstring_style != 'other' %}
    """Parse "booleanish" values like "yes"/"no" or "on"/"off" into true booleans.
{%- if cookiecutter.docstring_style == 'numpy' %}

    Parameters
    ----------
    string : str
        A string value to be parsed into a boolean.

    Returns
    -------
    bool
        The converted "booleanish" value.

    Raises
    ------
    ValueError
        If the string is not one of "true"/"false", "yes"/"y"/"no"/"n", "1"/"0" or
        "on"/"off".
{%- elif cookiecutter.docstring_style == 'google' %}

    Args:
        string: A string value to be parsed into a boolean.

    Returns:
        The converted "booleanish" value.

    Raises:
        ValueError: If the string is not one of "true"/"false", "yes"/"y"/"no"/"n",
        "1"/"0" or "on"/"off".
{%- else %}

    :param string: A string value to be parsed into a boolean.
    :type string: str
    :raises ValueError: If the string is not one of "true"/"false", "yes"/"y"/"no"/"n",
        "1"/"0" or "on"/"off".
    :return: The converted "booleanish" value.
    :rtype: bool
{%- endif %}
    """
{%- else %}
    """Parse "booleanish" values like "yes"/"no" or "on"/"off" into true booleans."""
{%- endif %}
    if string.lower() in {"true", "yes", "y", "1", "on"}:
        return True

    if string.lower() in {"false", "no", "n", "0", "off"}:
        return False

    msg = f"cannot convert '{string}' into boolean"
    raise ValueError(msg)
