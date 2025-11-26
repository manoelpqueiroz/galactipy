import os
from collections.abc import Callable
from dataclasses import dataclass
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
    FILE_REMOVER = 'find . -not -path "./.git/*" | grep -E "{}" | xargs rm -rf'
    FILE_OPENER = "xdg-open {}"

else:
    FILE_REMOVER = (
        "Get-ChildItem -Recurse -Exclude .git "
        '| Where-Object {{ $_.FullName -notlike "*\\.git\\*" '
        '-and $_.Name -match "{}" }} '
        "| Remove-Item -Recurse -Force"
    )
    FILE_OPENER = "start {}"


@dataclass
class TaskResult:
    """Dataclass to store Invoke task runs exit code."""

    name: str
    return_code: int

    @property
    def failed(self) -> bool:
        """Return the task's exit code."""
        return self.return_code != 0


class TaskRunner:
    """Helper class to track and report task execution results."""

    def __init__(self):
        self.results: list[TaskResult] = []

    def run_task(
        self, task_func: Callable, task_name: str, *args, **kwargs
    ) -> TaskResult:
        """Execute a task and track its result."""
        return_code = task_func(*args, **kwargs)
        result = TaskResult(task_name, return_code)

        self.results.append(result)

        return result

    def get_failed_tasks(self) -> list[TaskResult]:
        """Get all tasks that failed."""
        return [result for result in self.results if result.failed]

    def has_failures(self) -> bool:
        """Check if any tasks failed."""
        return any(result.failed for result in self.results)

    def get_failure_summary(self) -> str:
        """Generate a detailed failure summary."""
        failed = self.get_failed_tasks()

        if not failed:
            return "All tasks completed successfully"

        failed_names = [
            f"{task.name} (exit code {task.return_code})" for task in failed
        ]
        failed_output = ", ".join(failed_names)

        return f"Unsuccessful tasks: {failed_output}"


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

    result = c.run(
        f"{poetry_path} env info --path", hide=hide, warn=True, pty=IS_UNIX_OS
    )

    if result.failed:
        msg = f"unable to fetch Poetry virtual environment for {PROJECT_NAME}"
        raise Exit(msg)

    c.venv_bin_path = Path(result.stdout.strip()).resolve() / BIN_DIR


@task(call(venv, hide=True))
def mypy(
    c: Context,
    install_types: bool = False,
    non_interactive: bool = False,
    warn: bool = False,
) -> int:
    """Run type checks with `mypy` and `pyproject.toml` configuration."""
    install_flag = "--install-types" if install_types else ""
    non_interactive_flag = "--non-interactive" if non_interactive else ""

    result = c.run(
        f"{c.venv_bin_path}/mypy --config-file pyproject.toml {install_flag} "
        f"{non_interactive_flag}",
        pty=IS_UNIX_OS,
        warn=warn,
    )

    return result.return_code


@task(call(venv, hide=True), aliases=["pre-commit-install", "install-hooks"])
def hooks(c: Context) -> None:
    """Install pre-commit hooks."""
    c.run(
        f"{c.venv_bin_path}/pre-commit install --hook-type pre-commit", pty=IS_UNIX_OS
    )
    c.run(f"{c.venv_bin_path}/pre-commit install --hook-type pre-push", pty=IS_UNIX_OS)
    c.run(
        f"{c.venv_bin_path}/pre-commit install --hook-type commit-msg", pty=IS_UNIX_OS
    )


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
    c.run(f"{poetry_path} sync -n", pty=local_pty)


# Formatting, linting and other checks
@task(call(venv, hide=True), aliases=["format"])
def codestyle(c: Context, check: bool = False, warn: bool = False) -> int:
    """Format the entire project with `ruff format`."""
    flag = "--check" if check else ""

    result = c.run(f"{c.venv_bin_path}/ruff format {flag}", pty=IS_UNIX_OS, warn=warn)

    return result.return_code


@task(call(venv, hide=True), aliases=["check-linter"])
def lint(c: Context, fix: bool = False, warn: bool = False) -> int:
    """Check linting rules with `ruff check`."""
    flag = "--fix" if fix else ""

    result = c.run(f"{c.venv_bin_path}/ruff check {flag}", pty=IS_UNIX_OS, warn=warn)

    return result.return_code


