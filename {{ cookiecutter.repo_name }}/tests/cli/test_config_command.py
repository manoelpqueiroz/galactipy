from ast import literal_eval

from typer.testing import CliRunner

from dynaconf.base import BoxList
from orbittings.exceptions import SettingNotFoundError

{% if cookiecutter.use_bdd -%}
from pytest_bdd import given, parsers, scenario, then, when
{% else -%}
import pytest
{%- endif %}

from {{ cookiecutter.package_name }}.cli.commands.config import (
    config_extend_app,
    config_get_app,
    config_set_app,
    config_unset_app,
)
{% if cookiecutter.use_bdd -%}
from tests.utils.parsers import boolean_parser

ARRAY_LENGTH_STEP = parsers.parse(
    'the value for "{key}" has {length:Int} elements', extra_types={"Int": int}
)
{% endif %}

runner = CliRunner()


{% if cookiecutter.use_bdd -%}
@scenario("config_command.feature", "Get the entire configuration")
def test_get_entire_config():
    pass


@given(
    parsers.parse(
        'the configuration contains the key-value pair of "{key}" and "{value}"'
    ),
    target_fixture="config_dict",
)
def set_test_key(sandbox_manager, key, value):
    sandbox_manager["settings", key] = value

    sandbox_manager.save_all()
    sandbox_manager.reload_all()

    assert sandbox_manager["settings", key] == value

    return str(sandbox_manager["settings"].to_dict())


@when("the get program receives no arguments", target_fixture="cli_run")
def setup_get_command(sandbox_manager, sandbox_config_file):
    results = runner.invoke(config_get_app, args=["--path", sandbox_config_file])
    sandbox_manager.reload_all()

    return results


@then("the terminal prints the entire configuration as a dictionary")
def full_complete_config_output(cli_run, config_dict):
    assert cli_run.output == config_dict + "\n"


@then("the program exits without errors")
def successful_termination(cli_run):
    assert cli_run.exit_code == 0


@scenario("config_command.feature", "Get individual configuration value")
def test_get_individual_value():
    pass


@given(
    parsers.parse(
        'the configuration has a "{key}" key with a value of {value} and type '
        "{value_type}"
    )
)
def set_individual_test_key(sandbox_manager, key, value, value_type):
    saved_value = value if value_type == "string" else literal_eval(value)

    sandbox_manager["settings", key] = saved_value

    sandbox_manager.save_all()
    sandbox_manager.reload_all()

    assert sandbox_manager["settings", key] == saved_value


@when(
    parsers.parse('the get program receives the "{key}" key'), target_fixture="cli_run"
)
def get_key(sandbox_manager, sandbox_config_file, key):
    results = runner.invoke(config_get_app, args=[key, "--path", sandbox_config_file])
    sandbox_manager.reload_all()

    return results


@then(parsers.parse("the terminal prints {output} to the user"))
def get_command_output(cli_run, output):
    assert cli_run.output == f"{output}\n"


@scenario("config_command.feature", "Get an invalid configuration value")
def test_get_invalid_value():
    pass


@then("the program raises a key error")
def ensure_key_error(cli_run):
    assert cli_run.exc_info[0] is KeyError


@then("the program exits with status 1")
def ensure_status_1(cli_run):
    assert cli_run.exit_code == 1


@scenario("config_command.feature", "Set a new value")
def test_set_new_value():
    pass


@given(parsers.parse('the key "{key}" does not exist in the configuration'))
def ensure_no_key(sandbox_manager, key):
    assert sandbox_manager.get(f"settings.{key}") is None


@when(
    parsers.parse('the set program receives the "{key}" key with "{value}" value'),
    target_fixture="cli_run",
)
def setup_set_command(sandbox_manager, sandbox_config_file, key, value):
    results = runner.invoke(
        config_set_app, args=[key, value, "--path", sandbox_config_file]
    )
    sandbox_manager.reload_all()

    return results


@then(parsers.parse('the configuration adds a new key "{key}" with value "{value}"'))
def check_added_value(sandbox_manager, key, value):
    assert sandbox_manager["settings", key] == value


@scenario("config_command.feature", "Override an existing value")
def test_set_existing_value():
    pass


