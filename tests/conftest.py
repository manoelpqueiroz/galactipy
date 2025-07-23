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
        "file1_feature.md",
        package_test=["__main__.py"],
        docker=["Dockerfile", "README.md", "file2_feature.md"],
    )

    github_directory = tmp_path / ".github"
    bulk_file_creation(github_directory, workflows=["docker.yml", "test.yml"])

    feature_directory = tmp_path / "directory_feature"
    bulk_file_creation(
        feature_directory,
        "sample_file_1.md",
        subdirectory=["sample_file_2.md", "sample_file_3"],
    )

    tests_directory = tmp_path / "tests"
    bulk_file_creation(
        tests_directory,
        "conftest.py",
        ".gitkeep",
        features=[".gitkeep", "root_command.feature", "main_window.feature"],
        cli=["test_root_command.py"],
        tui=["test_main_window.py"],
        helpers=["tui_helpers.py"],
        utils=["pytest_bdd_async.py"],
    )

    cli_directory = tmp_path / package_name / "cli"
    bulk_file_creation(
        cli_directory, "root_command.py", commands=[".gitkeep", "launch.py"]
    )

    tui_directory = tmp_path / package_name / "tui"
    bulk_file_creation(
        tui_directory,
        "main_window.py",
        "themes.py",
        components=[".gitkeep"],
        css=["demo.tcss", "noctis.tcss"],
    )

    return {
        "root": tmp_path,
        "package_name": package_name,
        "pyproject": tmp_path / "pyproject.toml",
        "features": {
            "file1": tmp_path / "file1_feature.md",
            "file2": tmp_path / "docker" / "file2_feature.md",
            "directory": feature_directory,
            "subdirectory": feature_directory / "subdirectory",
            "sample1": feature_directory / "sample_file_1.md",
            "sample2": feature_directory / "subdirectory" / "sample_file_2.md",
            "sample3": feature_directory / "subdirectory" / "sample_file_3",
        },
        "cli": {
            "root": cli_directory,
            "root_command": cli_directory / "root_command.py",
            "commands": {
                "root": cli_directory / "commands",
                "gitkeep": cli_directory / "commands" / ".gitkeep",
                "launch": cli_directory / "commands" / "launch.py",
            },
            "main": tmp_path / package_name / "__main__.py",
        },
        "tui": {
            "root": tui_directory,
            "main_window": tui_directory / "main_window.py",
            "themes": tui_directory / "themes.py",
            "components": {
                "root": tui_directory,
                "gitkeep": tui_directory / "components" / ".gitkeep",
            },
            "css": {
                "root": tui_directory / "css",
                "demo": tui_directory / "css" / "demo.tcss",
                "noctis": tui_directory / "css" / "noctis.tcss",
            },
        },
        "tests": {
            "root": tests_directory,
            "cli": {
                "root": tests_directory / "cli",
                "test": tests_directory / "cli" / "test_root_command.py",
            },
            "tui": {
                "root": tests_directory / "tui",
                "test": tests_directory / "tui" / "test_main_window.py",
            },
            "conftest": tests_directory / "conftest.py",
            "gitkeep": tests_directory / ".gitkeep",
        },
        "bdd": {
            "root": tests_directory / "features",
            "cli": tests_directory / "features" / "root_command.feature",
            "tui": tests_directory / "features" / "main_window.feature",
            "gitkeep": tests_directory / "features" / ".gitkeep",
            "helpers": {
                "root": tests_directory / "helpers",
                "tui": tests_directory / "helpers" / "tui_helpers.py",
            },
            "utils": {
                "root": tests_directory / "utils",
                "bdd": tests_directory / "utils" / "pytest_bdd_async.py",
            },
        },
        "github": {
            "root": tmp_path / ".github",
            "test_workflow": tmp_path / ".github" / "workflows" / "test.yml",
        },
        "gitlab": {
            "ci": tmp_path / ".gitlab-ci.yml",
            "triage": tmp_path / ".triage-policies.yml",
        },
        "docker": {
            "root": tmp_path / "docker",
            "dockerfile": tmp_path / "docker" / "Dockerfile",
            "readme": tmp_path / "docker" / "README.md",
            "github_workflow": tmp_path / ".github" / "workflows" / "docker.yml",
            "dockerignore": tmp_path / ".dockerignore",
        },
    }


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
