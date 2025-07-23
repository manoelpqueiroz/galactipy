from hooks.post_gen_project import (
    ProjectFlags,
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
    def test_remove_gitlab(self, removal_tree):
        gitlab_files = removal_tree["gitlab"]
        ci_file = gitlab_files["ci"]
        triage_file = gitlab_files["triage"]

        config = ProjectFlags(True, False, False, False, "cli")

        remove_unused_files(removal_tree["root"], removal_tree["package_name"], config)

        assert not ci_file.exists()
        assert not triage_file.exists()

        assert removal_tree["github"]["test_workflow"].exists()
        assert removal_tree["docker"]["github_workflow"].exists()

        assert removal_tree["pyproject"].exists()
        assert removal_tree["tests"]["root"].exists()
        assert removal_tree["tests"]["conftest"].exists()
        assert removal_tree["bdd"]["cli"].exists()

    def test_remove_docker_gitlab(self, removal_tree):
        docker_files = removal_tree["docker"]
        docker_directory = docker_files["root"]
        dockerignore = docker_files["dockerignore"]

        config = ProjectFlags(False, True, False, False, "cli")

        remove_unused_files(removal_tree["root"], removal_tree["package_name"], config)

        assert not docker_directory.exists()
        assert not dockerignore.exists()

        assert removal_tree["pyproject"].exists()
        assert removal_tree["tests"]["root"].exists()
        assert removal_tree["tests"]["conftest"].exists()
        assert removal_tree["bdd"]["cli"].exists()

    def test_remove_docker_github(self, removal_tree):
        docker_files = removal_tree["docker"]
        docker_directory = docker_files["root"]
        dockerignore = docker_files["dockerignore"]
        docker_workflow = docker_files["github_workflow"]

        config = ProjectFlags(True, True, False, False, "cli")

        remove_unused_files(removal_tree["root"], removal_tree["package_name"], config)

        assert not docker_directory.exists()
        assert not dockerignore.exists()
        assert not docker_workflow.exists()

        assert removal_tree["pyproject"].exists()
        assert removal_tree["tests"]["root"].exists()
        assert removal_tree["tests"]["conftest"].exists()
        assert removal_tree["bdd"]["cli"].exists()
        assert removal_tree["github"]["test_workflow"].exists()

    def test_tui_with_bdd(self, removal_tree):
        cli_files = removal_tree["cli"]
        tui_files = removal_tree["tui"]
        bdd_files = removal_tree["bdd"]
        test_files = removal_tree["tests"]

        config = ProjectFlags(False, False, False, False, "tui")

        remove_unused_files(removal_tree["root"], removal_tree["package_name"], config)

        assert tui_files["main_window"].exists()
        assert tui_files["components"]["gitkeep"].exists()
        assert tui_files["css"]["demo"].exists()

        assert cli_files["root_command"].exists()
        assert not cli_files["commands"]["launch"].exists()
        assert cli_files["commands"]["gitkeep"].exists()
        assert cli_files["main"].exists()

        assert test_files["root"].exists()
        assert test_files["tui"]["test"].exists()
        assert test_files["cli"]["test"].exists()
        assert test_files["conftest"].exists()
        assert not test_files["gitkeep"].exists()

        assert bdd_files["tui"].exists()
        assert bdd_files["cli"].exists()
        assert not bdd_files["gitkeep"].exists()
        assert bdd_files["helpers"]["tui"].exists()
        assert bdd_files["utils"]["bdd"].exists()

    def test_tui_no_bdd(self, removal_tree):
        cli_files = removal_tree["cli"]
        tui_files = removal_tree["tui"]
        bdd_files = removal_tree["bdd"]
        test_files = removal_tree["tests"]

        config = ProjectFlags(False, False, True, False, "tui")

        remove_unused_files(removal_tree["root"], removal_tree["package_name"], config)

        assert tui_files["main_window"].exists()
        assert tui_files["components"]["gitkeep"].exists()
        assert tui_files["css"]["demo"].exists()

        assert cli_files["root_command"].exists()
        assert not cli_files["commands"]["launch"].exists()
        assert cli_files["commands"]["gitkeep"].exists()
        assert cli_files["main"].exists()

        assert test_files["tui"]["test"].exists()
        assert test_files["cli"]["test"].exists()
        assert test_files["conftest"].exists()
        assert not test_files["gitkeep"].exists()

        assert not bdd_files["root"].exists()
        assert not bdd_files["helpers"]["root"].exists()
        assert not bdd_files["utils"]["root"].exists()

    def test_hybrid_with_bdd(self, removal_tree):
        cli_files = removal_tree["cli"]
        tui_files = removal_tree["tui"]
        bdd_files = removal_tree["bdd"]
        test_files = removal_tree["tests"]

        config = ProjectFlags(False, False, False, False, "hybrid")

        remove_unused_files(removal_tree["root"], removal_tree["package_name"], config)

        assert tui_files["main_window"].exists()
        assert tui_files["components"]["gitkeep"].exists()
        assert tui_files["css"]["demo"].exists()

        assert cli_files["root_command"].exists()
        assert cli_files["commands"]["root"].exists()
        assert cli_files["commands"]["launch"].exists()
        assert not cli_files["commands"]["gitkeep"].exists()
        assert cli_files["main"].exists()

        assert test_files["tui"]["test"].exists()
        assert test_files["cli"]["test"].exists()
        assert test_files["conftest"].exists()
        assert not test_files["gitkeep"].exists()

        assert bdd_files["tui"].exists()
        assert bdd_files["cli"].exists()
        assert not bdd_files["gitkeep"].exists()
        assert bdd_files["helpers"]["tui"].exists()
        assert bdd_files["utils"]["bdd"].exists()

    def test_hybrid_no_bdd(self, removal_tree):
        cli_files = removal_tree["cli"]
        tui_files = removal_tree["tui"]
        bdd_files = removal_tree["bdd"]
        test_files = removal_tree["tests"]

        config = ProjectFlags(False, False, True, False, "hybrid")

        remove_unused_files(removal_tree["root"], removal_tree["package_name"], config)

        assert tui_files["main_window"].exists()
        assert tui_files["components"]["gitkeep"].exists()
        assert tui_files["css"]["demo"].exists()

        assert cli_files["root_command"].exists()
        assert cli_files["commands"]["launch"].exists()
        assert not cli_files["commands"]["gitkeep"].exists()
        assert cli_files["main"].exists()

        assert test_files["tui"]["test"].exists()
        assert test_files["cli"]["test"].exists()
        assert test_files["conftest"].exists()
        assert not test_files["gitkeep"].exists()

        assert not bdd_files["root"].exists()
        assert not bdd_files["helpers"]["root"].exists()
        assert not bdd_files["utils"]["root"].exists()

    def test_cli_with_bdd(self, removal_tree):
        cli_files = removal_tree["cli"]
        tui_files = removal_tree["tui"]
        bdd_files = removal_tree["bdd"]
        test_files = removal_tree["tests"]

        config = ProjectFlags(False, False, False, False, "cli")

        remove_unused_files(removal_tree["root"], removal_tree["package_name"], config)

        assert not tui_files["root"].exists()

        assert cli_files["root_command"].exists()
        assert not cli_files["commands"]["launch"].exists()
        assert cli_files["commands"]["gitkeep"].exists()
        assert cli_files["main"].exists()

        assert not test_files["tui"]["root"].exists()
        assert test_files["cli"]["test"].exists()
        assert test_files["conftest"].exists()
        assert not test_files["gitkeep"].exists()

        assert not bdd_files["tui"].exists()
        assert bdd_files["cli"].exists()
        assert not bdd_files["gitkeep"].exists()
        assert not bdd_files["helpers"]["root"].exists()
        assert not bdd_files["utils"]["root"].exists()

    def test_cli_no_bdd(self, removal_tree):
        cli_files = removal_tree["cli"]
        tui_files = removal_tree["tui"]
        bdd_files = removal_tree["bdd"]
        test_files = removal_tree["tests"]

        config = ProjectFlags(False, False, True, False, "cli")

        remove_unused_files(removal_tree["root"], removal_tree["package_name"], config)

        assert not tui_files["root"].exists()

        assert cli_files["root_command"].exists()
        assert not cli_files["commands"]["launch"].exists()
        assert cli_files["commands"]["gitkeep"].exists()
        assert cli_files["main"].exists()

        assert not test_files["tui"]["root"].exists()
        assert test_files["cli"]["test"].exists()
        assert test_files["conftest"].exists()
        assert not test_files["gitkeep"].exists()

        assert not bdd_files["root"].exists()
        assert not bdd_files["helpers"]["root"].exists()
        assert not bdd_files["utils"]["root"].exists()

    def test_bare_with_bdd(self, removal_tree):
        cli_files = removal_tree["cli"]
        tui_files = removal_tree["tui"]
        bdd_files = removal_tree["bdd"]
        test_files = removal_tree["tests"]

        config = ProjectFlags(False, False, False, False, "bare_repo")

        remove_unused_files(removal_tree["root"], removal_tree["package_name"], config)

        assert not tui_files["root"].exists()

        assert not cli_files["root"].exists()
        assert not cli_files["main"].exists()

        assert test_files["root"].exists()
        assert not test_files["tui"]["root"].exists()
        assert not test_files["cli"]["root"].exists()
        assert not test_files["conftest"].exists()
        assert test_files["gitkeep"].exists()

        assert bdd_files["root"].exists()
        assert not bdd_files["tui"].exists()
        assert not bdd_files["cli"].exists()
        assert bdd_files["gitkeep"].exists()
        assert not bdd_files["helpers"]["root"].exists()
        assert not bdd_files["utils"]["root"].exists()

    def test_bare_no_bdd(self, removal_tree):
        cli_files = removal_tree["cli"]
        tui_files = removal_tree["tui"]
        bdd_files = removal_tree["bdd"]
        test_files = removal_tree["tests"]

        config = ProjectFlags(False, False, True, False, "bare_repo")

        remove_unused_files(removal_tree["root"], removal_tree["package_name"], config)

        assert not tui_files["root"].exists()

        assert not cli_files["root"].exists()
        assert not cli_files["main"].exists()

        assert test_files["root"].exists()
        assert not test_files["tui"]["root"].exists()
        assert not test_files["cli"]["root"].exists()
        assert not test_files["conftest"].exists()
        assert test_files["gitkeep"].exists()

        assert not bdd_files["root"].exists()
        assert not bdd_files["helpers"]["root"].exists()
        assert not bdd_files["utils"]["root"].exists()

    def test_remove_feature_files(self, removal_tree):
        feature_files = removal_tree["features"]

        file1 = feature_files["file1"]
        file2 = feature_files["file2"]
        directory = feature_files["directory"]

        config = ProjectFlags(False, False, False, True, "cli")

        remove_unused_files(removal_tree["root"], removal_tree["package_name"], config)

        assert not file1.exists()
        assert not file2.exists()
        assert not directory.exists()

        assert removal_tree["bdd"]["cli"].exists()
        assert removal_tree["docker"]["dockerfile"].exists()
        assert removal_tree["docker"]["readme"].exists()

        assert removal_tree["pyproject"].exists()
        assert removal_tree["tests"]["root"].exists()
        assert removal_tree["tests"]["conftest"].exists()

    def test_keep_feature_files(self, removal_tree):
        feature_files = removal_tree["features"]

        file1 = feature_files["file1"]
        file2 = feature_files["file2"]
        sample1 = feature_files["sample1"]
        sample2 = feature_files["sample2"]
        sample3 = feature_files["sample3"]

        config = ProjectFlags(False, False, False, False, "cli")

        remove_unused_files(removal_tree["root"], removal_tree["package_name"], config)

        assert file1.exists()
        assert file2.exists()
        assert sample1.exists()
        assert sample2.exists()
        assert sample3.exists()

        assert removal_tree["bdd"]["cli"].exists()
        assert removal_tree["docker"]["dockerfile"].exists()
        assert removal_tree["docker"]["readme"].exists()

        assert removal_tree["pyproject"].exists()
        assert removal_tree["tests"]["root"].exists()
        assert removal_tree["tests"]["conftest"].exists()

    def test_remove_all(self, removal_tree):
        pyproject = removal_tree["pyproject"]

        cli_root = removal_tree["cli"]["root"]
        tui_root = removal_tree["tui"]["root"]

        bdd_root = removal_tree["bdd"]["root"]
        helpers_root = removal_tree["bdd"]["helpers"]["root"]
        utils_root = removal_tree["bdd"]["utils"]["root"]

        tests_cli_root = removal_tree["tests"]["cli"]["root"]
        tests_tui_root = removal_tree["tests"]["tui"]["root"]
        test_gitkeep = removal_tree["tests"]["gitkeep"]

        ci_file = removal_tree["gitlab"]["ci"]
        triage_file = removal_tree["gitlab"]["triage"]

        docker_directory = removal_tree["docker"]["root"]
        dockerignore = removal_tree["docker"]["dockerignore"]

        file1 = removal_tree["features"]["file1"]
        file2 = removal_tree["features"]["file2"]
        directory = removal_tree["features"]["directory"]

        config = ProjectFlags(True, True, True, True, "bare_repo")

        remove_unused_files(removal_tree["root"], removal_tree["package_name"], config)

        assert not cli_root.exists()
        assert not tui_root.exists()
        assert not tests_cli_root.exists()
        assert not tests_tui_root.exists()

        assert not ci_file.exists()
        assert not triage_file.exists()

        assert not docker_directory.exists()
        assert not dockerignore.exists()

        assert not bdd_root.exists()
        assert not helpers_root.exists()
        assert not utils_root.exists()

        assert not file1.exists()
        assert not file2.exists()
        assert not directory.exists()

        assert pyproject.exists()
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