@task(call(venv, hide=True))
def ruff(c: Context) -> None:
    """Perform formatting and linting in a single task with Ruff."""
    runner = TaskRunner()

    runner.run_task(codestyle, "Ruff format", c, check=False, warn=True)
    runner.run_task(lint, "Ruff check", c, fix=True, warn=True)

    if runner.has_failures():
        failed_count = len(runner.get_failed_tasks())
        failed_summary = runner.get_failure_summary()

        descriptive_message = "A Ruff task" if failed_count == 1 else "Both Ruff tasks"

        msg = f"{descriptive_message} returned warnings. {failed_summary}"

        raise Exit(msg)


@task(call(venv, hide=True), incrementable=["verbosity"])
def test(c: Context, verbosity: int = 0, warn: bool = False) -> int:  # noqa: PT028
    """Run tests with Pytest and `pyproject.toml` configuration."""
    verbosity_level = min(verbosity, 3)
    flag = "-" + verbosity_level * "v" if verbosity_level > 0 else ""

    result = c.run(
        f"{c.venv_bin_path}/pytest -c pyproject.toml {flag} tests",
        pty=IS_UNIX_OS,
        warn=warn,
    )

    c.run(f"{c.venv_bin_path}/coverage xml", pty=IS_UNIX_OS, warn=True)
    c.run(f"{c.venv_bin_path}/coverage html", pty=IS_UNIX_OS, warn=True)

    return result.return_code


@task(call(venv, hide=True), aliases=["coverage"])
def report(c: Context, pytest: bool = False, annotations: bool = False) -> None:
    """Run test and type checking suites, and open their HTML reports."""
    runner = TaskRunner()

    runner.run_task(test, "Pytest", c, warn=True)
    runner.run_task(mypy, "Type checks", c, warn=True)

    if not annotations:
        c.run(FILE_OPENER.format("htmlcov/index.html"))

    if not pytest:
        c.run(FILE_OPENER.format("mypycov/index.html"))

    if runner.has_failures():
        failed_count = len(runner.get_failed_tasks())
        failed_summary = runner.get_failure_summary()

        descriptive_message = (
            "One coverage check" if failed_count == 1 else "Both coverage checks"
        )

        msg = f"{descriptive_message} did not pass. {failed_summary}"
        raise Exit(msg)


@task(call(venv, hide=True), pyproject, aliases=["safety", "check-safety", "sec"])
def security(c: Context, warn: bool = False) -> int:
    """Perform security checks with Bandit."""
    result = c.run(
        f"{c.venv_bin_path}/bandit -ll -c pyproject.toml --recursive hooks",
        pty=IS_UNIX_OS,
        warn=warn,
    )

    return result.return_code


@task(call(venv, hide=True))
def sweep(c: Context) -> None:
    """Perform all code checks, including tests, linting and security."""
    runner = TaskRunner()

    # Execute all tasks and track results
    runner.run_task(test, "Pytest", c, warn=True)
    runner.run_task(lint, "Ruff check", c, warn=True)
    runner.run_task(codestyle, "Ruff format", c, check=True, warn=True)
    runner.run_task(mypy, "Type checks", c, warn=True)
    runner.run_task(security, "Security check", c, warn=True)

    if runner.has_failures():
        failed_count = len(runner.get_failed_tasks())
        total_count = len(runner.results)
        failed_summary = runner.get_failure_summary()

        pluralized_text = "task" if failed_count == 1 else "tasks"

        msg = (
            f"Sweep completed with {failed_count}/{total_count} {pluralized_text} not "
            f"passing.\n{failed_summary}"
        )
        raise Exit(msg)


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
    c.run(
        FILE_REMOVER.format(r"(.mypy_cache|mypy_report.xml|mypycov|mypy_coverage)"),
        pty=IS_UNIX_OS,
    )


@task(aliases=["rm-ipynb", "clean-ipynb"])
def remove_ipynb(c: Context) -> None:
    """Remove ipynb checkpoints from project directory."""
    c.run(FILE_REMOVER.format(".ipynb_checkpoints"), pty=IS_UNIX_OS)


@task(aliases=["rm-pytest", "clean-pytest"])
def remove_pytest(c: Context) -> None:
    """Remove Pytest cache files from project directory."""
    c.run(
        FILE_REMOVER.format(
            r"(.pytest_cache|.coverage|test_report.xml|htmlcov|assets)"
        ),
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
