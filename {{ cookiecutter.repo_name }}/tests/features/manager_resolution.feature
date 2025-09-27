@backend @config
Feature: Resolve application manager definitions
  The AppManager class allows for both the default configuration or a custom
  configuration to be provided for the application. In real-case scenarios, there is
  always an interplay between the configuration type and whether the default files or a
  custom file is used for a specific configuration type.

  This interplay must be resolved before the configuration in question is called.

  @standard
  Scenario Outline: Application resolution
    When the resolver receives a request with <is_secret> and <uses_custom_path>
    Then it returns a manager with <manager_length> domains
    * a string with <configuration_type> value
    * validating the <configuration_type> file inside the base directory is <file_in_base_dir>

    Examples:
      | is_secret | uses_custom_path | configuration_type | manager_length | file_in_base_dir |
      | False     | False            | settings           | 2              | True             |
      | True      | False            | secrets            | 2              | True             |
      | False     | True             | settings           | 1              | False            |
      | True      | True             | secrets            | 1              | False            |
