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
        project_root, licence_root, licence_file, header_root, header_file = (
            licence_tree
        )
        cc_file = project_root / "CODE_OF_CONDUCT.md"

        generate_licence(project_root, chosen_licence)

        assert licence_file.exists()
        assert not licence_root.exists()

        assert header_file.exists()
        assert not header_root.exists()

        assert cc_file.exists()

    def test_non_oss_licence(self, licence_tree):
        project_root, licence_root, licence_file, header_root, header_file = (
            licence_tree
        )
        cc_file = project_root / "CODE_OF_CONDUCT.md"

        generate_licence(project_root, None)

        assert not licence_file.exists()
        assert not licence_root.exists()

        assert not header_file.exists()
        assert not header_root.exists()

        assert not cc_file.exists()


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
        project_root, _ = template_tree

        with pytest.raises(FileNotFoundError):
            generate_templates(project_root, invalid_scm)


class TestServiceRemovals:
    def test_remove_gitlab(self, removal_tree):
        gitlab_files = removal_tree["gitlab"]
        ci_file = gitlab_files["ci"]
        triage_file = gitlab_files["triage"]
        renovate_file = gitlab_files["renovate"]

        config = ProjectFlags(True, False, False, False, True, "semver", "cli")

        remove_unused_files(removal_tree["root"], removal_tree["package_name"], config)

        assert not ci_file.exists()
        assert not triage_file.exists()
        assert not renovate_file.exists()

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
        components_directory = docker_files["gitlab_components"]

        config = ProjectFlags(False, True, False, False, True, "semver", "cli")

        remove_unused_files(removal_tree["root"], removal_tree["package_name"], config)

        assert not docker_directory.exists()
        assert not dockerignore.exists()
        assert not components_directory.exists()

        assert removal_tree["pyproject"].exists()
        assert removal_tree["tests"]["root"].exists()
        assert removal_tree["tests"]["conftest"].exists()
        assert removal_tree["bdd"]["cli"].exists()

    def test_remove_docker_github(self, removal_tree):
        docker_files = removal_tree["docker"]
        docker_directory = docker_files["root"]
        dockerignore = docker_files["dockerignore"]
        docker_workflow = docker_files["github_workflow"]

        config = ProjectFlags(True, True, False, False, True, "semver", "cli")

        remove_unused_files(removal_tree["root"], removal_tree["package_name"], config)

        assert not docker_directory.exists()
        assert not dockerignore.exists()
        assert not docker_workflow.exists()

        assert removal_tree["pyproject"].exists()
        assert removal_tree["tests"]["root"].exists()
        assert removal_tree["tests"]["conftest"].exists()
        assert removal_tree["bdd"]["cli"].exists()
        assert removal_tree["github"]["test_workflow"].exists()


