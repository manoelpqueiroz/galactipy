"""Specify Rich styles to render text output in the terminal.

Themes defined in this module can be added to the `AppCustomStyles` class and used in
conjunction with `rich.console.Console` to override the default terminal theme.

See https://rich.readthedocs.io/en/stable/style.html#style-themes for more information.

"""

from dataclasses import dataclass

from rich.theme import Theme

# Noctis VS Code theme text colours, full colorscheme definition at:
# https://github.com/liviuschera/noctis
NOCTIS_THEME = Theme({
    "string": "#49e9a6",
    "fstring": "#16b673",
    "comment": "#5b858b",
    "function": "#16a6b6",
    "method": "#49d6e9",
    "standout": "#49ace9",
    "number": "#7060eb",
    "keyword": "#df769b",
    "declaration": "#e66533",
    "property": "#d67e5c",
    "constant": "#d5971a",
    "variable": "#e4b781",
    "bold string": "bold #49e9a6",
    "bold fstring": "bold #16b673",
    "bold comment": "bold #5b858b",
    "bold function": "bold #16a6b6",
    "bold method": "bold #49d6e9",
    "bold standout": "bold #49ace9",
    "bold number": "bold #7060eb",
    "bold keyword": "bold #df769b",
    "bold declaration": "bold #e66533",
    "bold property": "bold #d67e5c",
    "bold constant": "bold #d5971a",
    "bold variable": "bold #e4b781",
})

@dataclass(frozen=True)
class AppCustomStyles:
    NOCTIS = NOCTIS_THEME