@then(
    parsers.parse(
        'the configuration replaces the value for the "{key}" key with "{new_value}"'
    )
)
def check_overridden_value(sandbox_manager, key, new_value):
    assert sandbox_manager["settings", key] == new_value


@scenario("config_command.feature", "Set empty string")
def test_set_empty_string():
    pass


@when(
    parsers.parse('the set program receives the key "{key}" with an empty string'),
    target_fixture="cli_run",
)
def setup_set_empty_string(sandbox_manager, sandbox_config_file, key):
    results = runner.invoke(
        config_set_app, args=[key, "", "--path", sandbox_config_file]
    )
    sandbox_manager.reload_all()

    return results


@then(parsers.parse('the terminal shows a "{msg}" message'))
def failed_value_parsing(cli_run, msg):
    assert cli_run.output == f"{msg}\n"


@scenario("config_command.feature", "Set a sequence value")
def test_set_sequence_values():
    pass


@when(
    parsers.parse('the set program receives the "{key}" key and value {value}'),
    target_fixture="cli_run",
)
def setup_non_string_value(sandbox_manager, sandbox_config_file, key, value):
    results = runner.invoke(
        config_set_app, args=[key, value, "--path", sandbox_config_file]
    )
    sandbox_manager.reload_all()

    return results


@then(parsers.parse('the key "{key}" becomes available in the configuration'))
def check_test_key(sandbox_manager, key):
    assert sandbox_manager.get(f"settings.{key}") is not None


@then(parsers.parse('the value for "{key}" is of a list type'))
def check_list_type_value(sandbox_manager, key):
    value = sandbox_manager["settings", key]

    assert isinstance(value, BoxList)


@scenario("config_command.feature", "Set a boolean value")
def test_set_boolean_values():
    pass


@then(parsers.parse('the value for "{key}" is of a boolean type'))
def check_bool_type_value(sandbox_manager, key):
    value = sandbox_manager["settings", key]

    assert isinstance(value, bool)


@scenario("config_command.feature", "Set positive integer value")
def test_set_positive_integer_values():
    pass


@then(parsers.parse('the value for "{key}" is of an integer type'))
def check_int_type_value(sandbox_manager, key):
    value = sandbox_manager["settings", key]

    assert isinstance(value, int)


@scenario("config_command.feature", "Set valid negative integer value")
def test_set_negative_integer_values():
    pass


@when(
    parsers.parse(
        'the set program receives the "{key}" key and value {value} with a double dash'
    ),
    target_fixture="cli_run",
)
def setup_negative_number(sandbox_manager, sandbox_config_file, key, value):
    results = runner.invoke(
        config_set_app, args=[key, "--path", sandbox_config_file, "--", value]
    )
    sandbox_manager.reload_all()

    return results


@scenario("config_command.feature", "Set positive float value")
def test_set_positive_float_values():
    pass


@then(parsers.parse('the value for "{key}" is of a float type'))
def check_float_type_value(sandbox_manager, key):
    value = sandbox_manager["settings", key]

    assert isinstance(value, float)


@scenario("config_command.feature", "Set valid negative float value")
def test_set_negative_float_values():
    pass


@scenario("config_command.feature", "Set invalid negative numbers")
def test_set_invalid_negative_numbers():
    pass


@then("the program exits with status 2")
def ensure_status_2(cli_run):
    assert cli_run.exit_code == 2


@scenario("config_command.feature", "Set near numeric values")
def test_set_near_numeric_value():
    pass


@then(parsers.parse('the value for "{key}" is of a string type'))
def check_string_type_value(sandbox_manager, key):
    value = sandbox_manager["settings", key]

    assert isinstance(value, str)


@scenario("config_command.feature", "Set a mapping value")
def test_set_dict_values():
    pass


@then(parsers.parse('the value for "{key}" is of a dictionary type'))
def check_dict_type_value(sandbox_manager, key):
    value = sandbox_manager["settings", key]

    assert isinstance(value, dict)


@scenario("config_command.feature", "Set malformed collection type")
def test_malformed_collection():
    pass


