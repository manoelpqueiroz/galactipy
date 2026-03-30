# Development Workflow

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

## Invoke Usage

[`invoke`][2] is a library that
enables easy configuration of
shell-oriented subprocesses
as Python functions.
At {{ cookiecutter.project_name }},
it is our tool of choice
to streamline common operations
developers might perform
during their work,
without requiring them
to memorise complex commands.

Available tasks can be viewed
at anytime
with the `invoke --list` command
and are defined in the [`tasks.py`][3] file.

Changes to the set of tasks
and their behaviour
should be proposed
through a [**Internal Improvement**][4] {{ cookiecutter.__mr_term }}.

### Environment Setup

::: tasks.install
    options:
      heading_level: 4
      show_signature: false
      separate_signature: false

::: tasks.pyproject
    options:
      heading_level: 4
      show_signature: false
      separate_signature: false

::: tasks.update
    options:
      heading_level: 4
      show_signature: false
      separate_signature: false

### Quality Assurance Tasks

::: tasks.codestyle
    options:
      heading_level: 4
      show_signature: false
      separate_signature: false

::: tasks.lint
    options:
      heading_level: 4
      show_signature: false
      separate_signature: false

::: tasks.ruff
    options:
      heading_level: 4
      show_signature: false
      separate_signature: false

::: tasks.mypy
    options:
      heading_level: 4
      show_signature: false
      separate_signature: false

::: tasks.report
    options:
      heading_level: 4
      show_signature: false
      separate_signature: false

::: tasks.security
    options:
      heading_level: 4
      show_signature: false
      separate_signature: false

::: tasks.sweep
    options:
      heading_level: 4
      show_signature: false
      separate_signature: false

### Project Building & Publishing

::: tasks.build
    options:
      heading_level: 4
      show_signature: false
      separate_signature: false

::: tasks.config
    options:
      heading_level: 4
      show_signature: false
      separate_signature: false

::: tasks.publish
    options:
      heading_level: 4
      show_signature: false
      separate_signature: false

{% if cookiecutter.create_docker -%}
### Docker Operations

::: tasks.login
    options:
      heading_level: 4
      show_signature: false
      separate_signature: false

::: tasks.container
    options:
      heading_level: 4
      show_signature: false
      separate_signature: false

::: tasks.push
    options:
      heading_level: 4
      show_signature: false
      separate_signature: false

::: tasks.prune
    options:
      heading_level: 4
      show_signature: false
      separate_signature: false

{% endif -%}
### Cleanup Tasks

::: tasks.remove_cache
    options:
      heading_level: 4
      show_signature: false
      separate_signature: false

::: tasks.remove_dsstore
    options:
      heading_level: 4
      show_signature: false
      separate_signature: false

::: tasks.remove_mypy
    options:
      heading_level: 4
      show_signature: false
      separate_signature: false

::: tasks.remove_ipynb
    options:
      heading_level: 4
      show_signature: false
      separate_signature: false

::: tasks.remove_pytest
    options:
      heading_level: 4
      show_signature: false
      separate_signature: false

::: tasks.remove_ruff
    options:
      heading_level: 4
      show_signature: false
      separate_signature: false

::: tasks.cleanup
    options:
      heading_level: 4
      show_signature: false
      separate_signature: false

::: tasks.remove_build
    options:
      heading_level: 4
      show_signature: false
      separate_signature: false

## Test Markers

When writing tests,
we strongly encourage developers
{%- if cookiecutter.use_bdd %}
to leverage [feature file tags][5]
{%- else %}
to leverage [custom Pytest markers][5]
{%- endif %}
to improve test collection
and organisation.
This allows the team
to get more context
if tests start to fail
after introducing a change.

The following markers are specified
in [`pyproject.toml`][6]:

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
do so through a [**Project Policy Proposal**][7].

## Feature Flags

<!-- RECORD the guidelines on how to implement and handle feature flags -->

<!-- Anchors -->

[1]: ../development_setup.md
[2]: https://www.pyinvoke.org/
[3]: {{ cookiecutter.__scm_link_url }}/blob/master/tasks.py
{% if cookiecutter.__scm_platform_lc == 'gitlab' -%}
[4]: {{ cookiecutter.__scm_link_url }}/merge_requests/new?issuable_template=Internal%2520Improvements
{% else -%}
[4]: {{ cookiecutter.__scm_link_url }}/pulls/compare?template=internal_improvements.md
{% endif -%}
{%- if cookiecutter.use_bdd %}
[5]: https://pytest-bdd.readthedocs.io/en/latest/#organizing-your-scenarios
{%- else %}
[5]: https://docs.pytest.org/en/stable/example/markers.html#mark-examples
{%- endif %}
[6]: {{ cookiecutter.__scm_link_url }}/blob/master/pyproject.toml
{%- if cookiecutter.__scm_platform_lc == 'gitlab' %}
[7]: {{ cookiecutter.__scm_link_url }}/merge_requests/new?issuable_template=Project%2520Policies
{%- else %}
[7]: {{ cookiecutter.__scm_link_url }}/pulls/compare?template=project_policies.md
{%- endif %}
