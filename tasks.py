import os
from pathlib import Path
from shutil import which

INSTALLATION_ERROR_MSG = (
    "{name} installation not found in the system. Install it through your "
    "distribution's package manager if available; otherwise install it via pipx with "
    "`pipx install {package}`. If you have {name} already installed, your virtual "
    "environment most likely is having trouble choosing the executable to run"
)

try:
    from invoke import Context, call, task
    from invoke.exceptions import Exit

except ModuleNotFoundError as e:
    raise ModuleNotFoundError(
        INSTALLATION_ERROR_MSG.format(name="Invoke", package="invoke")
    ) from e

IS_UNIX_OS = os.name != "nt"
BIN_DIR = "bin" if IS_UNIX_OS else "Scripts"

PROJECT_NAME = "galactipy"

# Reusable command templates
if IS_UNIX_OS:
    FILE_REMOVER = 'find . | grep -E "{}" | xargs rm -rf'

else:
    FILE_REMOVER = (
        "Get-ChildItem -Recurse "
        '| Where-Object {{ $_.Name -match "{}" }} '
        "| Remove-Item -Recurse"
    )


def get_poetry_command() -> Path:
    """Retrieve the executable path for Poetry.

    Returns
    -------
    Path
        Path to the Poetry executable. If no path is found, will use the
        system's default paths for a Poetry installation.
    """
    poetry_command = which("poetry")

    if poetry_command is not None:
        poetry_path = Path(poetry_command).resolve()

    else:
        raise Exit(INSTALLATION_ERROR_MSG.format(name="Poetry", package="poetry"))

    return poetry_path


# Foundational tasks, used as the basis for running other tasks
@task
def venv(c: Context, hide: bool = False) -> None:
    """Add Poetry executable and project environment binaries to context."""
    poetry_path = get_poetry_command()

    result = c.run(f"{poetry_path} env info --path", hide=hide, warn=True)

    if result.failed:
        msg = f"unable to fetch Poetry virtual environment for {PROJECT_NAME}"
        raise Exit(msg)

    c.venv_bin_path = Path(result.stdout.strip()).resolve() / BIN_DIR


@task(call(venv, hide=True))
def mypy(
    c: Context, install_types: bool = False, non_interactive: bool = False
) -> None:
    """Run type checks with `mypy` and `pyproject.toml` configuration."""
    install_flag = "--install-types" if install_types else ""
    non_interactive_flag = "--non-interactive" if non_interactive else ""

    c.run(
        f"{c.venv_bin_path}/mypy --config-file pyproject.toml {install_flag} "
        f"{non_interactive_flag}",
        pty=IS_UNIX_OS,
    )


@task(call(venv, hide=True), aliases=["pre-commit-install", "install-hooks"])
def hooks(c: Context) -> None:
    """Install pre-commit hooks."""
    c.run(f"{c.venv_bin_path}/pre-commit install", pty=IS_UNIX_OS)


# Poetry tasks
@task(aliases=["poetry-check"])
def pyproject(c: Context) -> None:
    """Check `pyproject.toml` configuration."""
    poetry_path = get_poetry_command()

    c.run(f"{poetry_path} check", pty=IS_UNIX_OS)


@task(aliases=["update-deps"])
def update(c: Context, latest: bool = False) -> None:
    """Update dependencies to their latest configuration."""
    poetry_path = get_poetry_command()
    flag = "--latest" if latest else ""

    c.run(f"{poetry_path} up {flag}", pty=IS_UNIX_OS)


# Installation tasks
@task(post=[hooks, call(mypy, install_types=True, non_interactive=True)])
def install(c: Context, ignore_pty: bool = False) -> None:
    """Install dependencies specified in `pyproject.toml` and run MyPy."""
    poetry_path = get_poetry_command()
    local_pty = False if ignore_pty else IS_UNIX_OS

    c.run(f"{poetry_path} lock -n", pty=local_pty)
    c.run(f"{poetry_path} install -n", pty=local_pty)


