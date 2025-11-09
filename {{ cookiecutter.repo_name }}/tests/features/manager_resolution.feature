@backend @config
Feature: Resolve application manager definitions
  The AppManager class allows for both the default configuration or a custom
  configuration to be provided for the application. In real-case scenarios, there is
  always an interplay between the configuration type and whether the default files or a
  custom file is used for a specific configuration type.

  This interplay must be resolved before the configuration in question is called.

  @standard
  Scenario Outline: Application resolution
    When the resolver receives a request with <domain> and <uses_custom_path>
    Then it returns a manager with <manager_length> domains
    And validating the <domain> file inside the base directory is <file_in_base_dir>

    Examples:
      | domain   | uses_custom_path | manager_length | file_in_base_dir |
      | settings | False            | 2              | True             |
      | secrets  | False            | 2              | True             |
      | settings | True             | 1              | False            |
      | secrets  | True             | 1              | False            |
