{% if cookiecutter.use_bdd -%}
from pytest_bdd import given, parsers, scenario, then, when
{% else -%}
import pytest
{%- endif %}

from {{ cookiecutter.package_name }}.config import AppManager, resolve_app_manager
{% if cookiecutter.use_bdd -%}
from tests.utils import boolean_parser


@scenario("app_manager.feature", "Manage at runtime")
def test_runtime_manager():
    pass


@when("the user calls a manager", target_fixture="manager_instance")
def call_manager(mock_config_path):
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
def call_default_manager(mock_config_path):
    return AppManager.default()


@then(parsers.parse('both "{settings}" and "{secrets}" are accessible'))
def check_both_domains(manager_instance, settings, secrets):
    assert settings in manager_instance
    assert secrets in manager_instance


@then(
    parsers.parse(
        "the {configuration_type} environment variable prefix matches the {expected_envvar} value"
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
    is_secret = configuration_type == "secrets"

    return AppManager.custom(custom_config, is_secret)


@then(parsers.parse("only the {configuration_type} domain is accessible"))
def ensure_single_domain(manager_instance, configuration_type):
    assert configuration_type in manager_instance
    assert len(manager_instance) == 1


@scenario("manager_resolution.feature", "Application resolution")
def test_application_resolution():
    pass


@when(
    parsers.parse(
        "the resolver receives a request with {is_secret:Boolean} and "
        "{uses_custom_path:Boolean}",
        extra_types={"Boolean": boolean_parser},
    ),
    target_fixture="resolver_output",
)
def provide_resolver_arguments(mock_config_path, tmp_path, is_secret, uses_custom_path):
    if uses_custom_path:
        custom_file = tmp_path / "test.toml"
        custom_file.touch()

        assert custom_file.exists()

    else:
        custom_file = None

    return resolve_app_manager(is_secret, custom_file)


@then(
    parsers.parse(
        "it returns a manager with {manager_length:Int} domains",
        extra_types={"Int": int},
    )
)
def check_custom_manager_with_resolver(resolver_output, manager_length):
    assert len(resolver_output[1]) == manager_length


@then(parsers.parse("a string with {configuration_type} value"))
def check_configuration_type_with_resolver(resolver_output, configuration_type):
    assert resolver_output[0] == configuration_type


@then(
    parsers.parse(
        "validating the {configuration_type} file inside the base directory is "
        "{file_in_base_dir:Boolean}",
        extra_types={"Boolean": boolean_parser},
    )
)
def check_base_directory_contents(
    mock_config_path, file_in_base_dir, configuration_type, resolver_output
):
    base_file = mock_config_path / f"{configuration_type}.toml"

    assert base_file.exists() == file_in_base_dir
{%- else %}
def test_runtime_manager(mock_config_path):
    manager_instance = AppManager()

    assert manager_instance.empty
    assert manager_instance.base_config_dir == mock_config_path


@pytest.mark.parametrize("configuration_type,expected_envvar", [
("settings", "{{ cookiecutter.__envvar }}"),
("secrets", "{{ cookiecutter.__envvar }}_SECRET"),
])
def test_default_manager(mock_config_path, configuration_type, expected_envvar):
    manager_instance = AppManager.default()

    assert "settings" in manager_instance
    assert "secrets" in manager_instance

    assert (
        manager_instance[configuration_type].envvar_prefix_for_dynaconf
        == expected_envvar
    )


@pytest.mark.parametrize("configuration_type,expected_envvar", [
("settings", "{{ cookiecutter.__envvar }}"),
("secrets", "{{ cookiecutter.__envvar }}_SECRET"),
])
def test_custom_manager(tmp_path, configuration_type, expected_envvar):
    custom_file = tmp_path / "test.toml"
    custom_file.touch()

    assert custom_file.exists()

    is_secret = configuration_type == "secrets"
    manager_instance = AppManager.custom(custom_file, is_secret)

    assert configuration_type in manager_instance
    assert len(manager_instance) == 1

    assert (
        manager_instance[configuration_type].envvar_prefix_for_dynaconf
        == expected_envvar
    )


@pytest.mark.parametrize(
    "is_secret,uses_custom_path,configuration_type,manager_length,file_in_base_dir",
    [
        (False, False, "settings", 2, True),
        (True, False, "secrets", 2, True),
        (False, True, "settings", 1, False),
        (True, True, "secrets", 1, False),
    ]
)
def test_application_resolution(
    mock_config_path,
    tmp_path,
    is_secret,
    uses_custom_path,
    configuration_type,
    manager_length,
    file_in_base_dir,
):
    if uses_custom_path:
        custom_file = tmp_path / "test.toml"
        custom_file.touch()

        assert custom_file.exists()

    else:
        custom_file = None

    resolver_output = resolve_app_manager(is_secret, custom_file)

    assert len(resolver_output[1]) == manager_length
    assert resolver_output[0] == configuration_type

    base_file = mock_config_path / f"{configuration_type}.toml"

    assert base_file.exists() == file_in_base_dir
{%- endif %}
