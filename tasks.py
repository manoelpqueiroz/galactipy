import os
from pathlib import Path

PACKAGE_NAME = "galactipy"

# Windows/Unix differentiation
BIN_DIR = "bin" if os.name != "nt" else "Scripts"
PTY = os.name != "nt"

# Virtualenv retrieval
ACTIVE_VENV = Path(os.environ.get("VIRTUAL_ENV", None))
VENV_HOME = Path(os.environ.get("WORKON_HOME", "~/virtualenvs"))
VENV_PATH = ACTIVE_VENV if ACTIVE_VENV.exists() else (VENV_HOME / PACKAGE_NAME)
VENV = VENV_PATH.expanduser()

VENV_BIN = Path(VENV) / Path(BIN_DIR)
