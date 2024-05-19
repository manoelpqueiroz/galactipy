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

    # Python functions do not accept a leading . for keywords, so the folder structure
    # has to be created first manually, then detailed with `bulk_file_creation`
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
        workflows=["build.yml", "greetings.yml", "release-drafter.yml"],
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
    bulk_file_creation(
        tmp_path,
        ".gitlab-ci.yml",
        ".dockerignore",
        "pyproject.toml",
        package_test=["__main__.py"],
        docker=["Dockerfile", "README.md"],
        docs=[".gitkeep"],
        tests=["test_hello.py"],
    )

    pyproject_file = tmp_path / "pyproject.toml"
    tests_directory = tmp_path / "tests"
    test_file = tests_directory / "test_hello.py"

    package_name = "package_test"

    return tmp_path, pyproject_file, tests_directory, test_file, package_name


@pytest.fixture
def galactipy_instructions():
    message = """
    Your project Galactipy is created.

    1) Now you can start working on it:

        $ cd galactipy && git init

    2) If you don't have Poetry installed run:

        $ make poetry-download

    3) Initialize poetry and install pre-commit hooks:

        $ make install
        $ make pre-commit-install

    4) Run codestyle:

        $ make codestyle

    5) Upload initial code to GitLab:

        $ git add .
        $ git commit -m ":tada: Initial commit"
        $ git remote add origin https://www.gitlab.com/manoelpqueiroz/galactipy.git
        $ git push -u origin master
    """

    return textwrap.dedent(message)
