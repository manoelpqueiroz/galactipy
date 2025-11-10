"""Helper functions designed to print unconventional types in Rich consoles."""

from rich.pretty import pprint

from dynaconf.utils.boxing import DynaBox
from dynaconf.vendor.box.box_list import BoxList


def pretty_print_setting(manager, key, config_type):
{%- if cookiecutter.docstring_style != 'other' %}
    """Print a Orbittings setting as a literal value on a Rich console.
{%- if cookiecutter.docstring_style == 'numpy' %}

    Parameters
    ----------
    manager : Nucleus
        A Orbittings manager instance.
    key : str, None
        The key to retrieve from `config_type`.
    config_type : str
        The OrbitalSystem object to inspect for `key`.
{%- elif cookiecutter.docstring_style == 'google' %}

    Args:
        manager: A Orbittings manager instance.
        key: The key to retrieve from `config_type`.
        config_type: The OrbitalSystem object to inspect for `key`.
{%- else %}

    :param manager: A Orbittings manager instance.
    :type manager: Nucleus
    :param key: The key to retrieve from `config_type`.
    :type key: str/None
    :param config_type: The OrbitalSystem object to inspect for `key`.
    :type config_type: str
{%- endif %}
    """
{%- else %}
    """Print a Orbittings setting as a literal value on a Rich console."""
{%- endif %}
    if key is None:
        _print_entire_config(manager, config_type)
    else:
        _print_specific_setting(manager, key, config_type)


def _print_entire_config(manager, config_type):
    """Print the entire Orbittings configuration as a dictionary on a Rich console."""
    config_dict = manager[config_type].to_dict()

    pprint(config_dict)


def _print_specific_setting(manager, key, config_type):
    """Print a Orbittings setting with their adequate type on a Rich console."""
    value = manager[config_type, key]
    formatted_value = _format_value_for_printing(value)

    pprint(formatted_value)


def _format_value_for_printing(value):
    """Format box and list Dynaconf objects to their respective literals."""
    if isinstance(value, DynaBox):
        return value.to_dict()

    if isinstance(value, BoxList):
        return value.to_list()

    return value
