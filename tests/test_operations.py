import pytest

from hooks.post_gen_project import generate_licence, generate_templates, licences_dict
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
