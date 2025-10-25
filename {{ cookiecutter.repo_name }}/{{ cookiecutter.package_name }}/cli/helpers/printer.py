from rich.pretty import pprint

from dynaconf.utils.boxing import DynaBox
from dynaconf.vendor.box.box_list import BoxList


def pretty_print_setting(manager, key, config_type):
    if key is None:
        _print_entire_config(manager, config_type)
    else:
        _print_specific_setting(manager, key, config_type)


def _print_entire_config(manager, config_type):
    config_dict = manager[config_type].to_dict()

    pprint(config_dict)


def _print_specific_setting(manager, key, config_type):
    value = manager[config_type, key]
    formatted_value = _format_value_for_printing(value)

    pprint(formatted_value)


def _format_value_for_printing(value):
    if isinstance(value, DynaBox):
        return value.to_dict()

    if isinstance(value, BoxList):
        return value.to_list()

    return value
