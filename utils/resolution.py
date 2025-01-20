"""Utilities for virtual environment resolution."""

import os
from pathlib import Path
from shutil import which

try:
    from invoke import run
except ModuleNotFoundError as e:
    msg = (
        "Invoke was not found in your system. Install it through your distribution's "
        "package manager if available, otherwise install it preferrably via pipx with "
        "`pipx install invoke` or through `pip install invoke --user`. If you have "
        "Invoke already installed, your virtual environment most likely is having "
        "trouble choosing the executable to run."
    )
    raise ModuleNotFoundError(msg) from e

UNIX_OS = os.name != "nt"
BIN_DIR = "bin" if UNIX_OS else "Scripts"


def get_venv_bin(package_name: str) -> Path:
    """Retrieve a Python virtual environment binary path from the system.

    Sequentially resolves possible venv paths through the following order:

    1. Gets the active venv from the VIRTUAL_ENV environment variable if one is
    active;
    2. Gets a candidate venv path from the virtualenvwrapper WORKON_HOME
    environment variable (or the `~/.virtualenvs` default), along with a
    package name to look for venvs inside the directory;
    3. Attempts to retrieve the venv path from the Poetry environment.

    Parameters
    ----------
    package_name : str
        Name for the package to look for a virtual environment inside
        virtualenvwrapper's default venv folder.

    Returns
    -------
    Path or None
        Returns the path of the "bin" directory of the virtual environment, or
        None if no virtual environment is found.
    """
    active_venv = os.environ.get("VIRTUAL_ENV", None)

    workon_home = os.environ.get("WORKON_HOME", "~/.virtualenvs")
    venvwrapper_venv = Path(workon_home).resolve() / package_name

    poetry_env_check = run("poetry env info --path", warn=True, hide=True)

    if active_venv is not None:
        venv_path = Path(active_venv).resolve()

    elif venvwrapper_venv.exists():
        venv_path = venvwrapper_venv

    elif poetry_env_check.return_code == 0:
        venv_path = Path(poetry_env_check.stdout.rstrip()).resolve()

    else:
        venv_path = None

    return Path(venv_path) / BIN_DIR if venv_path is not None else None


def get_commands(venv_bin: Path | None) -> list[Path]:
    """Retrieve the executable paths for Python and Poetry.

    Parameters
    ----------
    venv_bin : Path
        Path to the binary directory of the current virtual environment.

    Returns
    -------
    python_path : Path
        Path to the Python executable. If no virtual environment is found, will
        use the system's default Python path.
    poetry_path : Path
        Path to the Poetry executable. If no path is found, will use the
        system's default paths for a Poetry installation.
    """
    python_command = which("python")
    poetry_command = which("poetry")

    appdata = os.environ.get("APPDATA")
    localappdata = os.environ.get("LOCALAPPDATA")

    if python_command is None and UNIX_OS:
        python_path = Path("/usr/bin/python")

    elif python_command is None and not UNIX_OS:
        python_path = Path(localappdata) / "Programs" / "Python" / "Launcher" / "py"

    elif venv_bin is None:
        python_path = Path(python_command)

    else:
        python_path = venv_bin / "python" if venv_bin.exists() else Path(python_command)

    if poetry_command is not None:
        poetry_path = Path(poetry_command).resolve()

    elif UNIX_OS:
        poetry_path = Path("/usr/bin/poetry")

    else:
        poetry_path = Path(appdata) / "Python" / BIN_DIR / "poetry"

    return python_path, poetry_path
