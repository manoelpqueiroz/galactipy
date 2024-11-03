"""Module to be called after the project is created."""

import textwrap
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
CREATE_CLI = "{{ cookiecutter.create_cli }}" == "True"  # type: ignore[comparison-overlap] # noqa: PLR0133
CREATE_DOCKER = "{{ cookiecutter.create_docker }}" == "True"  # type: ignore[comparison-overlap] # noqa: PLR0133

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
    """
    files_to_delete: list[Path] = []

    def _cli_specific_files() -> list[Path]:
        return [directory / package_name / "__main__.py"]

    def _gitlab_specific_files() -> list[Path]:
        return [directory / ".gitlab-ci.yml"]

    def _docker_specific_files() -> list[Path]:
        return [directory / ".dockerignore", directory / "docker"]

    if remove_cli:
        files_to_delete.extend(_cli_specific_files())

    if remove_gitlab:
        files_to_delete.extend(_gitlab_specific_files())

    if remove_docker:
        files_to_delete.extend(_docker_specific_files())

    for path in files_to_delete:
        rmdir(path)


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
    message = f"""
    Your project {project_name} is created.

    1) Now you can start working on it:

        $ cd {project_repo} && git init

    2) If you don't have Poetry installed run:

        $ invoke poetry-download

    3) Initialize poetry and install pre-commit hooks:

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
    print(textwrap.dedent(message))


def main() -> None:  # noqa: D103
    remove_gitlab = SCM_PLATFORM_LC != "gitlab"
    remove_cli = not CREATE_CLI
    remove_docker = not CREATE_DOCKER

    generate_licence(directory=PROJECT_DIRECTORY, licence=licences_dict[LICENCE])

    generate_templates(directory=PROJECT_DIRECTORY, scm_platform=SCM_PLATFORM_LC)

    remove_unused_files(
        directory=PROJECT_DIRECTORY,
        package_name=PROJECT_PACKAGE,
        remove_cli=remove_cli,
        remove_gitlab=remove_gitlab,
        remove_docker=remove_docker,
    )

    print_further_instructions(
        project_name=PROJECT_NAME,
        project_repo=PROJECT_REPO,
        scm_platform=SCM_PLATFORM,
        scm_base_url=SCM_BASE_URL,
    )


if __name__ == "__main__":
    main()
