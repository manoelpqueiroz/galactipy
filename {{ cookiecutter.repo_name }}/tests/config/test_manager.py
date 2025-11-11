{%- if cookiecutter.use_bdd -%}
from pytest_bdd import given, parsers, scenario, then, when
{%- else -%}
import pytest
{%- endif %}

from {{ cookiecutter.package_name }}.config import AppManager, resolve_app_manager
{%- if cookiecutter.use_bdd %}

from tests.utils import boolean_parser


@scenario("app_manager.feature", "Manage at runtime")
def test_runtime_manager():
    pass


@when("the user calls a manager", target_fixture="manager_instance")
def call_manager(mock_config_path):  # noqa: ARG001
    return AppManager()


@then("the manager object is empty")
def check_empty_manager(manager_instance):
    assert manager_instance.empty


@then("the base directory points to the user config path")
def check_base_directory(manager_instance, mock_config_path):
    assert manager_instance.base_config_dir == mock_config_path


@scenario("app_manager.feature", "Call default manager")
def test_default_manager():
    pass


@when("the user calls the default manager", target_fixture="manager_instance")
def call_default_manager(mock_config_path):  # noqa: ARG001
    return AppManager.default()


@then(parsers.parse('both "{settings}" and "{secrets}" are accessible'))
def check_both_domains(manager_instance, settings, secrets):
    assert settings in manager_instance
    assert secrets in manager_instance


@then(
    parsers.parse(
        "the {configuration_type} environment variable prefix matches the "
        "{expected_envvar} value"
    )
)
def check_envvar_prefix(manager_instance, configuration_type, expected_envvar):
    assert (
        manager_instance[configuration_type].envvar_prefix_for_dynaconf
        == expected_envvar
    )


@scenario("app_manager.feature", "Call custom manager")
def test_custom_manager():
    pass


@given(
    "an existing configuration file outside the user config path",
    target_fixture="custom_config",
)
def ensure_custom_config(tmp_path):
    custom_file = tmp_path / "test.toml"
    custom_file.touch()

    assert custom_file.exists()

    return custom_file


@when(
    parsers.parse("the user calls a custom manager {configuration_type}"),
    target_fixture="manager_instance",
)
def call_custom_manager(configuration_type, custom_config):
    return AppManager.custom(custom_config, configuration_type)


@then(parsers.parse("only the {configuration_type} domain is accessible"))
def ensure_single_domain(manager_instance, configuration_type):
    assert configuration_type in manager_instance
    assert len(manager_instance) == 1


@scenario("manager_resolution.feature", "Application resolution")
def test_application_resolution():
    pass


@when(
    parsers.parse(
        "the resolver receives a request with {domain} and {uses_custom_path:Boolean}",
        extra_types={"Boolean": boolean_parser},
    ),
    target_fixture="resolved_manager",
)
def provide_resolver_arguments(
    mock_config_path,  # noqa: ARG001
    tmp_path,
    domain,
    uses_custom_path,
):
    if uses_custom_path:
        custom_file = tmp_path / "test.toml"
        custom_file.touch()

        assert custom_file.exists()

    else:
        custom_file = None

    return resolve_app_manager(domain, custom_file)


@then(
    parsers.parse(
        "it returns a manager with {manager_length:Int} domains",
        extra_types={"Int": int},
    )
)
def check_custom_manager_with_resolver(resolved_manager, manager_length):
    assert len(resolved_manager) == manager_length


@then(
    parsers.parse(
        "validating the {domain} file inside the base directory is "
        "{file_in_base_dir:Boolean}",
        extra_types={"Boolean": boolean_parser},
    )
)
def check_base_directory_contents(mock_config_path, file_in_base_dir, domain):
    base_file = mock_config_path / f"{domain}.toml"

    assert base_file.exists() == file_in_base_dir
{%- else %}


@pytest.mark.backend
@pytest.mark.config
@pytest.mark.standard
def test_runtime_manager(mock_config_path):
    manager_instance = AppManager()

    assert manager_instance.empty
    assert manager_instance.base_config_dir == mock_config_path


@pytest.mark.backend
@pytest.mark.config
@pytest.mark.standard
@pytest.mark.parametrize(
    ("configuration_type", "expected_envvar"),
    (["settings", "{{ cookiecutter.__envvar }}"], ["secrets", "{{ cookiecutter.__envvar }}_SECRET"]),
)
def test_default_manager(
    mock_config_path,  # noqa: ARG001
    configuration_type,
    expected_envvar,
):
    manager_instance = AppManager.default()

    assert "settings" in manager_instance
    assert "secrets" in manager_instance

    assert (
        manager_instance[configuration_type].envvar_prefix_for_dynaconf
        == expected_envvar
    )


@pytest.mark.backend
@pytest.mark.config
@pytest.mark.standard
@pytest.mark.parametrize(
    ("configuration_type", "expected_envvar"),
    (["settings", "{{ cookiecutter.__envvar }}"], ["secrets", "{{ cookiecutter.__envvar }}_SECRET"]),
)
def test_custom_manager(tmp_path, configuration_type, expected_envvar):
    custom_file = tmp_path / "test.toml"
    custom_file.touch()

    assert custom_file.exists()

    manager_instance = AppManager.custom(custom_file, configuration_type)

    assert configuration_type in manager_instance
    assert len(manager_instance) == 1

    assert (
        manager_instance[configuration_type].envvar_prefix_for_dynaconf
        == expected_envvar
    )


@pytest.mark.backend
@pytest.mark.config
@pytest.mark.standard
@pytest.mark.parametrize(
    ("domain", "uses_custom_path", "manager_length", "file_in_base_dir"),
    (
        ["settings", False, 2, True],
        ["secrets", False, 2, True],
        ["settings", True, 1, False],
        ["secrets", True, 1, False],
    ),
)
def test_application_resolution(
    mock_config_path,
    tmp_path,
    domain,
    uses_custom_path,
    manager_length,
    file_in_base_dir,
):
    if uses_custom_path:
        custom_file = tmp_path / "test.toml"
        custom_file.touch()

        assert custom_file.exists()

    else:
        custom_file = None

    manager = resolve_app_manager(domain, custom_file)

    assert len(manager) == manager_length

    base_file = mock_config_path / f"{domain}.toml"

    assert base_file.exists() == file_in_base_dir
{%- endif %}