@scenario("config_command.feature", "Extend non-existing key without creating")
def test_extend_without_creating():
    pass


@when(
    parsers.parse(
        'the extend program receives the key "{key}" and "{value}" value with the '
        "`--create-on-missing` option set to {flag:Boolean}",
        extra_types={"Boolean": boolean_parser},
    ),
    target_fixture="cli_run",
)
def setup_extend(sandbox_manager, sandbox_config_file, key, value, flag):
    if flag:
        results = runner.invoke(
            config_extend_app,
            args=[key, value, "--create-on-missing", "--path", sandbox_config_file],
        )

    else:
        results = runner.invoke(
            config_extend_app, args=[key, value, "--path", sandbox_config_file]
        )

    sandbox_manager.reload_all()

    return results


@then(parsers.parse('the terminal shows a message mentioning "{key}" was not found'))
def failed_non_existing_extend(cli_run, key):
    msg = (
        f"Setting `{key}` was not found, if you wish to update the configuration, run "
        "the command with the `--create-on-missing` option\n"
    )

    assert cli_run.output == msg


@scenario("config_command.feature", "Create array key")
def test_extend_with_creating():
    pass


@given(ARRAY_LENGTH_STEP)
@then(ARRAY_LENGTH_STEP)
def check_array_value_length(sandbox_manager, key, length):
    value = sandbox_manager["settings", key]

    assert len(value) == length


@then(parsers.parse('the last element for "{key}" is equal to "{argument}"'))
def check_array_last_element(sandbox_manager, key, argument):
    value = sandbox_manager["settings", key]

    assert value[-1] == argument


@scenario("config_command.feature", "Extend existing key")
def test_extend_existing_key():
    pass


@given(parsers.parse('the configuration has a "{key}" key with a list type value'))
def set_array_value(sandbox_manager, key):
    sandbox_manager["settings", key] = [0, 1, 2]
    sandbox_manager.save_all()

    assert isinstance(sandbox_manager["settings", key], list)


@scenario("config_command.feature", "Extend a scalar value")
def test_extend_scalar_value():
    pass


@then(parsers.parse('the terminal shows a message mentioning "{key}" must be an array'))
def failed_scalar_extend(sandbox_manager, cli_run, key):
    current_value = sandbox_manager["settings", key]

    msg = (
        f"To extend settings, the value for `{key}` must be an array, got "
        f"{current_value} instead\n"
    )

    assert cli_run.output == msg


@scenario("config_command.feature", "Extend with empty string")
def test_extend_empty_string():
    pass


@when(
    parsers.parse(
        'the extend program receives the key "{key}" with an empty string and the '
        "`--create-on-missing` option set to {flag}"
    ),
    target_fixture="cli_run",
)
def setup_extend_empty_string(sandbox_manager, sandbox_config_file, key, flag):
    if flag:
        results = runner.invoke(
            config_extend_app,
            args=[key, "", "--create-on-missing", "--path", sandbox_config_file],
        )

    else:
        results = runner.invoke(
            config_extend_app, args=[key, "", "--path", sandbox_config_file]
        )

    sandbox_manager.reload_all()

    return results


@scenario("config_command.feature", "Unset a valid top-level value")
def test_unset_existing_value():
    pass


@when(
    parsers.parse('the unset program receives the key "{key}"'),
    target_fixture="cli_run",
)
def unset_value(sandbox_manager, sandbox_config_file, key):
    results = runner.invoke(config_unset_app, args=[key, "--path", sandbox_config_file])
    sandbox_manager.reload_all()

    return results


@then(parsers.parse('the key "{key}" is removed from the configuration'))
def check_removed_value(sandbox_manager, key):
    assert sandbox_manager.get(f"settings.{key}") is None


@scenario("config_command.feature", "Unset a non-existing value")
def test_unset_non_existing_value():
    pass


