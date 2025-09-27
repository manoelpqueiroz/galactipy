@cli
Feature: Command-line interface

  @standard
  Scenario: Check program version
    When the root program receives the `--version` option
    Then the terminal displays the program's version
    And the program exits without errors

  @edge
  Scenario Outline: Call invalid command
    When the <command> program receives no arguments
    Then the program exits with status 2

    Examples:
      | command |
      |     any |
      |    some |
      | testing |
      |    help |
      |     run |

  # UPDATEME when new command groups are added to the CLI
  @standard
  Scenario Outline: Call valid command group
    When the <command> program receives no arguments
    Then the terminal displays the help menu for <command>
    And the program exits without errors

    Examples:
      | command |
      | config  |
