{% raw -%}
---
tags:
  - Section Intros
  - Development Guides
  - Workflows
---

{% endraw -%}
# Development Workflow
<!-- This section is also described in CONTRIBUTING.md
  [link]: ../../../../CONTRIBUTING.md#development-workflow

  REMEMBER TO MIRROR ANY CHANGES ON BOTH FILES
-->

After cloning {{ cookiecutter.project_name }}
and following the [development setup][1],
run `invoke test`
(an isolated Pytest task)
and if no errors are raised,
then run `invoke sweep`
(the whole set
of development checks
in a single task).
This step is crucial to ensure
you don't introduce any regressions
as you work on your change.

As a developer,
please be conscious
of crucial steps to validate
before submitting your changes.
A non-exhaustive list of steps to consider:

- Did you add
  or modify unit tests
  if development involved
  changes to the API?
- Did you
  flag the tests
  with the appropriate
  Pytest marks?
- Have you covered
  possible edge cases
  which might not be clear
  on first thought?
- Are all checks passing
  with `invoke sweep`?
{%- if cookiecutter.__coverage_lc == 'codacy' %}
- Did you address
  all issues raised by Codacy
  for the {{ cookiecutter.__mr_term }} branch in question?
{%- endif %}
{%- if cookiecutter.app_type == 'bare_repo' %}
<!-- RECORD common checks developers should make related specifically to your project's public API -->
{%- else %}
- Have any changes been made
  to how the default configuration
  file is structured?
  Can pre-existing user configuration
  still be used
  after these changes
  without crashing the application?
- Do changes secure
  user data integrity,
  without any data losses?
{%- if cookiecutter.__app_group == 'tui' %}
- Have changes been made
  to the frontend components?
  Did you check
  that these changes do not
  degrade,
  corrupt
  or crash
  the user interface?
{%- endif %}
{%- endif %}

## Test Markers
<!-- This section is also described in CONTRIBUTING.md
  [link]: ../../../../CONTRIBUTING.md#test-markers

  REMEMBER TO MIRROR ANY CHANGES ON BOTH FILES
-->

When writing tests,
we strongly encourage developers
{%- if cookiecutter.use_bdd %}
to leverage [feature file tags][2]
{%- else %}
to leverage [custom Pytest markers][2]
{%- endif %}
to improve test collection
and organisation.
This allows the team
to get more context
if tests start to fail
after introducing a change.

The following markers are specified
in [`pyproject.toml`][3]:

|     Marker      | Specification                                                                                                                   |
| :-------------: | ------------------------------------------------------------------------------------------------------------------------------- |
|    `backend`    | Tests validating the behaviour of back end components.                                                                          |
|   `frontend`    | Tests validating the behaviour of the user-facing components.                                                                   |
{%- if cookiecutter.app_type != 'bare_repo' %}
|      `cli`      | Tests validating command-line interface behaviour.                                                                              |
{%- endif %}
|   `standard`    | Tests defining behaviour for program operations considered the standard procedure.                                              |
|  `validation`   | Tests related to data input validation and handling.                                                                            |
|     `edge`      | Tests defining the expected behaviour of the program in edge cases.                                                             |
|   `security`    | Tests validating security aspects of the program.                                                                               |
|  `performance`  | Tests aimed at certifying expected performance from program operations, usually against benchmarks.                             |
|  `persistence`  | Tests which certify that data is consistently and correctly persisted.                                                          |
|    `config`     | Tests related to modifications in user configuration for the program.                                                           |
| `customization` | Tests related to customization options.                                                                                         |
| `compatibility` | Tests validating compatibility of {{ cookiecutter.project_name }} across its different versions.                                |
|     `async`     | Tests validating asynchronous code.                                                                                             |
|  `integration`  | Tests certifying integration with external services, libraries and platforms.                                                   |
|   `database`    | Tests specifically aimed at validating database operations.                                                                     |
|      `api`      | Tests validating integration with external API schemas.                                                                         |
|   `identity`    | Tests related to user identity verification and validation.                                                                     |
|  `networking`   | Tests validating expected connection standards and quality to other services, whether internal or external.                     |
|  `monitoring`   | Tests certifying that program healthchecks provide the necessary information to external systems and files in case of failures. |

To propose changes
to the marker options,
do so through a [**Project Policy Proposal**][4].

## Feature Flags
<!-- This section is also described in CONTRIBUTING.md
  [link]: ../../../../CONTRIBUTING.md#feature-flags

  REMEMBER TO MIRROR ANY CHANGES ON BOTH FILES
-->

<!-- RECORD the guidelines on how to implement and handle feature flags -->

<!-- Anchors -->

[1]: ../development_setup.md
{%- if cookiecutter.use_bdd %}
[2]: https://pytest-bdd.readthedocs.io/en/latest/#organizing-your-scenarios
{%- else %}
[2]: https://docs.pytest.org/en/stable/example/markers.html#mark-examples
{%- endif %}
[3]: {{ cookiecutter.__scm_link_url }}/blob/master/pyproject.toml
{%- if cookiecutter.__scm_platform_lc == 'gitlab' %}
[4]: {{ cookiecutter.__scm_link_url }}/merge_requests/new?issuable_template=Project%2520Policies
{%- else %}
[4]: {{ cookiecutter.__scm_link_url }}/pulls/compare?template=project_policies.md
{%- endif %}
