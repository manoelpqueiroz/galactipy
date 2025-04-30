Feature: Command-line interface

  Scenario: Invoke with version argument
    When the program is called with the `--version` argument
    Then the program's version is displayed
    And the program is terminated without errors

  # TODO replace scenario when new commands are added to the CLI
  Scenario: Invoke any command
    When the program is called with the <invalid> command
    Then the program is terminated with status 2

    Examples:
      | invalid |
      |     any |
      |    some |
      | testing |
      |    help |
      |     run |
