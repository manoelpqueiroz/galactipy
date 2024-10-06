import os
from pathlib import Path
from shutil import which
from uuid import uuid4

from invoke import Context, UnexpectedExit, task

PACKAGE_NAME = "galactipy"

# Windows/Unix differentiation
BIN_DIR = "bin" if os.name != "nt" else "Scripts"
PTY = os.name != "nt"

# Virtualenv retrieval
VENV_EV = os.environ.get("VIRTUAL_ENV", None)
WORKON_HOME_EV = os.environ.get("WORKON_HOME", "~/.virtualenvs")

ACTIVE_VENV = Path(VENV_EV) if VENV_EV is not None else Path(str(uuid4()))
VENV_HOME = Path(WORKON_HOME_EV).resolve()

VENV_PATH = ACTIVE_VENV if ACTIVE_VENV.exists() else (VENV_HOME / PACKAGE_NAME)
VENV = VENV_PATH.resolve()

VENV_BIN = Path(VENV) / Path(BIN_DIR)

# Executable paths
PYTHON_PATH = VENV_BIN / "python"

POETRY_COMMAND = which("poetry")
if POETRY_COMMAND is not None:
    POETRY_PATH = Path(POETRY_COMMAND).resolve()
else:
    POETRY_PATH = Path(str(uuid4()))


class PoetryPluginError(Exception):
    """Raised when a Poetry plugin is unable to be installed.

    """

    pass


@task
def poetry_download(c: Context) -> None:
    """Install Poetry as a standalone package via cURL.

    As per Poetry documentation, it should be either installed through a Python
    script which creates a temporary venv and installs Poetry in a
    platform-specific path or via pipx.

    More information can be obtained via https://python-poetry.org/docs/#installation
    and the script instructions in https://install.python-poetry.org/.

    """
    c.run(f"curl -sSL https://install.python-poetry.org | {PYTHON_PATH} -", pty=PTY)


@task
def poetry_remove(c: Context) -> None:
    """Remove Poetry using the standalone installation script.

    """
    c.run(
        f"curl -sSL https://install.python-poetry.org | {PYTHON_PATH} - --uninstall",
        pty=PTY,
    )


@task
def poetry_plugins(c: Context) -> None:
    """Install Poetry plugins through the `self add` command.

    """
    if POETRY_PATH.exists():
        try:
            c.run(f"{POETRY_PATH} self add poetry-plugin-up", pty=PTY)

        except UnexpectedExit as e:
            msg = (
                "Command errored with return code 1. Most likely Poetry is externally "
                "managed and `poetry-plugin-up` should be installed via your package "
                "manager."
            )
            raise PoetryPluginError(msg) from e

    else:
        msg = "Poetry installation not found."
        raise PoetryPluginError(msg)


@task
def install(c: Context) -> None:
    """Install dependencies specified in `pyproject.toml` and run mypy.

    """
    c.run(f"{POETRY_PATH} lock -n", pty=PTY)
    c.run(f"{POETRY_PATH} install -n", pty=PTY)
    c.run(
        f"{VENV_BIN}/mypy --config-file pyproject.toml --install-types "
        "--non-interactive hooks tests",
        pty=PTY,
    )


@task
def pre_commit_install(c: Context) -> None:
    """Install pre-commit hooks.

    """
    c.run(f"{VENV_BIN}/pre-commit install", pty=PTY)
