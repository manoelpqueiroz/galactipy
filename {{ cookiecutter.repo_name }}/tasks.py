from typing import Optional

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

PROJECT_NAME = "{{ cookiecutter.repo_name }}"
{%+ if cookiecutter.create_docker %}
{%- if cookiecutter.__scm_platform_lc == 'gitlab' %}
DOCKER_REGISTRY = "registry.gitlab.com"
DEFAULT_DOCKER_REPOSITORY = f"{DOCKER_REGISTRY}/{{ cookiecutter.scm_username }}/{{ cookiecutter.repo_name }}"
{%- else %}
DEFAULT_DOCKER_REPOSITORY = "{{ cookiecutter.scm_username }}/{{ cookiecutter.repo_name }}"
{%- endif %}
DEFAULT_DOCKER_TAG = "latest"
DEFAULT_DOCKER_IMAGE = f"{DEFAULT_DOCKER_REPOSITORY}:{DEFAULT_DOCKER_TAG}"
{% endif %}

# Reusable command templates
if IS_UNIX_OS:
    FILE_REMOVER = 'find . | grep -E "{}" | xargs rm -rf'

else:
    FILE_REMOVER = (
        "Get-ChildItem -Recurse "
        '| Where-Object {% raw %}{{ $_.Name -match "{}" }}{% endraw %} '
        "| Remove-Item -Recurse"
    )