@then("the program raises a setting not found error")
def ensure_setting_error(cli_run):
    assert cli_run.exc_info[0] is SettingNotFoundError
{%- else %}
@pytest.mark.cli
@pytest.mark.config
class TestGetCommand:
    @pytest.mark.standard
    def test_get_entire_config(self, setup_sample_manager):
        manager, file = setup_sample_manager.values()
        config_dict = manager.settings.to_dict()

        results = runner.invoke(config_get_app, args=["--path", file])
        manager.reload_all()

        assert results.exit_code == 0
        assert results.output == str(config_dict) + "\n"

    @pytest.mark.standard
    @pytest.mark.parametrize(
        ("value", "output"),
        (
            ("somevalue", "'somevalue'"),
            ([1, 2, "a"], "[1, 2, 'a']"),
            ({"a": 1, "b": 2}, "{'a': 1, 'b': 2}"),
        ),
    )
    def test_get_individual_value(
        self, generate_test_config, value, output
    ):
        manager, file = generate_test_config.values()

        manager["settings", "test"] = value

        manager.save_all()
        manager.reload_all()

        assert manager["settings", "test"] == value

        results = runner.invoke(config_get_app, args=["test", "--path", file])
        manager.reload_all()

        assert results.exit_code == 0
        assert results.output == f"{output}\n"

    @pytest.mark.standard
    def test_get_invalid_value(self, setup_sample_manager):
        manager, file = setup_sample_manager.values()

        results = runner.invoke(config_get_app, args=["notest", "--path", file])

        assert results.exit_code == 1
        assert results.exc_info[0] is KeyError


