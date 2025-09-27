@cli @config
Feature: Command-line configuration program

  Background:
    Given a valid configuration file

  Rule: Getting values
    Background:
      Given the configuration has a "test" key with a value of "somevalue"

    @standard
    Scenario: Get the entire configuration
      When the get program receives no arguments
      Then the terminal prints the entire configuration as a dictionary
      And the program exits without errors

    @standard
    Scenario: Get a specific configuration value
      When the get program receives the "test" key
      Then the terminal prints "somevalue" to the user
      And the program exits without errors

    @standard
    Scenario: Get an invalid configuration value
      When the get program receives the "notest" key
      Then the program raises a key error
      And the program exits with status 1

  Rule: Setting values
    @standard
    Scenario: Set a new value
      Given the key "test" does not exist in the configuration
      When the set program receives the "test" key with "newvalue" value
      Then the configuration adds a new key "test" with value "newvalue"
      And the program exits without errors

    @standard
    Scenario: Override an existing value
      Given the configuration has a "test" key with a value of "somevalue"
      When the set program receives the "test" key with "newvalue" value
      Then the configuration replaces the value for the "test" key with "newvalue"
      And the program exits without errors

    @edge
    Scenario: Set empty string
      When the set program receives the key "test" with an empty string
      Then the terminal shows a "Could not parse the value" message
      And the program exits with status 1

    @standard
    Scenario Outline: Set a sequence value
      When the set program receives the "test" key and value <value_argument>
      Then the key "test" becomes available in the configuration
      * the value for "test" is of a list type
      * the program exits without errors

      Examples:
        | value_argument                       |
        | [0, 1, 2]                            |
        | (0, 1, 2)                            |
        | ['a', 'b', 'c']                      |
        | ('a', 'b', 'c')                      |
        | [{"a": 1, "b": 2}, {"c": 3, "d": 4}] |

    @standard
    Scenario Outline: Set a boolean value
      When the set program receives the "test" key and value <value_argument>
      Then the key "test" becomes available in the configuration
      * the value for "test" is of a boolean type
      * the program exits without errors

      Examples:
        | value_argument |
        | true           |
        | false          |
        | True           |
        | False          |
        | TRUE           |
        | FALSE          |

    @standard
    Scenario Outline: Set a mapping value
      When the set program receives the "test" key and value <value_argument>
      Then the key "test" becomes available in the configuration
      * the value for "test" is of a dictionary type
      * the program exits without errors

      Examples:
        | value_argument   |
        | {"a": 0, "b": 1} |

  Rule: Extending list values
    @standard
    Scenario: Extend non-existing key without creating
      Given the key "test" does not exist in the configuration
      When the extend program receives the key "test" and "newvalue" value with the `--create-on-missing` option set to <flag>
      Then the terminal shows a message mentioning "test" was not found
      And the program exits with status 1

      Examples:
        | flag  |
        | False |

    @standard
    Scenario: Create array key
      Given the key "test" does not exist in the configuration
      When the extend program receives the key "test" and "newvalue" value with the `--create-on-missing` option set to <flag>
      Then the key "test" becomes available in the configuration
      * the value for "test" is of a list type
      * the value for "test" has <length> elements
      * the last element for "test" is equal to "newvalue"
      * the program exits without errors

      Examples:
        | flag | length |
        | True | 1      |

    @standard
    Scenario Outline: Extend existing key
      Given the configuration has a "test" key with a list type value
      And the value for "test" has <initial_length> elements
      When the extend program receives the key "test" and "newvalue" value with the `--create-on-missing` option set to <flag>
      Then the value for "test" has <final_length> elements
      * the last element for "test" is equal to "newvalue"
      * the program exits without errors

      Examples:
        | flag  | initial_length | final_length |
        | True  | 3              | 4            |
        | False | 3              | 4            |

    @edge
    Scenario Outline: Extend a scalar value
      Given the configuration has a "test" key with a value of "somevalue"
      When the extend program receives the key "test" and "newvalue" value with the `--create-on-missing` option set to <flag>
      Then the terminal shows a message mentioning "test" must be an array
      And the program exits with status 1

      Examples:
        | flag  |
        | True  |
        | False |

    @edge
    Scenario: Extend with empty string
      Given the configuration has a "test" key with a list type value
      When the extend program receives the key "test" with an empty string and the `--create-on-missing` option set to <flag>
      Then the terminal shows a "Could not parse the value" message

      Examples:
        | flag  |
        | True  |
        | False |

  @standard
  Rule: Unsetting values
    Background:
      Given the configuration has a "test" key with a value of "somevalue"

    Scenario: Unset a valid top-level value
      When the unset program receives the key "test"
      Then the key "test" is removed from the configuration
      And the program exits without errors

    Scenario: Unset a non-existing value
      When the unset program receives the key "notest"
      Then the program raises a setting not found error
      And the program exits with status 1
