import os
from pathlib import Path
from shutil import which

from invoke import Context, UnexpectedExit, task

PACKAGE_NAME = "galactipy"

# Windows/Unix differentiation
BIN_DIR = "bin" if os.name != "nt" else "Scripts"
PTY = os.name != "nt"

# Virtualenv retrieval
VENV_EV = os.environ.get("VIRTUAL_ENV", None)
WORKON_HOME_EV = os.environ.get("WORKON_HOME", "~/.virtualenvs")

ACTIVE_VENV = Path(VENV_EV) if VENV_EV is not None else Path.cwd() / "tmp"
VENV_HOME = Path(WORKON_HOME_EV).resolve()

VENV_PATH = ACTIVE_VENV if ACTIVE_VENV.exists() else (VENV_HOME / PACKAGE_NAME)
VENV = VENV_PATH.resolve()

VENV_BIN = Path(VENV) / BIN_DIR

# Executable paths
PYTHON_COMMAND = which("python")
PYTHON_PATH = VENV_BIN / "python" if VENV_BIN.exists() else Path(PYTHON_COMMAND)

POETRY_COMMAND = which("poetry")
if POETRY_COMMAND is not None:
    POETRY_PATH = Path(POETRY_COMMAND).resolve()

elif PTY:
    POETRY_PATH = Path("/usr/bin/poetry")

else:
    APPDATA = os.environ.get("APPDATA")
    POETRY_PATH = Path(APPDATA) / "Python" / BIN_DIR / "poetry"

# Reusable command templates
if PTY:
    FILE_REMOVER = 'find . | grep -E "{}" | xargs rm -rf'

else:
    FILE_REMOVER = (
        "Get-ChildItem -Recurse "
        '| Where-Object {{ $_.Name -match "{}" }} '
        "| Remove-Item -Recurse"
    )


class PoetryPluginError(Exception):
    """Raised when a Poetry plugin is unable to be installed."""

    pass


# Poetry tasks
@task
def poetry_download(c: Context) -> None:
    """Install Poetry as a standalone package via cURL.

    As per Poetry documentation, it should be either installed through a Python
    script which creates a temporary venv and installs Poetry in a
    platform-specific path or via pipx.

    More information can be obtained via https://python-poetry.org/docs/#installation
    and the script instructions in https://install.python-poetry.org/.

    """
    c.run(
        "curl -sSL https://install.python-poetry.org | "
        f"{PYTHON_PATH} - --version 1.8.5",
        pty=PTY,
    )


@task
def poetry_remove(c: Context) -> None:
    """Remove Poetry using the standalone installation script."""
    c.run(
        f"curl -sSL https://install.python-poetry.org | {PYTHON_PATH} - --uninstall",
        pty=PTY,
    )


@task
def poetry_plugins(c: Context) -> None:
    """Install Poetry plugins through the `self add` command."""
    try:
        c.run(
            f"{POETRY_PATH} self add poetry-plugin-up poetry-plugin-export "
            "poetry-bumpversion",
            pty=PTY,
        )

    except UnexpectedExit as e:
        msg = (
            "Command errored with return code 1. Most likely Poetry is externally "
            "managed and `poetry-plugin-up` should be installed via your package "
            "manager."
        )
        raise PoetryPluginError(msg) from e


@task
def poetry_check(c: Context) -> None:
    """Check `pyproject.toml` configuration."""
    c.run(f"{POETRY_PATH} check", pty=PTY)


@task
def update_dev_deps(c: Context) -> None:
    """Update dev dependencies to their latest configuration."""
    c.run(f"{POETRY_PATH} up --only=dev --latest", pty=PTY)


# Installation tasks
@task
def install(c: Context, ignore_pty: bool = False) -> None:
    """Install dependencies specified in `pyproject.toml` and run mypy."""
    local_pty = False if ignore_pty else PTY

    c.run(f"{POETRY_PATH} lock -n", pty=local_pty)
    c.run(f"{POETRY_PATH} install -n", pty=local_pty)
    c.run(
        f"{VENV_BIN}/mypy --config-file pyproject.toml --install-types "
        "--non-interactive",
        pty=local_pty,
    )


