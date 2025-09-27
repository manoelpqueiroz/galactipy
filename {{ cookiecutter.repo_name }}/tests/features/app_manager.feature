Feature: Application Manager

  Scenario: Manage at runtime
    When the user calls a manager
    Then the manager object is empty
    And the base directory points to the user config path

  Rule: There are only settings and secrets

    Scenario Outline: Call default manager
      When the user calls the default manager
      Then both "settings" and "secrets" are accessible
      And the <configuration_type> environment variable prefix matches the <expected_envvar> value

      Examples:
        | configuration_type | expected_envvar       |
        | settings           | {{ cookiecutter.__envvar }}        |
        | secrets            | {{ cookiecutter.__envvar }}_SECRET |

    Scenario Outline: Call custom manager
      Given an existing configuration file outside the user config path
      When the user calls a custom manager <configuration_type>
      Then only the <configuration_type> domain is accessible
      And the <configuration_type> environment variable prefix matches the <expected_envvar> value

      Examples:
        | configuration_type | expected_envvar       |
        | settings           | {{ cookiecutter.__envvar }}        |
        | secrets            | {{ cookiecutter.__envvar }}_SECRET |
