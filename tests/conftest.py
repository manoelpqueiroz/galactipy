import textwrap

import pytest
from tests.test_helpers import bulk_file_creation


@pytest.fixture
def licence_tree(tmp_path):
    licence_file = tmp_path / "LICENCE"
    licence_root = tmp_path / "_licences"

    header_file = tmp_path / ".licence_header.txt"
    header_root = tmp_path / "_headers"

    licence_list = [
        "agpl3.txt",
        "apache.txt",
        "bsd3.txt",
        "gpl3.txt",
        "lgpl3.txt",
        "mit.txt",
        "mozilla.txt",
    ]

    bulk_file_creation(
        tmp_path, "CODE_OF_CONDUCT.md", _licences=licence_list, _headers=licence_list
    )

    return tmp_path, licence_root, licence_file, header_root, header_file


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
        "release-drafter.yml",
        DISCUSSION_TEMPLATE=["request_for_improvement.yml", "request_for_support.yml"],
        ISSUE_TEMPLATE=[
            "config.yml",
            "internal_work_item.md",
            "request_for_correction.md",
            "starter_assignment_treatment.md",
        ],
        PULL_REQUEST_TEMPLATE=[
            "backend_components.md",
            "feature_proposals.md",
            "housekeeping.md",
            "interface_architecture.md",
            "internal_improvements.md",
            "localisation.md",
            "priority_patching.md",
            "project_policies.md",
            "structural_design.md",
            "user_experience.md",
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
        issue_templates=[
            "Internal Work Item.md",
            "Request for Correction.md",
            "Request for Improvement.md",
            "Request for Support.md",
            "Starter Assignment Treatment.md",
        ],
        merge_request_templates=[
            "Backend Components.md",
            "Feature Proposals.md",
            "Housekeeping.md",
            "Interface Architecture.md",
            "Internal Improvements.md",
            "Localisation.md",
            "Priority Patching.md",
            "Project Policies.md",
            "Structural Design.md",
            "User Experience.md",
        ],
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
    bulk_file_creation(
        github_directory,
        workflows=["docker.yml", "test.yml"],
        PULL_REQUEST_TEMPLATE=["interface_architecture.md", "user_experience.md"],
    )

    gitlab_directory = tmp_path / ".gitlab"
    bulk_file_creation(
        gitlab_directory,
        merge_request_templates=["Interface Architecture.md", "User Experience.md"],
    )

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
        features=[
            ".gitkeep",
            "root_command.feature",
            "launch_command.feature",
            "main_window.feature",
            "config_command.feature",
            "app_manager.feature",
            "manager_resolution.feature",
            "log_parser.feature",
        ],
        cli=[
            "test_root_command.py",
            "test_launch_command.py",
            "test_config_command.py",
        ],
        tui=["test_main_window.py"],
        config=["test_manager.py"],
        helpers=["tui_helpers.py"],
        utils=["parsers.py", "pytest_bdd_async.py"],
        logging=["test_regex_parser.py"],
    )

    cli_directory = tmp_path / package_name / "cli"
    bulk_file_creation(
        cli_directory,
        commands=["root_command.py", "launch.py"],
        styling=["themes.py"],
        helpers=["converter.py", "printer.py"],
    )

    commands_directory = cli_directory / "commands"
    bulk_file_creation(
        commands_directory, config=["extend.py", "get.py", "set.py", "unset.py"]
    )

    tui_directory = tmp_path / package_name / "tui"
    bulk_file_creation(
        tui_directory,
        "main_window.py",
        "themes.py",
        components=[".gitkeep"],
        css=["demo.tcss", "noctis.tcss"],
    )

    config_directory = tmp_path / package_name / "config"
    bulk_file_creation(config_directory, "constants.py", "helpers.py", "manager.py")

    logging_directory = tmp_path / package_name / "logging"
    bulk_file_creation(
        logging_directory, "formatters.py", "parsers.py", "text_tools.py"
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
            "commands": {
                "root": cli_directory / "commands",
                "root_command": cli_directory / "commands" / "root_command.py",
                "launch": cli_directory / "commands" / "launch.py",
                "config": {
                    "root": cli_directory / "commands" / "config",
                    "extend": cli_directory / "commands" / "config" / "extend.py",
                    "get": cli_directory / "commands" / "config" / "get.py",
                    "set": cli_directory / "commands" / "config" / "set.py",
                    "unset": cli_directory / "commands" / "config" / "unset.py",
                },
            },
            "helpers": {
                "root": cli_directory / "helpers",
                "converter": cli_directory / "helpers" / "converter.py",
                "printer": cli_directory / "helpers" / "printer.py",
            },
            "styling": {
                "root": cli_directory / "styling",
                "themes": cli_directory / "styling" / "themes.py",
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
        "config": {
            "root": config_directory,
            "constants": config_directory / "constants.py",
            "helpers": config_directory / "helpers.py",
            "manager": config_directory / "manager.py",
        },
        "logging": {
            "root": logging_directory,
            "formatters": logging_directory / "formatters.py",
            "parsers": logging_directory / "parsers.py",
            "tools": logging_directory / "text_tools.py",
        },
        "tests": {
            "root": tests_directory,
            "cli": {
                "root": tests_directory / "cli",
                "test": tests_directory / "cli" / "test_root_command.py",
                "launch": tests_directory / "cli" / "test_launch_command.py",
                "config": tests_directory / "cli" / "test_config_command.py",
            },
            "tui": {
                "root": tests_directory / "tui",
                "test": tests_directory / "tui" / "test_main_window.py",
            },
            "manager": {
                "root": tests_directory / "config",
                "test": tests_directory / "config" / "test_manager.py",
            },
            "logging": {
                "root": tests_directory / "logging",
                "test": tests_directory / "logging" / "test_regex_parser.py",
            },
            "conftest": tests_directory / "conftest.py",
            "gitkeep": tests_directory / ".gitkeep",
        },
        "bdd": {
            "root": tests_directory / "features",
            "cli": tests_directory / "features" / "root_command.feature",
            "launch": tests_directory / "features" / "launch_command.feature",
            "config": tests_directory / "features" / "config_command.feature",
            "tui": tests_directory / "features" / "main_window.feature",
            "manager": tests_directory / "features" / "app_manager.feature",
            "resolution": tests_directory / "features" / "manager_resolution.feature",
            "regex": tests_directory / "features" / "log_parser.feature",
            "gitkeep": tests_directory / "features" / ".gitkeep",
            "helpers": {
                "root": tests_directory / "helpers",
                "tui": tests_directory / "helpers" / "tui_helpers.py",
            },
            "utils": {
                "root": tests_directory / "utils",
                "async": tests_directory / "utils" / "pytest_bdd_async.py",
                "parsers": tests_directory / "utils" / "parsers.py",
            },
        },
        "github": {
            "root": tmp_path / ".github",
            "test_workflow": tmp_path / ".github" / "workflows" / "test.yml",
            "ux": tmp_path / ".github" / "PULL_REQUEST_TEMPLATE" / "user_experience.md",
            "arch": tmp_path
            / ".github"
            / "PULL_REQUEST_TEMPLATE"
            / "interface_architecture.md",
        },
        "gitlab": {
            "ci": tmp_path / ".gitlab-ci.yml",
            "triage": tmp_path / ".triage-policies.yml",
            "ux": tmp_path
            / ".gitlab"
            / "merge_request_templates"
            / "User Experience.md",
            "arch": tmp_path
            / ".gitlab"
            / "merge_request_templates"
            / "Interface Architecture.md",
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

        2) Initialize Poetry and install pre-commit hooks:

            $ invoke install

        3) Run the code checks for inconsistencies and issues:

            $ invoke sweep

        4) Upload initial code to GitLab:

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

        Install it first via your package manager or via pipx before running step 2.

            $ pipx install invoke
    """

    return galactipy_instructions + textwrap.dedent(extra_message)


@pytest.fixture
def galactipy_poetry_instructions(galactipy_instructions, rich_output):
    if rich_output is not None:
        extra_message = """
            WARNING! Poetry was not found in your system.

            Install it via your package manager or through one of the methods prescribed in their documentation.
        """  # noqa: E501

    else:
        extra_message = """
            WARNING! Poetry was not found in your system.

            Install it via your package manager or through one of the methods prescribed in their documentation:

                https://python-poetry.org/docs/#installation
        """  # noqa: E501

    return galactipy_instructions + textwrap.dedent(extra_message)