@task
def pre_commit_install(c: Context) -> None:
    """Install pre-commit hooks."""
    c.run(f"{VENV_BIN}/pre-commit install", pty=PTY)


# Formatting, linting and other checks
@task(aliases=["format"])
def codestyle(c: Context, check: bool = False) -> None:
    """Format the entire project with `ruff format`."""
    flag = "--check" if check else ""

    c.run(f"{VENV_BIN}/ruff format {flag}", pty=PTY)


@task
def check_linter(c: Context, fix: bool = False) -> None:
    """Check linting rules with `ruff check`."""
    flag = "--fix" if fix else ""

    c.run(f"{VENV_BIN}/ruff check {flag}", pty=PTY)


@task
def test(c: Context) -> None:
    """Run tests with `pytest` and `pyproject.toml` configuration."""
    c.run(f"{VENV_BIN}/pytest -c pyproject.toml tests", pty=PTY)


@task
def mypy(c: Context) -> None:
    """Run type checks with `mypy` and `pyproject.toml` configuration."""
    c.run(f"{VENV_BIN}/mypy --config-file pyproject.toml", pty=PTY)


@task(poetry_check)
def check_safety(c: Context) -> None:
    """Perform security checks with Safety CLI and `bandit`."""
    c.run(f"{VENV_BIN}/safety check --full-report --ignore 70612", pty=PTY)
    c.run(f"{VENV_BIN}/bandit -ll --recursive hooks", pty=PTY)


@task
def sweep(c: Context) -> None:
    """Perform all code checks, including tests, linting and security."""
    test(c)
    check_linter(c)
    codestyle(c)
    mypy(c)
    check_safety(c)


# Cleaning commands for Bash, Zsh and PowerShell
@task(aliases=["pycache-clean"])
def pycache_remove(c: Context) -> None:
    """Remove pycache files from project directory."""
    c.run(FILE_REMOVER.format(r"(__pycache__|\.pyc|\.pyo)$"))


@task(aliases=["dsstore-clean"])
def dsstore_remove(c: Context) -> None:
    """Remove DS Store files from project directory."""
    c.run(FILE_REMOVER.format(".DS_Store"))


@task(aliases=["mypycache-clean", "mypy-remove", "mypy-clean"])
def mypycache_remove(c: Context) -> None:
    """Remove mypy cache files from project directory."""
    c.run(FILE_REMOVER.format(".mypy_cache"))


@task(aliases=["ipynbcheckpoints-clean", "ipynb-clean", "ipynb-remove"])
def ipynbcheckpoints_remove(c: Context) -> None:
    """Remove ipynb checkpoints from project directory."""
    c.run(FILE_REMOVER.format(".ipynb_checkpoints"))


@task(aliases=["pytestcache-clean", "pytest-remove", "pytest-clean"])
def pytestcache_remove(c: Context) -> None:
    """Remove Pytest cache files from project directory."""
    c.run(FILE_REMOVER.format(r"(.pytest_cache|.coverage)"))


@task(aliases=["ruffcache-clean", "ruff-remove", "ruff-clean"])
def ruffcache_remove(c: Context) -> None:
    """Remove Ruff cache files from project directory."""
    c.run(FILE_REMOVER.format(".ruff_cache"))


@task
def cleanup(c: Context) -> None:
    """Perform all cleaning-related tasks."""
    pycache_remove(c)
    dsstore_remove(c)
    mypycache_remove(c)
    ipynbcheckpoints_remove(c)
    pytestcache_remove(c)
    ruffcache_remove(c)


@task
def build_remove(c: Context) -> None:
    """Remove the `build` directory."""
    c.run("rm -rf build/")
