import textwrap

import pytest
from tests.test_helpers import bulk_file_creation


@pytest.fixture
def licence_tree(tmp_path):
    licence_file = tmp_path / "LICENCE"
    licence_root = tmp_path / "_licences"

    bulk_file_creation(
        tmp_path,
        _licences=[
            "agpl3.txt",
            "apache.txt",
            "bsd3.txt",
            "gpl3.txt",
            "lgpl3.txt",
            "mit.txt",
            "mozilla.txt",
        ],
    )

    return tmp_path, licence_root, licence_file


@pytest.fixture
def template_tree(tmp_path):
    template_root = tmp_path / "_templates"
    template_root.mkdir()

    # Python functions do not accept a leading . for keywords, so the folder
    # structure has to be created first manually, then detailed with
    # `bulk_file_creation`
    github_dir = template_root / ".github"
    gitlab_dir = template_root / ".gitlab"

    bulk_file_creation(
        github_dir,
        ".stale.yml",
        "dependabot.yml",
        "PULL_REQUEST_TEMPLATE.md",
        "release-drafter.yml",
        ISSUE_TEMPLATE=[
            "bug_report.md",
            "config.yml",
            "feature_request.md",
            "question.md",
        ],
        workflows=[
            "test.yml",
            "greetings.yml",
            "release-drafter.yml",
            "docker.yml",
            "pypi-prod.yml",
            "pypi-test.yml",
        ],
    )
    bulk_file_creation(
        gitlab_dir,
        "changelog_config.yml",
        issue_templates=["Bug Report.md", "Feature Request.md", "Question.md"],
        merge_request_templates=["default.md"],
    )

    return tmp_path, template_root


@pytest.fixture
def removal_tree(tmp_path):
    package_name = "package_test"

    bulk_file_creation(
        tmp_path,
        ".gitlab-ci.yml",
        ".triage-policies.yml",
        ".dockerignore",
        "pyproject.toml",
        package_test=["__main__.py"],
        docker=["Dockerfile", "README.md"],
    )

    github_directory = tmp_path / ".github"
    bulk_file_creation(github_directory, workflows=["docker.yml", "test.yml"])

    tests_directory = tmp_path / "tests"
    bulk_file_creation(
        tests_directory,
        "conftest.py",
        ".gitkeep",
        features=[".gitkeep", "root_command.feature"],
        cli=["test_root_command.py"],
    )

    cli_directory = tmp_path / package_name / "cli"
    bulk_file_creation(cli_directory, "root_command.py", commands=[".gitkeep"])

    pyproject_file = tmp_path / "pyproject.toml"
    test_file = tests_directory / "cli" / "test_root_command.py"
    feature_file = tests_directory / "features" / "root_command.feature"

    return (
        tmp_path,
        pyproject_file,
        tests_directory,
        test_file,
        feature_file,
        package_name,
    )


@pytest.fixture
def galactipy_instructions():
    message = """
        Your project Galactipy is created.

        1) Now you can start working on it:

            $ cd galactipy && git init

        2) If you don't have Poetry installed run:

            $ invoke poetry-download

        3) Initialize Poetry and install pre-commit hooks:

            $ invoke install
            $ invoke pre-commit-install

        4) Run codestyle:

            $ invoke codestyle

        5) Upload initial code to GitLab:

            $ git add .
            $ git commit -m ":tada: Initial commit"
            $ git remote add origin https://www.gitlab.com/galactipy/galactipy.git
            $ git push -u origin master
    """

    return textwrap.dedent(message)


@pytest.fixture
def galactipy_invoke_instructions(galactipy_instructions):
    extra_message = """
        WARNING! Invoke was not found in your system.

        Install it first via your package manager or via pip before running step 2.

            $ pip install invoke
    """

    return galactipy_instructions + textwrap.dedent(extra_message)
