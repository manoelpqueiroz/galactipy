"""Module to be called after the project is created."""

import textwrap
from importlib.util import find_spec
from pathlib import Path
from shutil import move

# Project root directory
PROJECT_DIRECTORY = Path.cwd().absolute()
PROJECT_NAME = "{{ cookiecutter.project_name }}"
PROJECT_REPO = "{{ cookiecutter.repo_name }}"
PROJECT_PACKAGE = "{{ cookiecutter.package_name }}"

# Values to generate correct licence
LICENCE = "{{ cookiecutter.licence }}"
AUTHOR = "{{ cookiecutter.author }}"

# Values to generate repository information
SCM_PLATFORM = "{{ cookiecutter.scm_platform }}"
SCM_PLATFORM_LC = "{{ cookiecutter.__scm_platform_lc }}"
SCM_USERNAME = "{{ cookiecutter.scm_username }}"
SCM_BASE_URL = "{{ cookiecutter.__scm_base_url }}"

# Boolean variables for additional project structures
# Values wrapped inside strings and evaluated against the "True" string to
# avoid raising errors when testing
CREATE_CLI = "{{ cookiecutter.bare_repo }}" == "False"  # type: ignore[comparison-overlap] # noqa: PLR0133
CREATE_DOCKER = "{{ cookiecutter.create_docker }}" == "True"  # type: ignore[comparison-overlap] # noqa: PLR0133
USE_BDD = "{{ cookiecutter.use_bdd }}" == "True"  # type: ignore[comparison-overlap] # noqa: PLR0133

licences_dict = {
    "MIT": "mit",
    "BSD-3": "bsd3",
    "GNU GPL v3.0": "gpl3",
    "GNU AGPL v3.0": "agpl3",
    "GNU LGPL v3.0": "lgpl3",
    "Mozilla Public License 2.0": "mozilla",
    "Apache Software License 2.0": "apache",
    "nos": None,
}


def rmdir(path: Path) -> None:
    """Recursively remove a directory with Pathlib.

    Parameters
    ----------
    path : Path
        A pathlib Path to remove. If a directory, removes recursively all
        files and subdirectories. If a file, simply removes the file.
    """
    if path.is_dir():
        for item in path.iterdir():
            if item.is_dir():
                rmdir(item)

            else:
                item.unlink()

        path.rmdir()

    elif path.is_file():
        path.unlink()

    else:
        message = f"{path} is neither a file nor a directory to remove."
        raise ValueError(message)


def generate_licence(directory: Path, licence: str | None) -> None:
    """Generate licence file for the project.

    Parameters
    ----------
    directory : Path
        Path to the project directory.
    licence : str
        Chosen licence.
    """
    if licence is not None:
        licence_origin = directory / "_licences" / f"{licence}.txt"

        licence_origin.rename(directory / "LICENCE")

    rmdir(directory / "_licences")


def generate_templates(directory: Path, scm_platform: str) -> None:
    """Generate source control management platform structure and templates.

    Removes the "_templates" directory afterwards.

    Parameters
    ----------
    directory : Path
        Path to the project directory.
    scm_platform : str
        Name of the project's source control management platform in
        lowercase.
    """
    template_dir = f".{scm_platform}"

    move(directory / "_templates" / template_dir, directory / template_dir)

    rmdir(directory / "_templates")


def remove_unused_files(
    directory: Path,
    package_name: str,
    remove_cli: bool,
    remove_gitlab: bool,
    remove_docker: bool,
    remove_bdd: bool,
) -> None:
    """Remove unused files.

    Parameters
    ----------
    directory : Path
        path to the project directory.
    package_name : str
        Project module name.
    remove_cli : bool
        Flag for removing CLI related files.
    remove_gitlab : bool
        Flag for removing GitLab related files.
    remove_docker : bool
        Flag for removing Docker related files.
    remove_bdd : bool
        Flag for removing BDD related files.
    """
    files_to_delete = _get_files_to_delete(
        directory, package_name, remove_cli, remove_gitlab, remove_docker, remove_bdd
    )

    for path in files_to_delete:
        rmdir(path)


def _get_files_to_delete(
    directory: Path,
    package_name: str,
    remove_cli: bool,
    remove_gitlab: bool,
    remove_docker: bool,
    remove_bdd: bool,
) -> list[Path]:
    """Determine files to be removed from tree at template generation.

    Parameters
    ----------
    directory : Path
        path to the project directory.
    package_name : str
        Project module name.
    remove_cli : bool
        Flag for removing CLI related files.
    remove_gitlab : bool
        Flag for removing GitLab related files.
    remove_docker : bool
        Flag for removing Docker related files.
    remove_bdd : bool
        Flag for removing BDD related files.
    """
    files_to_delete: list[Path] = []

    cli_specific_files = _get_cli_specific_files(directory, package_name, remove_bdd)
    docker_specific_files = _get_docker_specific_files(directory, remove_gitlab)

    gitlab_specific_files = [
        directory / ".gitlab-ci.yml",
        directory / ".triage-policies.yml",
    ]

    bdd_specific_files = [directory / "tests" / "features"]

    if not remove_cli and not remove_bdd:
        files_to_delete.append(directory / "tests" / "features" / ".gitkeep")

    if remove_cli:
        files_to_delete.extend(cli_specific_files)

    else:
        files_to_delete.append(directory / "tests" / ".gitkeep")

    if remove_gitlab:
        files_to_delete.extend(gitlab_specific_files)

    if remove_docker:
        files_to_delete.extend(docker_specific_files)

    if remove_bdd:
        files_to_delete.extend(bdd_specific_files)

    return files_to_delete