# Formatting, linting and other checks
@task(call(venv, hide=True), aliases=["format"])
def codestyle(c: Context, check: bool = False) -> None:
    """Format the entire project with `ruff format`."""
    flag = "--check" if check else ""

    c.run(f"{c.venv_bin_path}/ruff format {flag}", pty=IS_UNIX_OS)


@task(call(venv, hide=True), aliases=["check-linter"])
def lint(c: Context, fix: bool = False) -> None:
    """Check linting rules with `ruff check`."""
    flag = "--fix" if fix else ""

    c.run(f"{c.venv_bin_path}/ruff check {flag}", pty=IS_UNIX_OS)


@task(call(venv, hide=True))
def test(c: Context) -> None:
    """Run tests with Pytest and `pyproject.toml` configuration."""
    c.run(f"{c.venv_bin_path}/pytest -c pyproject.toml tests", pty=IS_UNIX_OS)


@task(call(venv, hide=True))
def coverage(c: Context) -> None:
    """Generate coverage file in XML for integration with Codacy."""
    c.run(f"{c.venv_bin_path}/coverage xml", pty=IS_UNIX_OS)


@task(call(venv, hide=True), pyproject, aliases=["safety", "check-safety", "sec"])
def security(c: Context) -> None:
    """Perform security checks with Bandit."""
    c.run(
        f"{c.venv_bin_path}/bandit -ll -c pyproject.toml --recursive hooks",
        pty=IS_UNIX_OS,
    )


@task(call(venv, hide=True))
def sweep(c: Context) -> None:
    """Perform all code checks, including tests, linting and security."""
    test(c)
    lint(c)
    codestyle(c, check=True)
    mypy(c)
    security(c)


# Cleaning commands for Bash, Zsh and PowerShell
@task(aliases=["rm-cache", "clean-cache"])
def remove_cache(c: Context) -> None:
    """Remove pycache files from project directory."""
    c.run(FILE_REMOVER.format(r"(__pycache__|\.pyc|\.pyo)$"), pty=IS_UNIX_OS)


@task(aliases=["rm-dsstore", "clean-dsstore"])
def remove_dsstore(c: Context) -> None:
    """Remove DS Store files from project directory."""
    c.run(FILE_REMOVER.format(".DS_Store"), pty=IS_UNIX_OS)


@task(aliases=["rm-mypy", "clean-mypy"])
def remove_mypy(c: Context) -> None:
    """Remove mypy cache files from project directory."""
    c.run(FILE_REMOVER.format(".mypy_cache"), pty=IS_UNIX_OS)


@task(aliases=["rm-ipynb", "clean-ipynb"])
def remove_ipynb(c: Context) -> None:
    """Remove ipynb checkpoints from project directory."""
    c.run(FILE_REMOVER.format(".ipynb_checkpoints"), pty=IS_UNIX_OS)


@task(aliases=["rm-pytest", "clean-pytest"])
def remove_pytest(c: Context) -> None:
    """Remove Pytest cache files from project directory."""
    c.run(
        FILE_REMOVER.format(r"(.pytest_cache|.coverage|test_report.xml)"),
        pty=IS_UNIX_OS,
    )


@task(aliases=["rm-ruff", "clean-ruff"])
def remove_ruff(c: Context) -> None:
    """Remove Ruff cache files from project directory."""
    c.run(FILE_REMOVER.format(".ruff_cache"), pty=IS_UNIX_OS)


@task
def cleanup(c: Context) -> None:
    """Perform all cleaning-related tasks.

    Does not remove the `build` directory. This should be removed using
    `invoke remove-build`.
    """
    remove_cache(c)
    remove_dsstore(c)
    remove_mypy(c)
    remove_ipynb(c)
    remove_pytest(c)
    remove_ruff(c)


@task(aliases=["rm-build", "clean-build"])
def remove_build(c: Context) -> None:
    """Remove the `build` directory."""
    c.run("rm -rf build/", pty=IS_UNIX_OS)