@pytest.mark.cli
@pytest.mark.config
class TestSetCommand:
    @pytest.mark.standard
    def test_set_new_value(self, generate_test_config):
        manager, file = generate_test_config.values()
        key = "test"
        value = "somevalue"

        assert manager.get(f"settings.{key}") is None

        results = runner.invoke(config_set_app, args=[key, value, "--path", file])
        manager.reload_all()

        assert results.exit_code == 0
        assert manager["settings", key] == value

    @pytest.mark.standard
    def test_set_existing_value(self, setup_sample_manager):
        manager, file = setup_sample_manager.values()
        key = "test"
        value = "newvalue"

        results = runner.invoke(config_set_app, args=[key, value, "--path", file])
        manager.reload_all()

        assert results.exit_code == 0
        assert manager["settings", key] == value

    @pytest.mark.edge
    def test_set_empty_string(self, generate_test_config):
        manager, file = generate_test_config.values()

        results = runner.invoke(config_set_app, args=["test", "", "--path", file])
        manager.reload_all()

        assert results.exit_code == 1
        assert results.output == 'Could not parse the value ""\n'

    @pytest.mark.standard
    @pytest.mark.parametrize(
        "value",
        (
            "[0, 1, 2]",
            "(0, 1, 2)",
            "{0, 1, 2}",
            "['a', 'b', 'c']",
            "('a', 'b', 'c')",
            "{'a', 'b', 'c'}",
            '[{"a": 1, "b": 2}, {"c": 3, "d": 4}]',
        ),
    )
    def test_set_sequence_values(self, generate_test_config, value):
        manager, file = generate_test_config.values()
        key = "test"

        results = runner.invoke(config_set_app, args=[key, value, "--path", file])
        manager.reload_all()

        assert manager.get(f"settings.{key}") is not None

        read_value = manager["settings", key]

        assert results.exit_code == 0
        assert isinstance(read_value, BoxList)

    @pytest.mark.standard
    @pytest.mark.parametrize(
        "value", ("true", "false", "True", "False", "TRUE", "FALSE")
    )
    def test_set_boolean_values(self, generate_test_config, value):
        manager, file = generate_test_config.values()
        key = "test"

        results = runner.invoke(config_set_app, args=[key, value, "--path", file])
        manager.reload_all()

        assert manager.get(f"settings.{key}") is not None

        read_value = manager["settings", key]

        assert results.exit_code == 0
        assert isinstance(read_value, bool)

    @pytest.mark.standard
    @pytest.mark.parametrize("value", ("0", "2", "69", "818", "6128", "85195091098098"))
    def test_set_positive_integer_values(self, generate_test_config, value):
        manager, file = generate_test_config.values()
        key = "test"

        results = runner.invoke(config_set_app, args=[key, value, "--path", file])
        manager.reload_all()

        assert manager.get(f"settings.{key}") is not None

        read_value = manager["settings", key]

        assert results.exit_code == 0
        assert isinstance(read_value, int)

    @pytest.mark.standard
    @pytest.mark.parametrize("value", ("-1", "-28", "-351", "-6815", "-1298091902859"))
    def test_set_negative_integer_values(self, generate_test_config, value):
        manager, file = generate_test_config.values()
        key = "test"

        results = runner.invoke(config_set_app, args=[key, "--path", file, "--", value])
        manager.reload_all()

        assert manager.get(f"settings.{key}") is not None

        read_value = manager["settings", key]

        assert results.exit_code == 0
        assert isinstance(read_value, int)

    @pytest.mark.standard
    @pytest.mark.parametrize(
        "value",
        (
            "0.0",
            "0.05",
            "81.098088",
            "1518e3",
            "1.81889e15",
            "151.8189E7",
            "0.181809E12",
            "1.81889e-15",
            "0.181809E-12",
        )
    )
    def test_set_positive_float_values(self, generate_test_config, value):
        manager, file = generate_test_config.values()
        key = "test"

        results = runner.invoke(config_set_app, args=[key, value, "--path", file])
        manager.reload_all()

        assert manager.get(f"settings.{key}") is not None

        read_value = manager["settings", key]

        assert results.exit_code == 0
        assert isinstance(read_value, float)

    @pytest.mark.standard
    @pytest.mark.parametrize(
        "value",
        (
            "-0.05",
            "-81.098088",
            "-1518e3",
            "-1.81889e15",
            "-151.8189E7",
            "-0.181809E12",
            "-1.81889e-15",
            "-0.181809E-12",
        )
    )
    def test_set_negative_float_values(self, generate_test_config, value):
        manager, file = generate_test_config.values()
        key = "test"

        results = runner.invoke(config_set_app, args=[key, "--path", file, "--", value])
        manager.reload_all()

        assert manager.get(f"settings.{key}") is not None

        read_value = manager["settings", key]

        assert results.exit_code == 0
        assert isinstance(read_value, float)

    @pytest.mark.edge
    @pytest.mark.parametrize(
        "value",
        (
            "-1",
            "-28",
            "-351",
            "-6815",
            "-1298091902859",
            "-0.05",
            "-81.098088",
            "-1518e3",
            "-1.81889e15",
            "-151.8189E7",
            "-0.181809E12",
            "-1.81889e-15",
            "-0.181809E-12",
        ),
    )
    def test_set_invalid_negative_numbers(self, generate_test_config, value):
        manager, file = generate_test_config.values()
        key = "test"

        results = runner.invoke(config_set_app, args=[key, value, "--path", file])
        manager.reload_all()

        assert results.exit_code == 2

    @pytest.mark.edge
    @pytest.mark.parametrize("value", ("1f", "1.0x100"))
    def test_set_near_numeric_value(self, generate_test_config, value):
        manager, file = generate_test_config.values()
        key = "test"

        results = runner.invoke(config_set_app, args=[key, value, "--path", file])
        manager.reload_all()

        assert manager.get(f"settings.{key}") is not None

        read_value = manager["settings", key]

        assert results.exit_code == 0
        assert isinstance(read_value, str)

    @pytest.mark.standard
    def test_set_dict_values(self, generate_test_config):
        manager, file = generate_test_config.values()
        key = "test"
        value = '{"a": 0, "b": 1}'

        results = runner.invoke(config_set_app, args=[key, value, "--path", file])
        manager.reload_all()

        assert manager.get(f"settings.{key}") is not None

        read_value = manager["settings", key]

        assert results.exit_code == 0
        assert isinstance(read_value, dict)

    @pytest.mark.edge
    @pytest.mark.parametrize(
        "value",
        (
            "[1, 2",
            "(1, 2",
            "{1, 2",
            "['a', 'b'",
            "('a', 'b'",
            "{'a', 'b'",
            "{'a', 'b'",
            "{'a': 0",
        ),
    )
    def test_malformed_collection(self, generate_test_config, value):
        manager, file = generate_test_config.values()

        results = runner.invoke(config_set_app, args=["test", value, "--path", file])
        manager.reload_all()

        assert results.exit_code == 1
        assert results.output == f'Could not parse the value "{value}"\n'


