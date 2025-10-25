@cli @config
Feature: Command-line configuration program

  Background:
    Given a valid configuration file

  Rule: Getting values

    @standard
    Scenario: Get the entire configuration
      Given the configuration contains the key-value pair of "test" and "somevalue"
      When the get program receives no arguments
      Then the program exits without errors
      And the terminal prints the entire configuration as a dictionary

    @standard
    Scenario Outline: Get individual configuration value
      Given the configuration has a "test" key with a value of <value> and type <value_type>
      When the get program receives the "test" key
      Then the program exits without errors
      And the terminal prints <output> to the user

      Examples:
        | value            | output           | value_type |
        | somevalue        | 'somevalue'      | string     |
        | [1, 2, 'a']      | [1, 2, 'a']      | list       |
        | {'a': 1, 'b': 2} | {'a': 1, 'b': 2} | dict       |

    @standard
    Scenario: Get an invalid configuration value
      When the get program receives the "notest" key
      Then the program exits with status 1
      And the program raises a key error

  Rule: Setting values
    @standard
    Scenario: Set a new value
      Given the key "test" does not exist in the configuration
      When the set program receives the "test" key with "newvalue" value
      Then the program exits without errors
      And the configuration adds a new key "test" with value "newvalue"

    @standard
    Scenario: Override an existing value
      Given the configuration contains the key-value pair of "test" and "somevalue"
      When the set program receives the "test" key with "newvalue" value
      Then the program exits without errors
      And the configuration replaces the value for the "test" key with "newvalue"

    @edge
    Scenario: Set empty string
      When the set program receives the key "test" with an empty string
      Then the program exits with status 1
      And the terminal shows a "Could not parse the value """ message

    @standard
    Scenario Outline: Set a sequence value
      When the set program receives the "test" key and value <value_argument>
      Then the program exits without errors
      * the key "test" becomes available in the configuration
      * the value for "test" is of a list type

      Examples:
        | value_argument                       |
        | [0, 1, 2]                            |
        | (0, 1, 2)                            |
        | {0, 1, 2}                            |
        | ['a', 'b', 'c']                      |
        | ('a', 'b', 'c')                      |
        | {'a', 'b', 'c'}                      |
        | [{"a": 1, "b": 2}, {"c": 3, "d": 4}] |

    @standard
    Scenario Outline: Set a boolean value
      When the set program receives the "test" key and value <value_argument>
      Then the program exits without errors
      * the key "test" becomes available in the configuration
      * the value for "test" is of a boolean type

      Examples:
        | value_argument |
        | true           |
        | false          |
        | True           |
        | False          |
        | TRUE           |
        | FALSE          |

    @standard
    Scenario Outline: Set positive integer value
      When the set program receives the "test" key and value <value_argument>
      Then the program exits without errors
      * the key "test" becomes available in the configuration
      * the value for "test" is of an integer type

      Examples:
        | value_argument |
        | 0              |
        | 2              |
        | 69             |
        | 818            |
        | 6128           |
        | 85195091098098 |

    @standard
    Scenario Outline: Set valid negative integer value
      When the set program receives the "test" key and value <value_argument> with a double dash
      Then the program exits without errors
      * the key "test" becomes available in the configuration
      * the value for "test" is of an integer type

      Examples:
        | value_argument |
        | -1             |
        | -28            |
        | -351           |
        | -6815          |
        | -1298091902859 |

    @standard
    Scenario Outline: Set positive float value
      When the set program receives the "test" key and value <value_argument>
      Then the program exits without errors
      * the key "test" becomes available in the configuration
      * the value for "test" is of a float type

      Examples:
        | value_argument |
        | 0.0            |
        | 0.05           |
        | 81.098088      |
        | 1518e3         |
        | 1.81889e15     |
        | 151.8189E7     |
        | 0.181809E12    |
        | 1.81889e-15    |
        | 0.181809E-12   |

    @standard
    Scenario Outline: Set valid negative float value
      When the set program receives the "test" key and value <value_argument> with a double dash
      Then the program exits without errors
      * the key "test" becomes available in the configuration
      * the value for "test" is of a float type

      Examples:
        | value_argument |
        | -0.05          |
        | -81.098088     |
        | -1518e3        |
        | -1.81889e15    |
        | -151.8189E7    |
        | -0.181809E12   |
        | -1.81889e-15   |
        | -0.181809E-12  |

    @edge
    Scenario Outline: Set invalid negative numbers
      When the set program receives the "test" key and value <value_argument>
      Then the program exits with status 2

      Examples:
        | value_argument |
        | -1             |
        | -28            |
        | -351           |
        | -6815          |
        | -1298091902859 |
        | -0.05          |
        | -81.098088     |
        | -1518e3        |
        | -1.81889e15    |
        | -151.8189E7    |
        | -0.181809E12   |
        | -1.81889e-15   |
        | -0.181809E-12  |

    @edge
    Scenario Outline: Set near numeric values
      When the set program receives the "test" key and value <value_argument>
      Then the program exits without errors
      * the key "test" becomes available in the configuration
      * the value for "test" is of a string type

      Examples:
        | value_argument |
        | 1f             |
        | 1.0x100        |

    @standard
    Scenario Outline: Set a mapping value
      When the set program receives the "test" key and value <value_argument>
      Then the program exits without errors
      * the key "test" becomes available in the configuration
      * the value for "test" is of a dictionary type

      Examples:
        | value_argument   |
        | {"a": 0, "b": 1} |

    @edge
    Scenario Outline: Set malformed collection type
      When the set program receives the "test" key and value <value_argument>
      Then the program exits with status 1
      And the terminal shows a "Could not parse the value "<value_argument>"" message

      Examples:
        | value_argument |
        | [1, 2          |
        | (1, 2          |
        | {1, 2          |
        | ['a', 'b'      |
        | ('a', 'b'      |
        | {'a', 'b'      |
        | {'a', 'b'      |
        | {'a': 0        |

  Rule: Extending list values
    @standard
    Scenario: Extend non-existing key without creating
      Given the key "test" does not exist in the configuration
      When the extend program receives the key "test" and "newvalue" value with the `--create-on-missing` option set to <flag>
      Then the program exits with status 1
      And the terminal shows a message mentioning "test" was not found

      Examples:
        | flag  |
        | False |

    @standard
    Scenario: Create array key
      Given the key "test" does not exist in the configuration
      When the extend program receives the key "test" and "newvalue" value with the `--create-on-missing` option set to <flag>
      Then the program exits without errors
      * the key "test" becomes available in the configuration
      * the value for "test" is of a list type
      * the value for "test" has <length> elements
      * the last element for "test" is equal to "newvalue"

      Examples:
        | flag | length |
        | True | 1      |

    @standard
    Scenario Outline: Extend existing key
      Given the configuration has a "test" key with a list type value
      And the value for "test" has <initial_length> elements
      When the extend program receives the key "test" and "newvalue" value with the `--create-on-missing` option set to <flag>
      Then the program exits without errors
      * the value for "test" has <final_length> elements
      * the last element for "test" is equal to "newvalue"

      Examples:
        | flag  | initial_length | final_length |
        | True  | 3              | 4            |
        | False | 3              | 4            |

    @edge
    Scenario Outline: Extend a scalar value
      Given the configuration contains the key-value pair of "test" and "somevalue"
      When the extend program receives the key "test" and "newvalue" value with the `--create-on-missing` option set to <flag>
      Then the program exits with status 1
      And the terminal shows a message mentioning "test" must be an array

      Examples:
        | flag  |
        | True  |
        | False |

    @edge
    Scenario: Extend with empty string
      Given the configuration has a "test" key with a list type value
      When the extend program receives the key "test" with an empty string and the `--create-on-missing` option set to <flag>
      Then the terminal shows a "Could not parse the value <output>" message

      Examples:
        | flag  | output |
        | True  | ""     |
        | False | ""     |

  @standard
  Rule: Unsetting values
    Background:
      Given the configuration contains the key-value pair of "test" and "somevalue"

    Scenario: Unset a valid top-level value
      When the unset program receives the key "test"
      Then the program exits without errors
      And the key "test" is removed from the configuration

    Scenario: Unset a non-existing value
      When the unset program receives the key "notest"
      Then the program exits with status 1
      And the program raises a setting not found error
