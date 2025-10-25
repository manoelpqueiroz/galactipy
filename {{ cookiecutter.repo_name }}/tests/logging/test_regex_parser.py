{%- if cookiecutter.use_bdd %}
from pytest_bdd import given, parsers, scenario, then, when
{% else -%}
import pytest
{%- endif %}

from {{ cookiecutter.package_name }}.logging.parsers import FILE_PARSER


{% if cookiecutter.use_bdd -%}
@scenario("log_parser.feature", "Parse correct structure")
def test_correct_regex():
    pass


@when(
    parsers.parse('the parser reads the structure "{log}"'), target_fixture="log_entry"
)
def get_log_entry(log):
    return log


@then("the regular expression returns a match", target_fixture="regex_groups")
def ensure_regex_match(log_entry):
    match = FILE_PARSER.match(log_entry)

    assert match
    return match.groups()


@then("the regular expression finds 5 groups")
def ensure_capture_length(log_entry):
    assert len(FILE_PARSER.findall(log_entry)[0]) == 5


@then(parsers.parse('the first group is equal to "{timestamp}"'))
def check_first_group(regex_groups, timestamp):
    assert regex_groups[0] == timestamp


@then(parsers.parse("the second group is equal to {level}"))
def check_second_group(regex_groups, level):
    assert regex_groups[1] == level


@then(parsers.parse('the third group is equal to "{file}"'))
def check_third_group(regex_groups, file):
    assert regex_groups[2] == file


@then(parsers.parse("the fourth group is equal to {line}"))
def check_fourth_group(regex_groups, line):
    assert regex_groups[3] == line


@then(parsers.parse('the fifth group is equal to "{message}"'))
def check_fifth_group(regex_groups, message):
    assert regex_groups[4] == message
{%- else %}
@pytest.mark.backend
@pytest.mark.config
@pytest.mark.standard
@pytest.mark.parametrize(
    ("level", "line", "extra"),
    (
        ["TRACE", 1, False],
        ["TRACE", 10, False],
        ["TRACE", 1000, False],
        ["TRACE", 10000, False],
        ["DEBUG", 1, False],
        ["DEBUG", 10, False],
        ["DEBUG", 100, False],
        ["DEBUG", 1000, False],
        ["INFO", 1, False],
        ["INFO", 10, False],
        ["INFO", 100, False],
        ["INFO", 1000, False],
        ["SUCCESS", 1, False],
        ["SUCCESS", 10, False],
        ["SUCCESS", 100, False],
        ["SUCCESS", 1000, False],
        ["WARNING", 1, False],
        ["WARNING", 10, False],
        ["WARNING", 100, False],
        ["WARNING", 1000, False],
        ["ERROR", 1, False],
        ["ERROR", 10, False],
        ["ERROR", 100, False],
        ["ERROR", 1000, False],
        ["CRITICAL", 1, False],
        ["CRITICAL", 10, False],
        ["CRITICAL", 100, False],
        ["CRITICAL", 1000, False],
        ["TRACE", 1, True],
        ["TRACE", 10, True],
        ["TRACE", 1000, True],
        ["TRACE", 10000, True],
        ["DEBUG", 1, True],
        ["DEBUG", 10, True],
        ["DEBUG", 100, True],
        ["DEBUG", 1000, True],
        ["INFO", 1, True],
        ["INFO", 10, True],
        ["INFO", 100, True],
        ["INFO", 1000, True],
        ["SUCCESS", 1, True],
        ["SUCCESS", 10, True],
        ["SUCCESS", 100, True],
        ["SUCCESS", 1000, True],
        ["WARNING", 1, True],
        ["WARNING", 10, True],
        ["WARNING", 100, True],
        ["WARNING", 1000, True],
        ["ERROR", 1, True],
        ["ERROR", 10, True],
        ["ERROR", 100, True],
        ["ERROR", 1000, True],
        ["CRITICAL", 1, True],
        ["CRITICAL", 10, True],
        ["CRITICAL", 100, True],
        ["CRITICAL", 1000, True],
    ),
)
def test_correct_regex(sample_log, level, line, extra):
    logend = (
        "¶ {'key': 'somevalue', 'value': 818, 'is_secret': False}" if extra else "¶"
    )

    log_entry = sample_log.format(level, line, logend)

    match = FILE_PARSER.match(log_entry)
    regex_groups = match.groups()

    assert match
    assert len(FILE_PARSER.findall(log_entry)[0]) == 5

    assert regex_groups[0] == "2025-10-23 18:56:00.000"
    assert regex_groups[1] == level
    assert regex_groups[2] == "test"
    assert regex_groups[3] == str(line)
    assert regex_groups[4] == "This is a test message for the parser"
{%- endif %}
