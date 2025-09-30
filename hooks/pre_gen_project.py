"""Module to be called by Cookiecutter before the project is created."""

import re
import sys

REPO_NAME = "{{ cookiecutter.repo_name }}"
PACKAGE_NAME = "{{ cookiecutter.package_name }}"
NAMESPACE = "{{ cookiecutter.scm_namespace }}"
# Integer value wrapped inside strings to avoid raising errors when testing
LINE_LENGTH_PARAMETER = "{{ cookiecutter.line_length }}"
DOCSTRING_LENGTH_PARAMETER = "{{ cookiecutter.docstring_length }}"


MIN_NAMESPACE_LENGTH = 2
MAX_NAMESPACE_LENGTH = 255
MIN_LINE_LENGTH = 50
MAX_LINE_LENGTH = 300


PROJECT_REGEX = re.compile(
    r"""
        ^
        [a-zA-Z0-9]             # Must begin with letter or number
        (?!.*([._-]){2})        # Must not have any two consecutive of . - _ ahead
        [a-zA-Z0-9\.\_\-]*      # Can contain any letters, numbers or . - _
        [a-zA-Z0-9]             # Must end with letter or number
        (?<!\.atom)             # Must not end with .atom
        (?<!\.git)              # Must not end with .git
        $
    """,
    re.VERBOSE,
)
PACKAGE_REGEX = re.compile(r"^[a-z][a-z0-9\_]+[a-z0-9]$")
USERNAME_REGEX = re.compile(
    r"""
        ^[a-zA-Z0-9]            # Must begin with letter or number
        (?!.*(-){2})            # Must not have any two consecutive - ahead
        [a-zA-Z0-9\-]*          # Can contain any letters, numbers or -
        [a-zA-Z0-9]             # Must end with letter or number
        $
    """,
    re.VERBOSE,
)

# Reserved project and group names in GitLab
# https://docs.gitlab.com/ee/user/reserved_names.html#reserved-project-names
RESERVED_PROJECTS = [
    r"\-",
    "badges",
    "blame",
    "blob",
    "builds",
    "commits",
    "create",
    "create_dir",
    "edit",
    "environments/folders",
    "files",
    "find_file",
    "gitlab-lfs/objects",
    "info/lfs/objects",
    "new",
    "preview",
    "raw",
    "refs",
    "tree",
    "update",
    "wikis",
]

# https://docs.gitlab.com/ee/user/reserved_names.html#reserved-group-names
RESERVED_NAMESPACES = [
    r"\-",
    ".well-known",
    "404.html",
    "422.html",
    "500.html",
    "502.html",
    "503.html",
    "admin",
    "api",
    "apple-touch-icon.png",
    "assets",
    "dashboard",
    "deploy.html",
    "explore",
    "favicon.ico",
    "favicon.png",
    "files",
    "groups",
    "health_check",
    "help",
    "import",
    "jwt",
    "login",
    "oauth",
    "profile",
    "projects",
    "public",
    "robots.txt",
    "s",
    "search",
    "sitemap",
    "sitemap.xml",
    "sitemap.xml.gz",
    "slash-command-logo.png",
    "snippets",
    "unsubscribes",
    "uploads",
    "users",
    "v2",
]


def validate_repo_name(repo_name: str, reserved_projects: list[str]) -> None:
    """Ensure that `repo_name` is valid under GitLab restrictions.

    Valid input starts with a digit or letter, can be comprised of any
    digits, letters and the special characters dashes, underscores, dots or
    plus signs, but must not contain any two of those special characters.
    It must also not end on a special character nor the strings ".git" and
    ".atom".

    Also checks for reserved GitLab project names.

    Parameters
    ----------
    repo_name : str
        Current project repository slug.
    reserved_projects : list
        List of reserved project names that can not be used.

    Raises
    ------
    ValueError
        If `repo_name` is not a valid GitLab slug.
    """
    if PROJECT_REGEX.fullmatch(repo_name) is None:
        message = (
            f"ERROR: The project slug `{repo_name}` is not a valid GitLab/GitHub name."
        )
        raise ValueError(message)

    if repo_name in reserved_projects:
        message = f"ERROR: The project slug `{repo_name}` is a reserved project name."
        raise ValueError(message)


def validate_package_name(package_name: str) -> None:
    """Ensure that `package_name` is valid under Python restrictions.

    Valid inputs starts with the lowercase letter, followed by any
    lowercase letters, digits or underscores. It must end on a lowercase
    letter or digit.

    Parameters
    ----------
    package_name : str
        Current project package name.

    Raises
    ------
    ValueError
        If `package_name` is not a valid Python module name.
    """
    if PACKAGE_REGEX.fullmatch(package_name) is None:
        message = (
            f"ERROR: The package name `{package_name}` "
            "is not a valid Python module name."
        )
        raise ValueError(message)


def validate_namespace(namespace: str, reserved_names: list[str]) -> None:
    """Ensure that `username` is valid under GitLab and GitHub restrictions.

    Parameters
    ----------
    username : str
        Source control management platform username.
    reserved_projects : list
        List of reserved usernames that can not be used.

    Raises
    ------
    ValueError
        If `username` is not a valid GitLab or GitHub username.
    """
    if not (MIN_NAMESPACE_LENGTH <= len(namespace) <= MAX_NAMESPACE_LENGTH):
        message = (
            f"ERROR: scm_namespace must be between 2 and 255. Got `{len(namespace)}`."
        )
        raise ValueError(message)

    message = f"ERROR: `{namespace}` is not a valid name for user or organisation."

    if USERNAME_REGEX.fullmatch(namespace) is None:
        raise ValueError(message)
    if namespace in reserved_names:
        raise ValueError(message)


def validate_line_length(line_length: int) -> None:
    """Validate line_length parameter. Length should be between 50 and 300.

    Parameters
    ----------
    line_length : int
        Integer parameter for Ruff formatter.

    Raises
    ------
    ValueError
        If line_length isn't between 50 and 300.
    """
    if not (MIN_LINE_LENGTH <= line_length <= MAX_LINE_LENGTH):
        message = f"ERROR: line_length must be between 50 and 300. Got `{line_length}`."
        raise ValueError(message)


def validate_docstring_length(line_length: int, docstring_length: int) -> None:
    """Validate docstring_length parameter against line_length.

    Parameters
    ----------
    line_length : int
        Integer parameter for maximum line length for Ruff formatter.
    docstring_length : int
        Integer parameter for maximum docstring line length for Ruff formatter.

    Raises
    ------
    ValueError
        If docstring_length is greater than line_length
    """
    if docstring_length > line_length:
        message = (
            f"ERROR: docstring_length of {docstring_length} is greater than "
            f"line_length {line_length}"
        )
        raise ValueError(message)


def main() -> None:  # noqa: D103
    try:
        validate_repo_name(repo_name=REPO_NAME, reserved_projects=RESERVED_PROJECTS)

        validate_package_name(package_name=PACKAGE_NAME)

        validate_namespace(namespace=NAMESPACE, reserved_names=RESERVED_NAMESPACES)

        validate_line_length(line_length=int(LINE_LENGTH_PARAMETER))

        validate_line_length(line_length=int(DOCSTRING_LENGTH_PARAMETER))

        validate_docstring_length(
            line_length=int(LINE_LENGTH_PARAMETER),
            docstring_length=int(DOCSTRING_LENGTH_PARAMETER),
        )

    except ValueError as ex:
        print(ex)

        sys.exit(1)


if __name__ == "__main__":
    main()