def _get_cli_specific_files(
    directory: Path, package_name: str, remove_bdd: bool
) -> list[Path]:
    """Return select files to remove when CLI option is disabled.

    Parameters
    ----------
    directory : Path
        Root directory of the project.
    package_name : str
        Name of the package under the root directory of the project.
    remove_bdd : bool
        Determine whether CLI feature file should be removed as well.
    """
    removals = [
        directory / package_name / "cli",
        directory / package_name / "__main__.py",
        directory / "tests" / "cli",
        directory / "tests" / "conftest.py",
    ]

    if not remove_bdd:
        removals.append(directory / "tests" / "features" / "root_command.feature")

    return removals


def _get_docker_specific_files(directory: Path, is_github: bool) -> list[Path]:
    """Return select files to remove when the Docker option is disabled.

    Parameters
    ----------
    directory : Path
        Root directory of the project.
    is_github : bool
        Determine whether GitHub Docker workflow should be removed as well.
    """
    removals = [directory / ".dockerignore", directory / "docker"]

    if is_github:
        removals.append(directory / ".github" / "workflows" / "docker.yml")

    return removals


def print_further_instructions(
    project_name: str, project_repo: str, scm_platform: str, scm_base_url: str
) -> None:
    """Show user what to do next after project creation.

    Parameters
    ----------
    project_name : str
        Current project name.
    project_repo : str
        Current project repository slug.
    scm_platform : str
        Name of the project's source control management platform in
        lowercase.
    scm_base_url : str
        URL for the project's repository in `scm_platform`, consisting of
        username and repository slug.
    """
    if find_spec("rich") is not None:
        from rich.console import Console

        console = Console(emoji=False)

        message = textwrap.dedent(
            f"""
            Your project [bold][italic]{project_name}[/italic][/bold] is created.

            1) Now you can start working on it:

                [bold red]$[/] [green]cd[/] [underline magenta]{project_repo}[/] && [green]git[/] [yellow]init[/]

            2) If you don't have Poetry installed run:

                [bold red]$[/] [green]invoke[/] [blue]poetry-download[/]

            3) Initialize Poetry and install pre-commit hooks:

                [bold red]$[/] [green]invoke[/] [blue]install[/]
                [bold red]$[/] [green]invoke[/] [blue]pre-commit-install[/]

            4) Run codestyle:

                [bold red]$[/] [green]invoke[/] [blue]codestyle[/]

            5) Upload initial code to {scm_platform}:

                [bold red]$[/] [green]git[/] [yellow]add[/] [blue].[/]
                [bold red]$[/] [green]git[/] [yellow]commit[/] [blue]-m[/] [yellow]":tada: Initial commit"[/]
                [bold red]$[/] [green]git[/] [yellow]remote add[/] [red]origin[/] [blue]{scm_base_url}.git[/]
                [bold red]$[/] [green]git[/] [yellow]push[/] [cyan]-u[/] [blue]origin master[/]
            """  # noqa: E501
        )

        if find_spec("invoke") is None:
            message += textwrap.dedent(
                """
                [bold red]WARNING![/] Invoke was not found in your system.

                Install it first via your package manager or via pip before running step 2.

                    [bold red]$[/] [green]pip[/] [yellow]install[/] invoke
                """  # noqa: E501
            )

        console.print(message)

    else:
        message = textwrap.dedent(
            f"""
            Your project {project_name} is created.

            1) Now you can start working on it:

                $ cd {project_repo} && git init

            2) If you don't have Poetry installed run:

                $ invoke poetry-download

            3) Initialize Poetry and install pre-commit hooks:

                $ invoke install
                $ invoke pre-commit-install

            4) Run codestyle:

                $ invoke codestyle

            5) Upload initial code to {scm_platform}:

                $ git add .
                $ git commit -m ":tada: Initial commit"
                $ git remote add origin {scm_base_url}.git
                $ git push -u origin master
            """
        )

        if find_spec("invoke") is None:
            message += textwrap.dedent(
                """
                WARNING! Invoke was not found in your system.

                Install it first via your package manager or via pip before running step 2.

                    $ pip install invoke
                """  # noqa: E501
            )

        print(message)


def main() -> None:  # noqa: D103
    remove_gitlab = SCM_PLATFORM_LC != "gitlab"
    remove_cli = not CREATE_CLI
    remove_docker = not CREATE_DOCKER
    remove_bdd = not USE_BDD

    generate_licence(directory=PROJECT_DIRECTORY, licence=licences_dict[LICENCE])

    generate_templates(directory=PROJECT_DIRECTORY, scm_platform=SCM_PLATFORM_LC)

    remove_unused_files(
        directory=PROJECT_DIRECTORY,
        package_name=PROJECT_PACKAGE,
        remove_cli=remove_cli,
        remove_gitlab=remove_gitlab,
        remove_docker=remove_docker,
        remove_bdd=remove_bdd,
    )

    print_further_instructions(
        project_name=PROJECT_NAME,
        project_repo=PROJECT_REPO,
        scm_platform=SCM_PLATFORM,
        scm_base_url=SCM_BASE_URL,
    )


if __name__ == "__main__":
    main()