class TestApplicationOptions:
    def test_tui_with_bdd(self, removal_tree):
        cli_files = removal_tree["cli"]

        config_command_files = cli_files["commands"]["config"]
        helper_files = cli_files["helpers"]
        styling_files = cli_files["styling"]

        tui_files = removal_tree["tui"]
        bdd_files = removal_tree["bdd"]
        test_files = removal_tree["tests"]
        config_files = removal_tree["config"]
        logging_files = removal_tree["logging"]

        config = ProjectFlags(False, False, False, False, True, "semver", "tui")

        remove_unused_files(removal_tree["root"], removal_tree["package_name"], config)

        assert tui_files["main_window"].exists()
        assert tui_files["themes"].exists()
        assert tui_files["components"]["gitkeep"].exists()
        assert tui_files["css"]["demo"].exists()
        assert tui_files["css"]["noctis"].exists()

        assert cli_files["commands"]["root_command"].exists()
        assert not cli_files["commands"]["launch"].exists()
        assert cli_files["main"].exists()

        assert config_command_files["get"].exists()
        assert config_command_files["set"].exists()
        assert config_command_files["extend"].exists()
        assert config_command_files["unset"].exists()

        assert helper_files["converter"].exists()
        assert helper_files["printer"].exists()

        assert styling_files["themes"].exists()

        assert config_files["constants"].exists()
        assert config_files["helpers"].exists()
        assert config_files["manager"].exists()

        assert logging_files["formatters"].exists()
        assert logging_files["parsers"].exists()
        assert logging_files["tools"].exists()

        assert test_files["root"].exists()
        assert test_files["tui"]["test"].exists()
        assert test_files["cli"]["test"].exists()
        assert not test_files["cli"]["launch"].exists()
        assert test_files["cli"]["config"].exists()
        assert test_files["manager"]["test"].exists()
        assert test_files["logging"]["test"].exists()
        assert test_files["conftest"].exists()
        assert not test_files["gitkeep"].exists()

        assert bdd_files["tui"].exists()
        assert bdd_files["cli"].exists()
        assert not bdd_files["launch"].exists()
        assert bdd_files["config"].exists()
        assert bdd_files["manager"].exists()
        assert bdd_files["resolution"].exists()
        assert bdd_files["regex"].exists()
        assert bdd_files["helpers"]["tui"].exists()
        assert bdd_files["utils"]["async"].exists()
        assert bdd_files["utils"]["parsers"].exists()
        assert not bdd_files["gitkeep"].exists()

        assert removal_tree["gitlab"]["ux"].exists()
        assert removal_tree["gitlab"]["arch"].exists()

    def test_tui_no_bdd(self, removal_tree):
        cli_files = removal_tree["cli"]

        config_command_files = cli_files["commands"]["config"]
        helper_files = cli_files["helpers"]
        styling_files = cli_files["styling"]

        tui_files = removal_tree["tui"]
        bdd_files = removal_tree["bdd"]
        test_files = removal_tree["tests"]
        config_files = removal_tree["config"]
        logging_files = removal_tree["logging"]

        config = ProjectFlags(False, False, True, False, True, "semver", "tui")

        remove_unused_files(removal_tree["root"], removal_tree["package_name"], config)

        assert tui_files["main_window"].exists()
        assert tui_files["themes"].exists()
        assert tui_files["components"]["gitkeep"].exists()
        assert tui_files["css"]["demo"].exists()
        assert tui_files["css"]["noctis"].exists()

        assert cli_files["commands"]["root_command"].exists()
        assert not cli_files["commands"]["launch"].exists()
        assert cli_files["main"].exists()

        assert config_command_files["get"].exists()
        assert config_command_files["set"].exists()
        assert config_command_files["extend"].exists()
        assert config_command_files["unset"].exists()

        assert helper_files["converter"].exists()
        assert helper_files["printer"].exists()

        assert styling_files["themes"].exists()

        assert config_files["constants"].exists()
        assert config_files["helpers"].exists()
        assert config_files["manager"].exists()

        assert logging_files["formatters"].exists()
        assert logging_files["parsers"].exists()
        assert logging_files["tools"].exists()

        assert test_files["tui"]["test"].exists()
        assert test_files["cli"]["test"].exists()
        assert not test_files["cli"]["launch"].exists()
        assert test_files["cli"]["config"].exists()
        assert test_files["manager"]["test"].exists()
        assert test_files["logging"]["test"].exists()
        assert test_files["conftest"].exists()
        assert not test_files["gitkeep"].exists()

        assert not bdd_files["root"].exists()
        assert not bdd_files["helpers"]["root"].exists()
        assert not bdd_files["utils"]["root"].exists()

        assert removal_tree["gitlab"]["ux"].exists()
        assert removal_tree["gitlab"]["arch"].exists()

    def test_hybrid_with_bdd(self, removal_tree):
        cli_files = removal_tree["cli"]

        config_command_files = cli_files["commands"]["config"]
        helper_files = cli_files["helpers"]
        styling_files = cli_files["styling"]

        tui_files = removal_tree["tui"]
        bdd_files = removal_tree["bdd"]
        test_files = removal_tree["tests"]
        config_files = removal_tree["config"]
        logging_files = removal_tree["logging"]

        config = ProjectFlags(False, False, False, False, True, "semver", "hybrid")

        remove_unused_files(removal_tree["root"], removal_tree["package_name"], config)

        assert tui_files["main_window"].exists()
        assert tui_files["themes"].exists()
        assert tui_files["components"]["gitkeep"].exists()
        assert tui_files["css"]["demo"].exists()
        assert tui_files["css"]["noctis"].exists()

        assert cli_files["commands"]["root_command"].exists()
        assert cli_files["commands"]["root"].exists()
        assert cli_files["commands"]["launch"].exists()
        assert cli_files["main"].exists()

        assert config_command_files["get"].exists()
        assert config_command_files["set"].exists()
        assert config_command_files["extend"].exists()
        assert config_command_files["unset"].exists()

        assert helper_files["converter"].exists()
        assert helper_files["printer"].exists()

        assert styling_files["themes"].exists()

        assert config_files["constants"].exists()
        assert config_files["helpers"].exists()
        assert config_files["manager"].exists()

        assert logging_files["formatters"].exists()
        assert logging_files["parsers"].exists()
        assert logging_files["tools"].exists()

        assert test_files["tui"]["test"].exists()
        assert test_files["cli"]["test"].exists()
        assert test_files["cli"]["launch"].exists()
        assert test_files["cli"]["config"].exists()
        assert test_files["manager"]["test"].exists()
        assert test_files["logging"]["test"].exists()
        assert test_files["conftest"].exists()
        assert not test_files["gitkeep"].exists()

        assert bdd_files["tui"].exists()
        assert bdd_files["cli"].exists()
        assert bdd_files["launch"].exists()
        assert bdd_files["config"].exists()
        assert bdd_files["manager"].exists()
        assert bdd_files["resolution"].exists()
        assert bdd_files["regex"].exists()
        assert bdd_files["helpers"]["tui"].exists()
        assert bdd_files["utils"]["async"].exists()
        assert bdd_files["utils"]["parsers"].exists()
        assert not bdd_files["gitkeep"].exists()

        assert removal_tree["gitlab"]["ux"].exists()
        assert removal_tree["gitlab"]["arch"].exists()

    def test_hybrid_no_bdd(self, removal_tree):
        cli_files = removal_tree["cli"]

        config_command_files = cli_files["commands"]["config"]
        helper_files = cli_files["helpers"]
        styling_files = cli_files["styling"]

        tui_files = removal_tree["tui"]
        bdd_files = removal_tree["bdd"]
        test_files = removal_tree["tests"]
        config_files = removal_tree["config"]
        logging_files = removal_tree["logging"]

        config = ProjectFlags(False, False, True, False, True, "semver", "hybrid")

        remove_unused_files(removal_tree["root"], removal_tree["package_name"], config)

        assert tui_files["main_window"].exists()
        assert tui_files["themes"].exists()
        assert tui_files["components"]["gitkeep"].exists()
        assert tui_files["css"]["demo"].exists()
        assert tui_files["css"]["noctis"].exists()

        assert cli_files["commands"]["root_command"].exists()
        assert cli_files["commands"]["launch"].exists()
        assert cli_files["main"].exists()

        assert config_command_files["get"].exists()
        assert config_command_files["set"].exists()
        assert config_command_files["extend"].exists()
        assert config_command_files["unset"].exists()

        assert helper_files["converter"].exists()
        assert helper_files["printer"].exists()

        assert styling_files["themes"].exists()

        assert config_files["constants"].exists()
        assert config_files["helpers"].exists()
        assert config_files["manager"].exists()

        assert logging_files["formatters"].exists()
        assert logging_files["parsers"].exists()
        assert logging_files["tools"].exists()

        assert test_files["tui"]["test"].exists()
        assert test_files["cli"]["test"].exists()
        assert test_files["cli"]["launch"].exists()
        assert test_files["cli"]["config"].exists()
        assert test_files["manager"]["test"].exists()
        assert test_files["logging"]["test"].exists()
        assert test_files["conftest"].exists()
        assert not test_files["gitkeep"].exists()

        assert not bdd_files["root"].exists()
        assert not bdd_files["helpers"]["root"].exists()
        assert not bdd_files["utils"]["root"].exists()

        assert removal_tree["gitlab"]["ux"].exists()
        assert removal_tree["gitlab"]["arch"].exists()

    def test_cli_with_bdd(self, removal_tree):
        cli_files = removal_tree["cli"]

        config_command_files = cli_files["commands"]["config"]
        helper_files = cli_files["helpers"]
        styling_files = cli_files["styling"]

        tui_files = removal_tree["tui"]
        bdd_files = removal_tree["bdd"]
        test_files = removal_tree["tests"]
        config_files = removal_tree["config"]
        logging_files = removal_tree["logging"]

        config = ProjectFlags(False, False, False, False, True, "semver", "cli")

        remove_unused_files(removal_tree["root"], removal_tree["package_name"], config)

        assert not tui_files["root"].exists()

        assert cli_files["commands"]["root_command"].exists()
        assert not cli_files["commands"]["launch"].exists()
        assert cli_files["main"].exists()

        assert config_files["constants"].exists()
        assert config_files["helpers"].exists()
        assert config_files["manager"].exists()

        assert logging_files["formatters"].exists()
        assert logging_files["parsers"].exists()
        assert logging_files["tools"].exists()

        assert config_command_files["get"].exists()
        assert config_command_files["set"].exists()
        assert config_command_files["extend"].exists()
        assert config_command_files["unset"].exists()

        assert helper_files["converter"].exists()
        assert helper_files["printer"].exists()

        assert styling_files["themes"].exists()

        assert not test_files["tui"]["root"].exists()
        assert test_files["cli"]["test"].exists()
        assert not test_files["cli"]["launch"].exists()
        assert test_files["cli"]["config"].exists()
        assert test_files["manager"]["test"].exists()
        assert test_files["logging"]["test"].exists()
        assert test_files["conftest"].exists()
        assert not test_files["gitkeep"].exists()

        assert not bdd_files["tui"].exists()
        assert bdd_files["cli"].exists()
        assert not bdd_files["launch"].exists()
        assert bdd_files["config"].exists()
        assert bdd_files["manager"].exists()
        assert bdd_files["resolution"].exists()
        assert bdd_files["regex"].exists()
        assert not bdd_files["gitkeep"].exists()
        assert not bdd_files["helpers"]["root"].exists()

        assert bdd_files["utils"]["root"].exists()
        assert bdd_files["utils"]["parsers"].exists()
        assert not bdd_files["utils"]["async"].exists()

        assert removal_tree["gitlab"]["ux"].exists()
        assert removal_tree["gitlab"]["arch"].exists()

    def test_cli_no_bdd(self, removal_tree):
        cli_files = removal_tree["cli"]

        config_command_files = cli_files["commands"]["config"]
        helper_files = cli_files["helpers"]
        styling_files = cli_files["styling"]

        tui_files = removal_tree["tui"]
        bdd_files = removal_tree["bdd"]
        test_files = removal_tree["tests"]
        config_files = removal_tree["config"]
        logging_files = removal_tree["logging"]

        config = ProjectFlags(False, False, True, False, True, "semver", "cli")

        remove_unused_files(removal_tree["root"], removal_tree["package_name"], config)

        assert not tui_files["root"].exists()

        assert cli_files["commands"]["root_command"].exists()
        assert not cli_files["commands"]["launch"].exists()
        assert cli_files["main"].exists()

        assert config_files["constants"].exists()
        assert config_files["helpers"].exists()
        assert config_files["manager"].exists()

        assert logging_files["formatters"].exists()
        assert logging_files["parsers"].exists()
        assert logging_files["tools"].exists()

        assert config_command_files["get"].exists()
        assert config_command_files["set"].exists()
        assert config_command_files["extend"].exists()
        assert config_command_files["unset"].exists()

        assert helper_files["converter"].exists()
        assert helper_files["printer"].exists()

        assert styling_files["themes"].exists()

        assert not test_files["tui"]["root"].exists()
        assert test_files["cli"]["test"].exists()
        assert not test_files["cli"]["launch"].exists()
        assert test_files["cli"]["config"].exists()
        assert test_files["manager"]["test"].exists()
        assert test_files["logging"]["test"].exists()
        assert test_files["conftest"].exists()
        assert not test_files["gitkeep"].exists()

        assert not bdd_files["root"].exists()
        assert not bdd_files["helpers"]["root"].exists()
        assert not bdd_files["utils"]["root"].exists()

        assert removal_tree["gitlab"]["ux"].exists()
        assert removal_tree["gitlab"]["arch"].exists()

    def test_bare_cli_with_bdd(self, removal_tree):
        cli_files = removal_tree["cli"]

        command_files = cli_files["commands"]
        helper_files = cli_files["helpers"]
        styling_files = cli_files["styling"]

        tui_files = removal_tree["tui"]
        bdd_files = removal_tree["bdd"]
        test_files = removal_tree["tests"]
        config_files = removal_tree["config"]
        logging_files = removal_tree["logging"]

        config = ProjectFlags(False, False, False, False, True, "semver", "bare_cli")

        remove_unused_files(removal_tree["root"], removal_tree["package_name"], config)

        assert not tui_files["root"].exists()

        assert cli_files["main"].exists()
        assert command_files["root_command"].exists()
        assert not command_files["launch"].exists()
        assert not command_files["config"]["root"].exists()

        assert not config_files["root"].exists()

        assert logging_files["formatters"].exists()
        assert logging_files["parsers"].exists()
        assert logging_files["tools"].exists()

        assert helper_files["converter"].exists()
        assert not helper_files["printer"].exists()

        assert styling_files["themes"].exists()

        assert not test_files["tui"]["root"].exists()
        assert test_files["cli"]["test"].exists()
        assert not test_files["cli"]["launch"].exists()
        assert not test_files["cli"]["config"].exists()
        assert not test_files["manager"]["test"].exists()
        assert test_files["logging"]["test"].exists()
        assert test_files["conftest"].exists()
        assert not test_files["gitkeep"].exists()

        assert not bdd_files["tui"].exists()
        assert bdd_files["cli"].exists()
        assert not bdd_files["launch"].exists()
        assert not bdd_files["config"].exists()
        assert not bdd_files["manager"].exists()
        assert not bdd_files["resolution"].exists()
        assert bdd_files["regex"].exists()
        assert not bdd_files["gitkeep"].exists()
        assert not bdd_files["helpers"]["root"].exists()

        assert bdd_files["utils"]["root"].exists()
        assert bdd_files["utils"]["parsers"].exists()
        assert not bdd_files["utils"]["async"].exists()

        assert removal_tree["gitlab"]["ux"].exists()
        assert removal_tree["gitlab"]["arch"].exists()

    def test_bare_cli_no_bdd(self, removal_tree):
        cli_files = removal_tree["cli"]

        command_files = cli_files["commands"]
        helper_files = cli_files["helpers"]
        styling_files = cli_files["styling"]

        tui_files = removal_tree["tui"]
        bdd_files = removal_tree["bdd"]
        test_files = removal_tree["tests"]
        config_files = removal_tree["config"]
        logging_files = removal_tree["logging"]

        config = ProjectFlags(False, False, True, False, True, "semver", "bare_cli")

        remove_unused_files(removal_tree["root"], removal_tree["package_name"], config)

        assert not tui_files["root"].exists()

        assert cli_files["main"].exists()
        assert command_files["root_command"].exists()
        assert not command_files["launch"].exists()
        assert not command_files["config"]["root"].exists()

        assert not config_files["root"].exists()

        assert logging_files["formatters"].exists()
        assert logging_files["parsers"].exists()
        assert logging_files["tools"].exists()

        assert helper_files["converter"].exists()
        assert not helper_files["printer"].exists()

        assert styling_files["themes"].exists()

        assert not test_files["tui"]["root"].exists()
        assert test_files["cli"]["test"].exists()
        assert not test_files["cli"]["launch"].exists()
        assert not test_files["cli"]["config"].exists()
        assert not test_files["manager"]["test"].exists()
        assert test_files["logging"]["test"].exists()
        assert test_files["conftest"].exists()
        assert not test_files["gitkeep"].exists()

        assert not bdd_files["root"].exists()
        assert not bdd_files["helpers"]["root"].exists()
        assert not bdd_files["utils"]["root"].exists()

        assert removal_tree["gitlab"]["ux"].exists()
        assert removal_tree["gitlab"]["arch"].exists()

    def test_bare_repo_with_bdd(self, removal_tree):
        cli_files = removal_tree["cli"]

        config_command_files = cli_files["commands"]["config"]
        helper_files = cli_files["helpers"]
        styling_files = cli_files["styling"]

        tui_files = removal_tree["tui"]
        bdd_files = removal_tree["bdd"]
        test_files = removal_tree["tests"]
        config_files = removal_tree["config"]
        logging_files = removal_tree["logging"]

        config = ProjectFlags(False, False, False, False, True, "semver", "bare_repo")

        remove_unused_files(removal_tree["root"], removal_tree["package_name"], config)

        assert not tui_files["root"].exists()

        assert not cli_files["root"].exists()
        assert not cli_files["main"].exists()

        assert not config_command_files["root"].exists()
        assert not helper_files["root"].exists()
        assert not styling_files["root"].exists()

        assert not config_files["root"].exists()

        assert not logging_files["root"].exists()

        assert test_files["root"].exists()
        assert not test_files["tui"]["root"].exists()
        assert not test_files["cli"]["root"].exists()
        assert not test_files["manager"]["root"].exists()
        assert not test_files["logging"]["root"].exists()
        assert not test_files["conftest"].exists()
        assert test_files["gitkeep"].exists()

        assert bdd_files["root"].exists()
        assert not bdd_files["tui"].exists()
        assert not bdd_files["cli"].exists()
        assert not bdd_files["launch"].exists()
        assert not bdd_files["config"].exists()
        assert not bdd_files["manager"].exists()
        assert not bdd_files["resolution"].exists()
        assert not bdd_files["regex"].exists()
        assert bdd_files["gitkeep"].exists()
        assert not bdd_files["helpers"]["root"].exists()
        assert not bdd_files["utils"]["root"].exists()

        assert not removal_tree["gitlab"]["ux"].exists()
        assert not removal_tree["gitlab"]["arch"].exists()

    def test_bare_repo_no_bdd(self, removal_tree):
        cli_files = removal_tree["cli"]

        config_command_files = cli_files["commands"]["config"]
        helper_files = cli_files["helpers"]
        styling_files = cli_files["styling"]

        tui_files = removal_tree["tui"]
        bdd_files = removal_tree["bdd"]
        test_files = removal_tree["tests"]
        config_files = removal_tree["config"]
        logging_files = removal_tree["logging"]

        config = ProjectFlags(False, False, True, False, True, "semver", "bare_repo")

        remove_unused_files(removal_tree["root"], removal_tree["package_name"], config)

        assert not tui_files["root"].exists()

        assert not cli_files["root"].exists()
        assert not cli_files["main"].exists()

        assert not config_command_files["root"].exists()
        assert not helper_files["root"].exists()
        assert not styling_files["root"].exists()

        assert not config_files["root"].exists()

        assert not logging_files["root"].exists()

        assert test_files["root"].exists()
        assert not test_files["tui"]["root"].exists()
        assert not test_files["cli"]["root"].exists()
        assert not test_files["manager"]["root"].exists()
        assert not test_files["logging"]["root"].exists()
        assert not test_files["conftest"].exists()
        assert test_files["gitkeep"].exists()

        assert not bdd_files["root"].exists()
        assert not bdd_files["helpers"]["root"].exists()
        assert not bdd_files["utils"]["root"].exists()

        assert not removal_tree["gitlab"]["ux"].exists()
        assert not removal_tree["gitlab"]["arch"].exists()

    def test_remove_all(self, removal_tree):
        pyproject = removal_tree["pyproject"]

        cli_root = removal_tree["cli"]["root"]
        tui_root = removal_tree["tui"]["root"]

        config_root = removal_tree["config"]["root"]
        logging_root = removal_tree["logging"]["root"]

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

        ux_template = removal_tree["github"]["ux"]
        arch_template = removal_tree["github"]["arch"]

        config = ProjectFlags(True, True, True, True, False, "trunkver", "bare_repo")

        remove_unused_files(removal_tree["root"], removal_tree["package_name"], config)

        assert not cli_root.exists()
        assert not tui_root.exists()
        assert not config_root.exists()
        assert not logging_root.exists()
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

        assert not ux_template.exists()
        assert not arch_template.exists()


