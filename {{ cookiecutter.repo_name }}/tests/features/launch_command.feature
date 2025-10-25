@cli @frontend @standard
Feature: Command-line launch program

  Scenario: Launch application from CLI
    Given a valid configuration file
    When the launch program receives no arguments
    Then the terminal launches the TUI interface
    And the program exits without errors
