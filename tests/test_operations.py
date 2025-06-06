from hooks.post_gen_project import (
    generate_licence,
    generate_templates,
    licences_dict,
    print_further_instructions,
    remove_unused_files,
)

import pytest

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
        (
            project_root,
            pyproject_file,
            tests_root,
            test_file,
            feature_file,
            package_name,
        ) = removal_tree
        cli_root = project_root / package_name / "cli"
        main_file = project_root / package_name / "__main__.py"
        conftest_file = tests_root / "conftest.py"
        test_gitkeep = tests_root / ".gitkeep"

        remove_unused_files(project_root, package_name, True, False, False, False)

        assert not cli_root.exists()
        assert not main_file.exists()
        assert not test_file.exists()
        assert not conftest_file.exists()
        assert not feature_file.exists()

        assert pyproject_file.exists()
        assert tests_root.exists()
        assert test_gitkeep.exists()

    def test_remove_gitlab(self, removal_tree):
        (
            project_root,
            pyproject_file,
            tests_root,
            test_file,
            feature_file,
            package_name,
        ) = removal_tree
        ci_file = project_root / ".gitlab-ci.yml"
        triage_file = project_root / ".triage-policies.yml"

        remove_unused_files(project_root, package_name, False, True, False, False)

        assert not ci_file.exists()
        assert not triage_file.exists()

        assert pyproject_file.exists()
        assert tests_root.exists()
        assert test_file.exists()
        assert feature_file.exists()

    def test_remove_docker_gitlab(self, removal_tree):
        (
            project_root,
            pyproject_file,
            tests_root,
            test_file,
            feature_file,
            package_name,
        ) = removal_tree
        docker_directory = project_root / "docker"
        dockerignore = project_root / ".dockerignore"

        remove_unused_files(project_root, package_name, False, False, True, False)

        assert not docker_directory.exists()
        assert not dockerignore.exists()

        assert pyproject_file.exists()
        assert tests_root.exists()
        assert test_file.exists()
        assert feature_file.exists()

    def test_remove_docker_github(self, removal_tree):
        (
            project_root,
            pyproject_file,
            tests_root,
            test_file,
            feature_file,
            package_name,
        ) = removal_tree
        docker_directory = project_root / "docker"
        dockerignore = project_root / ".dockerignore"
        docker_workflow = project_root / ".github" / "workflows" / "docker.yml"
        test_workflow = project_root / ".github" / "workflows" / "test.yml"

        remove_unused_files(project_root, package_name, False, True, True, False)

        assert not docker_directory.exists()
        assert not dockerignore.exists()
        assert not docker_workflow.exists()

        assert pyproject_file.exists()
        assert tests_root.exists()
        assert test_file.exists()
        assert feature_file.exists()
        assert test_workflow.exists()

    def test_remove_bdd_keep_cli(self, removal_tree):
        (
            project_root,
            pyproject_file,
            tests_root,
            test_file,
            feature_file,
            package_name,
        ) = removal_tree
        cli_root = project_root / package_name / "cli"
        main_file = project_root / package_name / "__main__.py"
        conftest_file = tests_root / "conftest.py"
        test_gitkeep = tests_root / ".gitkeep"
        features_gitkeep = tests_root / "features" / ".gitkeep"

        remove_unused_files(project_root, package_name, False, False, False, True)

        assert not feature_file.exists()
        assert not test_gitkeep.exists()
        assert not features_gitkeep.exists()

        assert pyproject_file.exists()

        assert cli_root.exists()
        assert main_file.exists()

        assert tests_root.exists()
        assert test_file.exists()
        assert conftest_file.exists()

    def test_remove_bdd_and_cli(self, removal_tree):
        (
            project_root,
            pyproject_file,
            tests_root,
            test_file,
            feature_file,
            package_name,
        ) = removal_tree
        cli_root = project_root / package_name / "cli"
        main_file = project_root / package_name / "__main__.py"
        conftest_file = tests_root / "conftest.py"
        test_gitkeep = tests_root / ".gitkeep"
        features_gitkeep = tests_root / "features" / ".gitkeep"

        remove_unused_files(project_root, package_name, True, False, False, True)

        assert not cli_root.exists()
        assert not main_file.exists()
        assert not test_file.exists()
        assert not conftest_file.exists()

        assert not feature_file.exists()
        assert not features_gitkeep.exists()

        assert pyproject_file.exists()
        assert tests_root.exists()
        assert test_gitkeep.exists()

    def test_keep_bdd_and_cli(self, removal_tree):
        (
            project_root,
            pyproject_file,
            tests_root,
            test_file,
            feature_file,
            package_name,
        ) = removal_tree
        cli_command = project_root / package_name / "cli" / "root_command.py"
        main_file = project_root / package_name / "__main__.py"
        conftest_file = tests_root / "conftest.py"
        test_gitkeep = tests_root / ".gitkeep"
        features_gitkeep = tests_root / "features" / ".gitkeep"

        remove_unused_files(project_root, package_name, False, False, False, False)

        assert not test_gitkeep.exists()
        assert not features_gitkeep.exists()

        assert cli_command.exists()
        assert main_file.exists()
        assert test_file.exists()
        assert conftest_file.exists()
        assert feature_file.exists()

        assert pyproject_file.exists()

    def test_remove_all(self, removal_tree):
        (
            project_root,
            pyproject_file,
            tests_root,
            test_file,
            feature_file,
            package_name,
        ) = removal_tree

        cli_root = project_root / package_name / "cli"
        cli_file = project_root / package_name / "__main__.py"
        ci_file = project_root / ".gitlab-ci.yml"
        docker_directory = project_root / "docker"
        dockerignore = project_root / ".dockerignore"
        test_gitkeep = tests_root / ".gitkeep"
        features_gitkeep = project_root / "tests" / "features" / ".gitkeep"

        remove_unused_files(project_root, package_name, True, True, True, True)

        assert not cli_root.exists()
        assert not cli_file.exists()
        assert not ci_file.exists()
        assert not docker_directory.exists()
        assert not dockerignore.exists()
        assert not test_file.exists()
        assert not feature_file.exists()
        assert not features_gitkeep.exists()

        assert pyproject_file.exists()
        assert tests_root.exists()
        assert test_gitkeep.exists()


class TestInstructions:
    @pytest.mark.parametrize("rich_output", [True, None])
    def test_print_further_instructions(
        self, capsys, mocker, rich_output, galactipy_instructions
    ):
        mocker.patch(
            "hooks.post_gen_project.find_spec", side_effect=[rich_output, True]
        )

        print_further_instructions(
            "Galactipy",
            "galactipy",
            "GitLab",
            "https://www.gitlab.com/galactipy/galactipy",
        )
        captured = capsys.readouterr()

        # STDOUT always finishes with a newline
        assert captured.out == galactipy_instructions + "\n"

    @pytest.mark.parametrize("rich_output", [True, None])
    def test_print_invoke_instructions(
        self, capsys, mocker, rich_output, galactipy_invoke_instructions
    ):
        mocker.patch(
            "hooks.post_gen_project.find_spec", side_effect=[rich_output, None]
        )

        print_further_instructions(
            "Galactipy",
            "galactipy",
            "GitLab",
            "https://www.gitlab.com/galactipy/galactipy",
        )
        captured = capsys.readouterr()

        # STDOUT always finishes with a newline
        assert captured.out == galactipy_invoke_instructions + "\n"
