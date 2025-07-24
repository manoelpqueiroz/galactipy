"""Specify Textual themes to be loadable and rendered in the TUI application.

Themes defined in this module can be added to the `AppCustomThemes` class and registered
to the TUI app, see https://textual.textualize.io/guide/design/ for more information.

"""

from enum import Enum
from textual.theme import Theme

# Noctis VS Code theme colours, full colorscheme definition at:
# https://github.com/liviuschera/noctis
NOCTIS_AUX_COLOURS_DARK = {
    "secondary": "#e4b781",
    "warning": "#d5971a",
    "error": "#e66533",
    "success": "#16b673",
    "accent": "#7060eb",
}

NOCTIS_AUX_COLOURS_LIGHT = {
    "secondary": "#d67e5c",
    "warning": "#e4b781",
    "error": "#e66533",
    "success": "#16b673",
    "accent": "#16a3b6",
}

NOCTIS_THEME = Theme(
    name="noctis",
    primary="#169fb1",
    foreground="#a5b5b5",
    background="#052529",
    surface="#083d44",
    panel="#041d20",
    boost="#083d44ee",
    dark=True,
    variables={
        "border": "#062e32",
    },
    **NOCTIS_AUX_COLOURS_DARK,
)

NOCTIS_AZUREUS_THEME = Theme(
    name="noctis-azureus",
    primary="#1679b6",
    foreground="#9fb6c6",
    background="#07273b",
    surface="#09334e",
    panel="#062132",
    boost="#003c61ee",
    dark=True,
    variables={
        "border": "#0a3652",
    },
    **NOCTIS_AUX_COLOURS_DARK,
)

NOCTIS_MINIMUS_THEME = Theme(
    name="noctis-minimus",
    primary="#496d83",
    foreground="#96a8b6",
    background="#1b2932",
    surface="#202e37",
    panel="#17232b",
    boost="#1d3544ee",
    dark=True,
    variables={
        "border": "#243742",
    },
    **NOCTIS_AUX_COLOURS_DARK,
)

NOCTIS_BORDO_THEME = Theme(
    name="noctis-bordo",
    primary="#997582",
    foreground="#bbaab0",
    background="#322a2d",
    surface="#413036",
    panel="#2c2528",
    boost="#453138aa",
    dark=True,
    variables={
        "border": "#8f566a33",
    },
    **NOCTIS_AUX_COLOURS_DARK,
)

NOCTIS_UVA_THEME = Theme(
    name="noctis-uva",
    primary="#6e67a8",
    foreground="#a9a5c0",
    background="#292640",
    surface="#2f2c49",
    panel="#232136",
    boost="#35305aee",
    dark=True,
    variables={
        "border": "#363253",
    },
    **NOCTIS_AUX_COLOURS_DARK,
)

NOCTIS_VIOLA_THEME = Theme(
    name="noctis-viola",
    primary="#8767a8",
    foreground="#b3a5c0",
    background="#30243d",
    surface="#3d2e4d",
    panel="#2b2136",
    boost="#402d53ee",
    dark=True,
    variables={
        "border": "#422b5a",
    },
    **NOCTIS_AUX_COLOURS_DARK,
)

NOCTIS_LUX_THEME = Theme(
    name="noctis-lux",
    primary="#0099ad",
    foreground="#888477",
    background="#fef8ec",
    surface="#f6edda",
    panel="#f0e9d6",
    boost="#d1ebefcc",
    dark=False,
    variables={
        "border": "#d1e8eb",
    },
    **NOCTIS_AUX_COLOURS_LIGHT,
)

NOCTIS_LILAC_THEME = Theme(
    name="noctis-lilac",
    primary="#7060eb",
    foreground="#75718e",
    background="#f2f1f8",
    surface="#e9e7f3",
    panel="#e2dff6",
    boost="#d5d2ef99",
    dark=False,
    variables={
        "border": "#c9c2f9",
    },
    **NOCTIS_AUX_COLOURS_LIGHT,
)

NOCTIS_HIBERNUS_THEME = Theme(
    name="noctis-hibernus",
    primary="#0099ad",
    foreground="#71838e",
    background="#f4f6f6",
    surface="#e1eeef",
    panel="#caedf2",
    boost="#d1ebefcc",
    dark=True,
    variables={
        "border": "#d1e8eb",
    },
    **NOCTIS_AUX_COLOURS_LIGHT,
)

class AppCustomThemes(Enum):
    NOCTIS = NOCTIS_THEME

    AZUREUS = NOCTIS_AZUREUS_THEME
    MINIMUS = NOCTIS_MINIMUS_THEME
    BORDO = NOCTIS_BORDO_THEME
    UVA = NOCTIS_UVA_THEME
    VIOLA = NOCTIS_VIOLA_THEME

    LUX = NOCTIS_LUX_THEME
    LILAC = NOCTIS_LILAC_THEME
    HIBERNUS = NOCTIS_HIBERNUS_THEME