class TestVersioningSchemas:
    def test_calver_auto(self, removal_tree):
        github_files = removal_tree["github"]

        tag_workflow = github_files["weekly_tag_workflow"]

        config = ProjectFlags(True, False, False, False, True, "calver-auto", "cli")

        remove_unused_files(removal_tree["root"], removal_tree["package_name"], config)

        assert tag_workflow.exists()

    @pytest.mark.parametrize(
        "schema",
        ["semver", "effver", "romver", "calver-explicit", "solover", "trunkver"],
    )
    def test_non_calver_auto(self, removal_tree, schema):
        github_files = removal_tree["github"]

        tag_workflow = github_files["weekly_tag_workflow"]

        config = ProjectFlags(True, False, False, False, True, schema, "cli")

        remove_unused_files(removal_tree["root"], removal_tree["package_name"], config)

        assert not tag_workflow.exists()

    def test_trunkver(self, removal_tree):
        github_files = removal_tree["github"]

        release_drafter_config = github_files["release_drafter_config"]
        release_drafter_workflow = github_files["release_drafter_workflow"]
        test_template = github_files["test_template"]
        test_workflow = github_files["test_workflow"]

        config = ProjectFlags(True, False, False, False, True, "trunkver", "cli")

        remove_unused_files(removal_tree["root"], removal_tree["package_name"], config)

        assert not release_drafter_config.exists()
        assert not release_drafter_workflow.exists()
        assert not test_template.exists()

        assert test_workflow.exists()

    @pytest.mark.parametrize(
        "schema",
        ["semver", "effver", "romver", "calver-auto", "calver-explicit", "solover"],
    )
    def test_non_trunkver(self, removal_tree, schema):
        github_files = removal_tree["github"]

        release_drafter_config = github_files["release_drafter_config"]
        release_drafter_workflow = github_files["release_drafter_workflow"]
        test_template = github_files["test_template"]
        test_workflow = github_files["test_workflow"]

        config = ProjectFlags(True, False, False, False, True, schema, "cli")

        remove_unused_files(removal_tree["root"], removal_tree["package_name"], config)

        assert release_drafter_config.exists()
        assert release_drafter_workflow.exists()
        assert test_template.exists()
        assert test_workflow.exists()


