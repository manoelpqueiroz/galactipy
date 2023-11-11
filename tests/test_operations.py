import pytest

from hooks.post_gen_project import (
    generate_licence,
    generate_templates,
    licences_dict,
    print_further_instructions,
    remove_unused_files,
)
from tests.test_helpers import bulk_file_creation

LICENCES_TO_CHECK = list(licences_dict.values())
LICENCES_TO_CHECK.remove(None)


class TestLicenceGeneration:
    @pytest.mark.parametrize("chosen_licence", LICENCES_TO_CHECK)
    def test_generate_licence(self, licence_tree, chosen_licence):
        project_root, licence_root, licence_file = licence_tree

        generate_licence(project_root, chosen_licence)

        assert licence_file.exists()
        assert not licence_root.exists()

    def test_non_oss_licence(self, licence_tree):
        project_root, licence_root, licence_file = licence_tree

        generate_licence(project_root, None)

        assert not licence_file.exists()
        assert not licence_root.exists()


class TestTemplateGeneration:
    @pytest.mark.parametrize("valid_scm", ["github", "gitlab"])
    def test_generate_valid_templates(self, template_tree, valid_scm):
        project_root, template_root = template_tree
        scm_template_directory = project_root / f".{valid_scm}"

        generate_templates(project_root, valid_scm)

        assert scm_template_directory.exists()
        assert not template_root.exists()

    @pytest.mark.parametrize("invalid_scm", ["bitbucket", "gitea", "azure"])
    def test_generate_invalid_templates(self, template_tree, invalid_scm):
        project_root, template_root = template_tree

        with pytest.raises(FileNotFoundError):
            generate_templates(project_root, invalid_scm)


class TestFileRemoval:
    def test_remove_cli(self, removal_tree):
        project_root, pyproject_file, tests_root, test_file, package_name = removal_tree
        cli_file = project_root / package_name / "__main__.py"

        remove_unused_files(project_root, package_name, True, False, False, False)

        assert not cli_file.exists()

        assert pyproject_file.exists()
        assert tests_root.exists()
        assert test_file.exists()

    def test_remove_gitlab(self, removal_tree):
        project_root, pyproject_file, tests_root, test_file, package_name = removal_tree
        ci_file = project_root / ".gitlab-ci.yml"

        remove_unused_files(project_root, package_name, False, True, False, False)

        assert not ci_file.exists()

        assert pyproject_file.exists()
        assert tests_root.exists()
        assert test_file.exists()

    def test_remove_docker(self, removal_tree):
        project_root, pyproject_file, tests_root, test_file, package_name = removal_tree
        docker_directory = project_root / "docker"
        dockerignore = project_root / ".dockerignore"

        remove_unused_files(project_root, package_name, False, False, True, False)

        assert not docker_directory.exists()
        assert not dockerignore.exists()

        assert pyproject_file.exists()
        assert tests_root.exists()
        assert test_file.exists()

    def test_remove_docs(self, removal_tree):
        project_root, pyproject_file, tests_root, test_file, package_name = removal_tree
        docs_directory = project_root / "docs"

        remove_unused_files(project_root, package_name, False, False, False, True)

        assert not docs_directory.exists()

        assert pyproject_file.exists()
        assert tests_root.exists()
        assert test_file.exists()

    def test_remove_all(self, removal_tree):
        project_root, pyproject_file, tests_root, test_file, package_name = removal_tree

        cli_file = project_root / package_name / "__main__.py"
        ci_file = project_root / ".gitlab-ci.yml"
        docker_directory = project_root / "docker"
        dockerignore = project_root / ".dockerignore"
        docs_directory = project_root / "docs"

        remove_unused_files(project_root, package_name, True, True, True, True)

        assert not cli_file.exists()
        assert not ci_file.exists()
        assert not docker_directory.exists()
        assert not dockerignore.exists()
        assert not docs_directory.exists()

        assert pyproject_file.exists()
        assert tests_root.exists()
        assert test_file.exists()


def test_print_further_instructions(capsys, galactipy_instructions):
    print_further_instructions(
        "Galactipy",
        "galactipy",
        "GitLab",
        "https://www.gitlab.com/manoelpqueiroz/galactipy",
    )
    captured = capsys.readouterr()

    # STDOUT always finishes with a newline, hence the addition on the right side
    assert captured.out == galactipy_instructions + "\n"
