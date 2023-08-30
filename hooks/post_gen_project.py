"""This module is called after project is created."""
from typing import List

import textwrap
from pathlib import Path
from shutil import move, rmtree

# Project root directory
PROJECT_DIRECTORY = Path.cwd().absolute()
PROJECT_NAME = "{{ cookiecutter.project_name }}"
PROJECT_REPO = "{{ cookiecutter.repo_name }}"
PROJECT_PACKAGE = "{{ cookiecutter.package_name }}"
CREATE_EXAMPLE_TEMPLATE = "{{ cookiecutter.create_example_template }}"

# Values to generate correct licence
LICENCE = "{{ cookiecutter.licence }}"
AUTHOR = "{{ cookiecutter.author }}"

# Values to generate github repository
SCM_PLATFORM = "{{ cookiecutter.scm_platform }}"
SCM_USERNAME = "{{ cookiecutter.scm_username }}"
SCM_BASE_URL = "{{ cookiecutter.__scm_base_url }}"

licences_dict = {
    "MIT": "mit",
    "BSD-3": "bsd3",
    "GNU GPL v3.0": "gpl3",
    "GNU AGPL v3.0": "agpl3",
    "GNU LGPL v3.0": "lgpl3",
    "Mozilla Public License 2.0": "mozilla",
    "Apache Software License 2.0": "apache",
}


platforms_dict = {
    "gitlab": "GitLab",
    "github": "GitHub",
}


def generate_licence(directory: Path, licence: str) -> None:
    """Generate licence file for the project.

    Args:
        directory: path to the project directory
        licence: chosen licence
    """
    move(str(directory / "_licences" / f"{licence}.txt"), str(directory / "LICENCE"))
    rmtree(str(directory / "_licences"))


def remove_unused_files(directory: Path, module_name: str, need_to_remove_cli: bool) -> None:
    """Remove unused files.

    Args:
        directory: path to the project directory
        module_name: project module name
        need_to_remove_cli: flag for removing CLI related files
    """
    files_to_delete: List[Path] = []

    def _cli_specific_files() -> List[Path]:
        return [directory / module_name / "__main__.py"]

    if need_to_remove_cli:
        files_to_delete.extend(_cli_specific_files())

    for path in files_to_delete:
        path.unlink()


def print_futher_instuctions(project_name: str, project_repo: str, scm_platform: str, scm_base_url: str) -> None:
    """Show user what to do next after project creation.

    Args:
        project_name: current project name
        github: GitHub username
    """
    message = f"""
    Your project {project_name} is created.

    1) Now you can start working on it:

        $ cd {project_repo} && git init

    2) If you don't have Poetry installed run:

        $ make poetry-download

    3) Initialize poetry and install pre-commit hooks:

        $ make install
        $ make pre-commit-install

    4) Run codestyle:

        $ make codestyle

    5) Upload initial code to {scm_platform}:

        $ git add .
        $ git commit -m ":tada: Initial commit"
        $ git remote add origin {scm_base_url}.git
        $ git push -u origin master
    """
    print(textwrap.dedent(message))


def main() -> None:
    generate_licence(directory=PROJECT_DIRECTORY, licence=licences_dict[LICENCE])
    remove_unused_files(
        directory=PROJECT_DIRECTORY,
        module_name=PROJECT_PACKAGE,
        need_to_remove_cli=CREATE_EXAMPLE_TEMPLATE != "cli",
    )
    print_futher_instuctions(
        project_name=PROJECT_NAME,
        project_repo=PROJECT_REPO,
        scm_platform=platforms_dict[SCM_PLATFORM],
        scm_base_url=SCM_BASE_URL
    )


if __name__ == "__main__":
    main()