class TestDocsGeneration:
    def test_oss_licence(self, removal_tree):
        getting_started = removal_tree["docs"]["getting_started"]
        tutorials = getting_started["tutorials"]
        overview = getting_started["overview"]

        dev = removal_tree["docs"]["development"]
        dev_section = dev["index"]
        dev_packages = dev["dev_packages"]["index"]

        ref = removal_tree["docs"]["reference"]
        ref_section = ref["index"]

        noticeboard = removal_tree["docs"]["noticeboard"]
        roadmap = noticeboard["roadmap"]
        security_guide = noticeboard["security"]
        advisories = noticeboard["advisories"]

        config = ProjectFlags(False, False, False, True, True, "semver-like", "tui")

        remove_unused_files(removal_tree["root"], removal_tree["package_name"], config)

        assert tutorials.exists()
        assert overview.exists()

        assert dev_section.exists()
        assert dev_packages.exists()
        assert ref_section.exists()

        assert not roadmap.exists()
        assert not security_guide.exists()
        assert advisories.exists()

    def test_non_oss_licence(self, removal_tree):
        getting_started = removal_tree["docs"]["getting_started"]
        tutorials = getting_started["tutorials"]
        overview = getting_started["overview"]

        dev = removal_tree["docs"]["development"]
        dev_section = dev["root"]

        ref = removal_tree["docs"]["reference"]
        ref_section = ref["index"]

        noticeboard = removal_tree["docs"]["noticeboard"]
        roadmap = noticeboard["roadmap"]
        security_guide = noticeboard["security"]
        advisories = noticeboard["advisories"]

        config = ProjectFlags(False, False, False, True, False, "semver-like", "tui")

        remove_unused_files(removal_tree["root"], removal_tree["package_name"], config)

        assert not tutorials.exists()
        assert overview.exists()

        assert not dev_section.exists()
        assert ref_section.exists()

        assert roadmap.exists()
        assert advisories.exists()
        assert security_guide.exists()

    @pytest.mark.parametrize("app_type", ["tui", "hybrid"])
    def test_tui_options_with_bdd(self, removal_tree, app_type):
        policies = removal_tree["docs"]["development"]["policies"]
        policy_bdd = policies["bdd"]
        policy_versioning = policies["versioning"]

        cli_guide = removal_tree["docs"]["user_guide"]["cli"]
        cli_guide_index = cli_guide["index"]
        cli_guide_options = cli_guide["options"]

        ref = removal_tree["docs"]["reference"]
        ref_manager = ref["config"]["manager"]
        ref_parser = ref["utils"]["parser"]
        ref_logger = ref["utils"]["logger"]

        dev_packages = removal_tree["docs"]["development"]["dev_packages"]
        dev_printer = dev_packages["cli"]["printer"]
        dev_converter = dev_packages["cli"]["converter"]
        dev_themes = dev_packages["cli"]["themes"]
        dev_tui = dev_packages["tui"]["app"]
        dev_config = dev_packages["internal"]["config"]
        dev_logging = dev_packages["internal"]["logging"]
        dev_tests = dev_packages["tests"]["index"]
        dev_helpers = dev_packages["tests"]["helpers"]
        dev_utils = dev_packages["tests"]["utils"]

        config = ProjectFlags(False, False, False, True, True, "semver-like", app_type)

        remove_unused_files(removal_tree["root"], removal_tree["package_name"], config)

        assert policy_bdd.exists()
        assert policy_versioning.exists()

        assert cli_guide_index.exists()
        assert cli_guide_options.exists()

        assert ref_manager.exists()
        assert ref_parser.exists()
        assert ref_logger.exists()

        assert dev_printer.exists()
        assert dev_converter.exists()
        assert dev_themes.exists()
        assert dev_tui.exists()
        assert dev_config.exists()
        assert dev_logging.exists()
        assert dev_tests.exists()
        assert dev_helpers.exists()
        assert dev_utils.exists()

    @pytest.mark.parametrize("app_type", ["tui", "hybrid"])
    def test_tui_options_no_bdd(self, removal_tree, app_type):
        policies = removal_tree["docs"]["development"]["policies"]
        policy_bdd = policies["bdd"]
        policy_versioning = policies["versioning"]

        cli_guide = removal_tree["docs"]["user_guide"]["cli"]
        cli_guide_index = cli_guide["index"]
        cli_guide_options = cli_guide["options"]

        ref = removal_tree["docs"]["reference"]
        ref_manager = ref["config"]["manager"]
        ref_parser = ref["utils"]["parser"]
        ref_logger = ref["utils"]["logger"]

        dev_packages = removal_tree["docs"]["development"]["dev_packages"]
        dev_printer = dev_packages["cli"]["printer"]
        dev_converter = dev_packages["cli"]["converter"]
        dev_themes = dev_packages["cli"]["themes"]
        dev_tui = dev_packages["tui"]["app"]
        dev_config = dev_packages["internal"]["config"]
        dev_logging = dev_packages["internal"]["logging"]
        dev_tests = dev_packages["tests"]["index"]
        dev_helpers = dev_packages["tests"]["helpers"]
        dev_utils = dev_packages["tests"]["utils"]

        config = ProjectFlags(False, False, True, True, True, "semver-like", app_type)

        remove_unused_files(removal_tree["root"], removal_tree["package_name"], config)

        assert not policy_bdd.exists()
        assert policy_versioning.exists()

        assert cli_guide_index.exists()
        assert cli_guide_options.exists()

        assert ref_manager.exists()
        assert ref_parser.exists()
        assert ref_logger.exists()

        assert dev_printer.exists()
        assert dev_converter.exists()
        assert dev_themes.exists()
        assert dev_tui.exists()
        assert dev_config.exists()
        assert dev_logging.exists()
        assert dev_tests.exists()
        assert not dev_helpers.exists()
        assert not dev_utils.exists()

    def test_cli_with_bdd(self, removal_tree):
        policies = removal_tree["docs"]["development"]["policies"]
        policy_bdd = policies["bdd"]
        policy_versioning = policies["versioning"]

        cli_guide = removal_tree["docs"]["user_guide"]["cli"]
        cli_guide_index = cli_guide["index"]
        cli_guide_options = cli_guide["options"]

        ref = removal_tree["docs"]["reference"]
        ref_manager = ref["config"]["manager"]
        ref_parser = ref["utils"]["parser"]
        ref_logger = ref["utils"]["logger"]

        dev_packages = removal_tree["docs"]["development"]["dev_packages"]
        dev_printer = dev_packages["cli"]["printer"]
        dev_converter = dev_packages["cli"]["converter"]
        dev_themes = dev_packages["cli"]["themes"]
        dev_tui = dev_packages["tui"]["root"]
        dev_config = dev_packages["internal"]["config"]
        dev_logging = dev_packages["internal"]["logging"]
        dev_tests = dev_packages["tests"]["index"]
        dev_helpers = dev_packages["tests"]["helpers"]
        dev_utils = dev_packages["tests"]["utils"]

        config = ProjectFlags(False, False, False, True, True, "semver-like", "cli")

        remove_unused_files(removal_tree["root"], removal_tree["package_name"], config)

        assert policy_bdd.exists()
        assert policy_versioning.exists()

        assert cli_guide_index.exists()
        assert cli_guide_options.exists()

        assert ref_manager.exists()
        assert ref_parser.exists()
        assert ref_logger.exists()

        assert dev_printer.exists()
        assert dev_converter.exists()
        assert dev_themes.exists()
        assert not dev_tui.exists()
        assert dev_config.exists()
        assert dev_logging.exists()
        assert dev_tests.exists()
        assert not dev_helpers.exists()
        assert dev_utils.exists()

    def test_cli_no_bdd(self, removal_tree):
        policies = removal_tree["docs"]["development"]["policies"]
        policy_bdd = policies["bdd"]
        policy_versioning = policies["versioning"]

        cli_guide = removal_tree["docs"]["user_guide"]["cli"]
        cli_guide_index = cli_guide["index"]
        cli_guide_options = cli_guide["options"]

        ref = removal_tree["docs"]["reference"]
        ref_manager = ref["config"]["manager"]
        ref_parser = ref["utils"]["parser"]
        ref_logger = ref["utils"]["logger"]

        dev_packages = removal_tree["docs"]["development"]["dev_packages"]
        dev_printer = dev_packages["cli"]["printer"]
        dev_converter = dev_packages["cli"]["converter"]
        dev_themes = dev_packages["cli"]["themes"]
        dev_tui = dev_packages["tui"]["root"]
        dev_config = dev_packages["internal"]["config"]
        dev_logging = dev_packages["internal"]["logging"]
        dev_tests = dev_packages["tests"]["index"]
        dev_helpers = dev_packages["tests"]["helpers"]
        dev_utils = dev_packages["tests"]["utils"]

        config = ProjectFlags(False, False, True, True, True, "semver-like", "cli")

        remove_unused_files(removal_tree["root"], removal_tree["package_name"], config)

        assert not policy_bdd.exists()
        assert policy_versioning.exists()

        assert cli_guide_index.exists()
        assert cli_guide_options.exists()

        assert ref_manager.exists()
        assert ref_parser.exists()
        assert ref_logger.exists()

        assert dev_printer.exists()
        assert dev_converter.exists()
        assert dev_themes.exists()
        assert not dev_tui.exists()
        assert dev_config.exists()
        assert dev_logging.exists()
        assert dev_tests.exists()
        assert not dev_helpers.exists()
        assert not dev_utils.exists()

    def test_bare_cli_with_bdd(self, removal_tree):
        policies = removal_tree["docs"]["development"]["policies"]
        policy_bdd = policies["bdd"]
        policy_versioning = policies["versioning"]

        cli_guide = removal_tree["docs"]["user_guide"]["cli"]
        cli_guide_index = cli_guide["index"]
        cli_guide_options = cli_guide["options"]

        ref = removal_tree["docs"]["reference"]
        ref_config = ref["config"]["root"]
        ref_parser = ref["utils"]["parser"]
        ref_logger = ref["utils"]["logger"]

        dev_packages = removal_tree["docs"]["development"]["dev_packages"]
        dev_printer = dev_packages["cli"]["printer"]
        dev_converter = dev_packages["cli"]["converter"]
        dev_themes = dev_packages["cli"]["themes"]
        dev_tui = dev_packages["tui"]["root"]
        dev_config = dev_packages["internal"]["config"]
        dev_logging = dev_packages["internal"]["logging"]
        dev_tests = dev_packages["tests"]["index"]
        dev_helpers = dev_packages["tests"]["helpers"]
        dev_utils = dev_packages["tests"]["utils"]

        config = ProjectFlags(
            False, False, False, True, True, "semver-like", "bare_cli"
        )

        remove_unused_files(removal_tree["root"], removal_tree["package_name"], config)

        assert policy_bdd.exists()
        assert policy_versioning.exists()

        assert cli_guide_index.exists()
        assert not cli_guide_options.exists()

        assert not ref_config.exists()
        assert ref_parser.exists()
        assert ref_logger.exists()

        assert not dev_printer.exists()
        assert dev_converter.exists()
        assert dev_themes.exists()
        assert not dev_tui.exists()
        assert not dev_config.exists()
        assert dev_logging.exists()
        assert dev_tests.exists()
        assert not dev_helpers.exists()
        assert dev_utils.exists()

    def test_bare_cli_no_bdd(self, removal_tree):
        policies = removal_tree["docs"]["development"]["policies"]
        policy_bdd = policies["bdd"]
        policy_versioning = policies["versioning"]

        cli_guide = removal_tree["docs"]["user_guide"]["cli"]
        cli_guide_index = cli_guide["index"]
        cli_guide_options = cli_guide["options"]

        ref = removal_tree["docs"]["reference"]
        ref_config = ref["config"]["root"]
        ref_parser = ref["utils"]["parser"]
        ref_logger = ref["utils"]["logger"]

        dev_packages = removal_tree["docs"]["development"]["dev_packages"]
        dev_printer = dev_packages["cli"]["printer"]
        dev_converter = dev_packages["cli"]["converter"]
        dev_themes = dev_packages["cli"]["themes"]
        dev_tui = dev_packages["tui"]["root"]
        dev_config = dev_packages["internal"]["config"]
        dev_logging = dev_packages["internal"]["logging"]
        dev_tests = dev_packages["tests"]["index"]
        dev_helpers = dev_packages["tests"]["helpers"]
        dev_utils = dev_packages["tests"]["utils"]

        config = ProjectFlags(False, False, True, True, True, "semver-like", "bare_cli")

        remove_unused_files(removal_tree["root"], removal_tree["package_name"], config)

        assert not policy_bdd.exists()
        assert policy_versioning.exists()

        assert cli_guide_index.exists()
        assert not cli_guide_options.exists()

        assert not ref_config.exists()
        assert ref_parser.exists()
        assert ref_logger.exists()

        assert not dev_printer.exists()
        assert dev_converter.exists()
        assert dev_themes.exists()
        assert not dev_tui.exists()
        assert not dev_config.exists()
        assert dev_logging.exists()
        assert dev_tests.exists()
        assert not dev_helpers.exists()
        assert not dev_utils.exists()

    def test_bare_repo_with_bdd(self, removal_tree):
        policies = removal_tree["docs"]["development"]["policies"]
        policy_bdd = policies["bdd"]
        policy_versioning = policies["versioning"]

        user_guide = removal_tree["docs"]["user_guide"]
        cli_guide = user_guide["cli"]["root"]
        faq = user_guide["faq"]

        ref = removal_tree["docs"]["reference"]
        ref_index = ref["index"]
        ref_config = ref["config"]["root"]
        ref_utils = ref["utils"]["root"]

        dev_packages = removal_tree["docs"]["development"]["dev_packages"]
        dev_packages_index = dev_packages["index"]
        dev_cli = dev_packages["cli"]["root"]
        dev_tui = dev_packages["tui"]["root"]
        dev_config = dev_packages["internal"]["root"]
        dev_tests = dev_packages["tests"]["root"]

        config = ProjectFlags(
            False, False, False, True, True, "semver-like", "bare_repo"
        )

        remove_unused_files(removal_tree["root"], removal_tree["package_name"], config)

        assert policy_bdd.exists()
        assert policy_versioning.exists()

        assert not cli_guide.exists()
        assert faq.exists()

        assert ref_index.exists()
        assert not ref_config.exists()
        assert not ref_utils.exists()

        assert dev_packages_index.exists()
        assert not dev_cli.exists()
        assert not dev_tui.exists()
        assert not dev_config.exists()
        assert not dev_tests.exists()

    def test_bare_repo_no_bdd(self, removal_tree):
        policies = removal_tree["docs"]["development"]["policies"]
        policy_bdd = policies["bdd"]
        policy_versioning = policies["versioning"]

        user_guide = removal_tree["docs"]["user_guide"]
        cli_guide = user_guide["cli"]["root"]
        faq = user_guide["faq"]

        ref = removal_tree["docs"]["reference"]
        ref_index = ref["index"]
        ref_config = ref["config"]["root"]
        ref_utils = ref["utils"]["root"]

        dev_packages = removal_tree["docs"]["development"]["dev_packages"]
        dev_packages_index = dev_packages["index"]
        dev_cli = dev_packages["cli"]["root"]
        dev_tui = dev_packages["tui"]["root"]
        dev_config = dev_packages["internal"]["root"]
        dev_tests = dev_packages["tests"]["root"]

        config = ProjectFlags(
            False, False, True, True, True, "semver-like", "bare_repo"
        )

        remove_unused_files(removal_tree["root"], removal_tree["package_name"], config)

        assert not policy_bdd.exists()
        assert policy_versioning.exists()

        assert not cli_guide.exists()
        assert faq.exists()

        assert ref_index.exists()
        assert not ref_config.exists()
        assert not ref_utils.exists()

        assert dev_packages_index.exists()
        assert not dev_cli.exists()
        assert not dev_tui.exists()
        assert not dev_config.exists()
        assert not dev_tests.exists()