def get_poetry_command() -> Path:
    """Retrieve the executable path for Poetry.

    Returns
    -------
    Path
        Path to the Poetry executable. If no path is found, will use the system's
        default paths for a Poetry installation.
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
    """Install dependencies specified in `pyproject.toml` and run mypy."""
    poetry_path = get_poetry_command()
    local_pty = False if ignore_pty else IS_UNIX_OS

    c.run(f"{poetry_path} lock -n", pty=local_pty)
    c.run(f"{poetry_path} install -n", pty=local_pty)


# Packaging-related tasks
@task(aliases=["pypi-config"])
def config(
    c: Context, api_token: str, repo: str = "pypi", url: Optional[str] = None
) -> None:
    """Configure a PyPI API token for package uploads.

    If an alternate registry is provided to the `repo` argument, the `url` argument must
    also be provided, except for the "testpypi" repo.
    """
    poetry_path = get_poetry_command()
    package_registry_url_configurator = "{path} config repositories.{repo} {url}"

    if repo == "testpypi":
        c.run(
            package_registry_url_configurator.format(
                path=poetry_path, repo=repo, url="https://test.pypi.org/legacy/"
            ),
            pty=IS_UNIX_OS,
        )

    elif repo != "pypi" and url is None:
        msg = f"repository URL not set for {repo}"
        raise Exit(msg)

    elif url is not None:
        c.run(
            package_registry_url_configurator.format(
                path=poetry_path, repo=repo, url=url
            ),
            pty=IS_UNIX_OS,
        )

    c.run(f"{poetry_path} config pypi-token.{repo} {api_token}", pty=IS_UNIX_OS)


@task
def build(c: Context) -> None:
    """Build {{ cookiecutter.project_name }} wheels."""
    poetry_path = get_poetry_command()

    c.run(f"{poetry_path} build", pty=IS_UNIX_OS)


@task(aliases=["pypi-publish"])
def publish(c: Context, repo: str = "pypi", build: bool = True) -> None:
    """Publish {{ cookiecutter.project_name }} to a package registry."""
    poetry_path = get_poetry_command()

    # HACK If PyPI is specifically specified as a repo, Poetry fails to recognize it
    repo_flag = f"--repository {repo}" if repo != "pypi" else ""
    build_flag = "--build" if build else ""

    result = c.run(
        f"{poetry_path} publish {repo_flag} {build_flag}",
        hide="err",
        warn=True,
        pty=IS_UNIX_OS,
    )

    if result.failed:
        msg = (
            "unable to upload to the package registry for {repo}"
            "\n\nDid you set up your API token with `invoke config`?"
            "\nIs the registry URL correctly set up?"
            '\nDid you remove any "Private :: Do Not Upload" classifiers from '
            "`pyproject.toml`?"
        )
        raise Exit(msg)


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


@task(call(venv, hide=True), incrementable=["verbosity"])
def test(c: Context, verbosity: int = 0) -> None:  # noqa: PT028
    """Run tests with Pytest and `pyproject.toml` configuration."""
    verbosity_level = min(verbosity, 3)
    flag = "-" + verbosity_level * "v" if verbosity_level > 0 else ""

    c.run(f"{c.venv_bin_path}/pytest -c pyproject.toml {flag} tests", pty=IS_UNIX_OS)


@task(call(venv, hide=True))
def coverage(c: Context) -> None:
    """Generate coverage file in XML for integration with {{ cookiecutter.coverage_service }}."""
    c.run(f"{c.venv_bin_path}/coverage xml", pty=IS_UNIX_OS)


@task(call(venv, hide=True), pyproject, aliases=["safety", "check-safety", "sec"])
def security(c: Context) -> None:
    """Perform security checks with Bandit."""
    c.run(
        f"{c.venv_bin_path}/bandit -ll -c pyproject.toml --recursive {{ cookiecutter.package_name }}",
        pty=IS_UNIX_OS
    )


@task(call(venv, hide=True))
def sweep(c: Context) -> None:
    """Perform all code checks, including tests, linting and security."""
    test(c)
    lint(c)
    codestyle(c, check=True)
    mypy(c)
    security(c)

{%+ if cookiecutter.create_docker %}
# Docker commands
@task(aliases=["docker-login"])
{%- if cookiecutter.__scm_platform_lc == 'gitlab' %}
def login(c: Context, username: str, password: str) -> None:
    """Log in to the GitLab Container Registry using a token.

    More information for authentication methods provided at
    https://docs.gitlab.com/ee/user/packages/container_registry/authenticate_with_container_registry.html
    """
{%- else %}
def login(c: Context, username: str) -> None:
    """Log in to Docker Hub using the one-time device confirmation code."""
{%- endif %}
    if IS_UNIX_OS:
        password_cmd = f"echo {password}"

    else:
        password_cmd = f"Write-Host {password}"

    c.run(
        f"{password_cmd} | "
{%- if cookiecutter.__scm_platform_lc == 'gitlab' %}
        f"docker login {DOCKER_REGISTRY} -u {username} --password-stdin"
{%- else %}
        f"docker login -u {username} --password-stdin"
{%- endif %},
        pty=IS_UNIX_OS,
    )


@task(iterable=["tags"], aliases=["docker-build"])
def container(
    c: Context, tags: list[str], repository: str = DEFAULT_DOCKER_REPOSITORY
) -> None:
    """Build Docker images for {{ cookiecutter.repo_name }}."""
    if len(tags) == 0:
        tags.append(DEFAULT_DOCKER_TAG)

    docker_images = " ".join(f"-t {repository}:{tag}" for tag in tags)

    c.run(
        f"docker build . {docker_images} -f ./docker/Dockerfile --no-cache",
        pty=IS_UNIX_OS
    )


@task(iterable=["tags"], aliases=["docker-remove", "rmi"])
def prune(
    c: Context,tags: list[str], repository: str = DEFAULT_DOCKER_REPOSITORY
) -> None:
    """Remove specified Docker images created for {{ cookiecutter.repo_name }}."""
    if len(tags) == 0:
        docker_images = c.run(
            f"docker images {repository} -qa", hide="out", pty=IS_UNIX_OS
        ).stdout
    else:
        docker_images = " ".join(f"{repository}:{tag}" for tag in tags)

    c.run(f"docker rmi -f {docker_images}", pty=IS_UNIX_OS)


@task(iterable=["tags"], aliases=["docker-push", "deploy"])
def push(
    c: Context, tags: list[str], repository: str = DEFAULT_DOCKER_REPOSITORY
) -> None:
    """Push specified Docker images to a container registry."""
    if len(tags) == 0:
        c.run(f"docker push -a {repository}", pty=IS_UNIX_OS)
    else:
        docker_images = " ".join(f"{repository}:{tag}" for tag in tags)

    c.run(f"docker push -f {docker_images}", pty=IS_UNIX_OS)

{% endif %}
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
        pty=IS_UNIX_OS
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
