@backend @config @standard
Feature: Log file parser
  Nebulog allows developers to define custom parsers for reading `.log` files. This
  enables the creation of utilities to take advantage of data stored in the log files
  for analysis purposes. {{ cookiecutter.project_name }} defines a custom log file formatting, along with
  the necessary objects to parse this file.

  Scenario Outline: Parse correct structure
    When the parser reads the structure "2025-10-23 18:56:00.000 | 0:00:00.000000 | <level> | test.py:<line>    | This is a test message for the parser      <logend>"
    Then the regular expression returns a match
    * the regular expression finds 5 groups
    * the first group is equal to "2025-10-23 18:56:00.000"
    * the second group is equal to <level>
    * the third group is equal to "test"
    * the fourth group is equal to <line>
    * the fifth group is equal to "This is a test message for the parser"

    Examples:
      | level    | line  | logend                                              |
      | TRACE    | 1     | ¶                                                   |
      | TRACE    | 10    | ¶                                                   |
      | TRACE    | 1000  | ¶                                                   |
      | TRACE    | 10000 | ¶                                                   |
      | DEBUG    | 1     | ¶                                                   |
      | DEBUG    | 10    | ¶                                                   |
      | DEBUG    | 100   | ¶                                                   |
      | DEBUG    | 1000  | ¶                                                   |
      | INFO     | 1     | ¶                                                   |
      | INFO     | 10    | ¶                                                   |
      | INFO     | 100   | ¶                                                   |
      | INFO     | 1000  | ¶                                                   |
      | SUCCESS  | 1     | ¶                                                   |
      | SUCCESS  | 10    | ¶                                                   |
      | SUCCESS  | 100   | ¶                                                   |
      | SUCCESS  | 1000  | ¶                                                   |
      | WARNING  | 1     | ¶                                                   |
      | WARNING  | 10    | ¶                                                   |
      | WARNING  | 100   | ¶                                                   |
      | WARNING  | 1000  | ¶                                                   |
      | ERROR    | 1     | ¶                                                   |
      | ERROR    | 10    | ¶                                                   |
      | ERROR    | 100   | ¶                                                   |
      | ERROR    | 1000  | ¶                                                   |
      | CRITICAL | 1     | ¶                                                   |
      | CRITICAL | 10    | ¶                                                   |
      | CRITICAL | 100   | ¶                                                   |
      | CRITICAL | 1000  | ¶                                                   |
      | TRACE    | 1     | ¶ {'key': 'somevalue', 'value': 818, 'is_secret': False} |
      | TRACE    | 10    | ¶ {'key': 'somevalue', 'value': 818, 'is_secret': False} |
      | TRACE    | 1000  | ¶ {'key': 'somevalue', 'value': 818, 'is_secret': False} |
      | TRACE    | 10000 | ¶ {'key': 'somevalue', 'value': 818, 'is_secret': False} |
      | DEBUG    | 1     | ¶ {'key': 'somevalue', 'value': 818, 'is_secret': False} |
      | DEBUG    | 10    | ¶ {'key': 'somevalue', 'value': 818, 'is_secret': False} |
      | DEBUG    | 100   | ¶ {'key': 'somevalue', 'value': 818, 'is_secret': False} |
      | DEBUG    | 1000  | ¶ {'key': 'somevalue', 'value': 818, 'is_secret': False} |
      | INFO     | 1     | ¶ {'key': 'somevalue', 'value': 818, 'is_secret': False} |
      | INFO     | 10    | ¶ {'key': 'somevalue', 'value': 818, 'is_secret': False} |
      | INFO     | 100   | ¶ {'key': 'somevalue', 'value': 818, 'is_secret': False} |
      | INFO     | 1000  | ¶ {'key': 'somevalue', 'value': 818, 'is_secret': False} |
      | SUCCESS  | 1     | ¶ {'key': 'somevalue', 'value': 818, 'is_secret': False} |
      | SUCCESS  | 10    | ¶ {'key': 'somevalue', 'value': 818, 'is_secret': False} |
      | SUCCESS  | 100   | ¶ {'key': 'somevalue', 'value': 818, 'is_secret': False} |
      | SUCCESS  | 1000  | ¶ {'key': 'somevalue', 'value': 818, 'is_secret': False} |
      | WARNING  | 1     | ¶ {'key': 'somevalue', 'value': 818, 'is_secret': False} |
      | WARNING  | 10    | ¶ {'key': 'somevalue', 'value': 818, 'is_secret': False} |
      | WARNING  | 100   | ¶ {'key': 'somevalue', 'value': 818, 'is_secret': False} |
      | WARNING  | 1000  | ¶ {'key': 'somevalue', 'value': 818, 'is_secret': False} |
      | ERROR    | 1     | ¶ {'key': 'somevalue', 'value': 818, 'is_secret': False} |
      | ERROR    | 10    | ¶ {'key': 'somevalue', 'value': 818, 'is_secret': False} |
      | ERROR    | 100   | ¶ {'key': 'somevalue', 'value': 818, 'is_secret': False} |
      | ERROR    | 1000  | ¶ {'key': 'somevalue', 'value': 818, 'is_secret': False} |
      | CRITICAL | 1     | ¶ {'key': 'somevalue', 'value': 818, 'is_secret': False} |
      | CRITICAL | 10    | ¶ {'key': 'somevalue', 'value': 818, 'is_secret': False} |
      | CRITICAL | 100   | ¶ {'key': 'somevalue', 'value': 818, 'is_secret': False} |
      | CRITICAL | 1000  | ¶ {'key': 'somevalue', 'value': 818, 'is_secret': False} |