@pytest.mark.cli
@pytest.mark.config
class TestExtendCommand:
    @pytest.mark.standard
    def test_extend_without_creating(self, generate_test_config):
        manager, file = generate_test_config.values()
        key = "test"
        value = "newvalue"

        results = runner.invoke(config_extend_app, args=[key, value, "--path", file])
        manager.reload_all()

        msg = (
            f"Setting `{key}` was not found, if you wish to update the configuration, "
            "run the command with the `--create-on-missing` option\n"
        )

        assert results.exit_code == 1
        assert results.output == msg

    @pytest.mark.standard
    def test_extend_with_creating(self, generate_test_config):
        manager, file = generate_test_config.values()
        key = "test"
        value = "newvalue"

        results = runner.invoke(
            config_extend_app, args=[key, value, "--create-on-missing", "--path", file]
        )
        manager.reload_all()

        assert manager.get(f"settings.{key}") is not None

        read_value = manager["settings", key]

        assert results.exit_code == 0
        assert isinstance(read_value, BoxList)
        assert len(read_value) == 1
        assert read_value[-1] == value

    @pytest.mark.standard
    @pytest.mark.parametrize("flag", (True, False))
    def test_extend_existing_key(self, generate_test_config, flag):
        manager, file = generate_test_config.values()
        key = "test"
        value = "newvalue"

        manager["settings", key] = [0, 1, 2]
        manager.save_all()

        assert isinstance(manager["settings", key], list)

        if flag:
            results = runner.invoke(
                config_extend_app,
                args=[key, value, "--create-on-missing", "--path", file],
            )

        else:
            results = runner.invoke(
                config_extend_app, args=[key, value, "--path", file]
            )

        manager.reload_all()

        assert manager.get(f"settings.{key}") is not None

        read_value = manager["settings", key]

        assert results.exit_code == 0
        assert isinstance(read_value, BoxList)
        assert len(read_value) == 4
        assert read_value[-1] == value

    @pytest.mark.edge
    @pytest.mark.parametrize("flag", (True, False))
    def test_extend_scalar_value(self, setup_sample_manager, flag):
        manager, file = setup_sample_manager.values()
        key = "test"
        value = "newvalue"

        if flag:
            results = runner.invoke(
                config_extend_app,
                args=[key, value, "--create-on-missing", "--path", file],
            )

        else:
            results = runner.invoke(
                config_extend_app, args=[key, value, "--path", file]
            )

        manager.reload_all()

        current_value = manager["settings", key]

        msg = (
            f"To extend settings, the value for `{key}` must be an array, got "
            f"{current_value} instead\n"
        )

        assert results.exit_code == 1
        assert results.output == msg

    @pytest.mark.edge
    @pytest.mark.parametrize("flag", (True, False))
    def test_extend_empty_string(self, generate_test_config, flag):
        manager, file = generate_test_config.values()
        key = "test"

        manager["settings", key] = [0, 1, 2]
        manager.save_all()

        assert isinstance(manager["settings", key], list)

        if flag:
            results = runner.invoke(
                config_extend_app, args=[key, "", "--create-on-missing", "--path", file]
            )

        else:
            results = runner.invoke(config_extend_app, args=[key, "", "--path", file])

        manager.reload_all()

        assert results.exit_code == 1
        assert results.output == 'Could not parse the value ""\n'


@pytest.mark.cli
@pytest.mark.config
@pytest.mark.standard
class TestUnsetCommand:
    def test_unset_existing_value(self, setup_sample_manager):
        manager, file = setup_sample_manager.values()
        key = "test"

        results = runner.invoke(config_unset_app, args=[key, "--path", file])
        manager.reload_all()

        assert manager.get(f"settings.{key}") is None
        assert results.exit_code == 0

    def test_unset_non_existing_value(self, setup_sample_manager):
        manager, file = setup_sample_manager.values()

        results = runner.invoke(config_unset_app, args=["notest", "--path", file])
        manager.reload_all()

        assert results.exit_code == 1
        assert results.exc_info[0] is SettingNotFoundError
{%- endif %}
