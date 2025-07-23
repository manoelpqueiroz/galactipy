Feature: Main window

  Scenario: Quit the interface
    Given the interface is running
    When the user presses `Ctrl+Q`
    Then the program is terminated without errors