class TestFeatureFiles:
    def test_remove_feature_files(self, removal_tree):
        feature_files = removal_tree["features"]

        file1 = feature_files["file1"]
        file2 = feature_files["file2"]
        directory = feature_files["directory"]

        config = ProjectFlags(False, False, False, True, True, "semver", "cli")

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

        config = ProjectFlags(False, False, False, False, True, "semver", "cli")

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


class TestInstructions:
    @pytest.mark.parametrize("rich_output", [True, None])
    def test_print_further_instructions(
        self, capsys, mocker, rich_output, galactipy_instructions
    ):
        mocker.patch("hooks.post_gen_project.which", side_effect=[True, True])
        mocker.patch("hooks.post_gen_project.find_spec", return_value=rich_output)

        print_further_instructions(
            "Galactipy",
            "galactipy",
            "GitLab",
            "https://www.gitlab.com/galactipy/galactipy",
            ":tada:",
        )
        captured = capsys.readouterr()

        # STDOUT always finishes with a newline
        assert captured.out == galactipy_instructions + "\n"

    @pytest.mark.parametrize("rich_output", [True, None])
    def test_print_invoke_instructions(
        self, capsys, mocker, rich_output, galactipy_invoke_instructions
    ):
        mocker.patch("hooks.post_gen_project.which", side_effect=[True, None])
        mocker.patch("hooks.post_gen_project.find_spec", return_value=rich_output)

        print_further_instructions(
            "Galactipy",
            "galactipy",
            "GitLab",
            "https://www.gitlab.com/galactipy/galactipy",
            ":tada:",
        )
        captured = capsys.readouterr()

        # STDOUT always finishes with a newline
        assert captured.out == galactipy_invoke_instructions + "\n"

    @pytest.mark.parametrize(
        "rich_output",
        [
            pytest.param(
                True,
                marks=pytest.mark.xfail(
                    reason="rich.Console width defaults to 80, unable to mock"
                ),
            ),
            None,
        ],
    )
    def test_print_poetry_instructions(
        self, capsys, mocker, rich_output, galactipy_poetry_instructions
    ):
        mocker.patch("hooks.post_gen_project.which", side_effect=[None, True])
        mocker.patch("hooks.post_gen_project.find_spec", return_value=rich_output)

        print_further_instructions(
            "Galactipy",
            "galactipy",
            "GitLab",
            "https://www.gitlab.com/galactipy/galactipy",
            ":tada:",
        )
        captured = capsys.readouterr()

        # STDOUT always finishes with a newline
        assert captured.out == galactipy_poetry_instructions + "\n"
