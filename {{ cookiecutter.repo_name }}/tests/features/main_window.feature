@frontend
Feature: Main window

  @standard
  Scenario: Quit the interface
    Given the interface is running
    When the user presses "Ctrl+Q"
    Then the application exits without errors
