# Invoke Usage

[`invoke`][1] is a library that
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
and are defined in the [`tasks.py`][2] file.

Changes to the set of tasks
and their behaviour
should be proposed
through a [**Internal Improvement**][3] {{ cookiecutter.__mr_term }}.

## Environment Setup

::: tasks.install
    options:
      heading_level: 3
      show_signature: false
      separate_signature: false

::: tasks.pyproject
    options:
      heading_level: 3
      show_signature: false
      separate_signature: false

::: tasks.update
    options:
      heading_level: 3
      show_signature: false
      separate_signature: false

## Quality Assurance Tasks

::: tasks.codestyle
    options:
      heading_level: 3
      show_signature: false
      separate_signature: false

::: tasks.lint
    options:
      heading_level: 3
      show_signature: false
      separate_signature: false

::: tasks.ruff
    options:
      heading_level: 3
      show_signature: false
      separate_signature: false

::: tasks.mypy
    options:
      heading_level: 3
      show_signature: false
      separate_signature: false

::: tasks.report
    options:
      heading_level: 3
      show_signature: false
      separate_signature: false

::: tasks.security
    options:
      heading_level: 3
      show_signature: false
      separate_signature: false

::: tasks.sweep
    options:
      heading_level: 3
      show_signature: false
      separate_signature: false

## Project Building & Publishing

::: tasks.build
    options:
      heading_level: 3
      show_signature: false
      separate_signature: false

::: tasks.config
    options:
      heading_level: 3
      show_signature: false
      separate_signature: false

::: tasks.publish
    options:
      heading_level: 3
      show_signature: false
      separate_signature: false

{% if cookiecutter.create_docker -%}
## Docker Operations

::: tasks.login
    options:
      heading_level: 3
      show_signature: false
      separate_signature: false

::: tasks.container
    options:
      heading_level: 3
      show_signature: false
      separate_signature: false

::: tasks.push
    options:
      heading_level: 3
      show_signature: false
      separate_signature: false

::: tasks.prune
    options:
      heading_level: 3
      show_signature: false
      separate_signature: false

{% endif -%}
## Cleanup Tasks

::: tasks.remove_cache
    options:
      heading_level: 3
      show_signature: false
      separate_signature: false

::: tasks.remove_dsstore
    options:
      heading_level: 3
      show_signature: false
      separate_signature: false

::: tasks.remove_mypy
    options:
      heading_level: 3
      show_signature: false
      separate_signature: false

::: tasks.remove_ipynb
    options:
      heading_level: 3
      show_signature: false
      separate_signature: false

::: tasks.remove_pytest
    options:
      heading_level: 3
      show_signature: false
      separate_signature: false

::: tasks.remove_ruff
    options:
      heading_level: 3
      show_signature: false
      separate_signature: false

::: tasks.cleanup
    options:
      heading_level: 3
      show_signature: false
      separate_signature: false

::: tasks.remove_build
    options:
      heading_level: 3
      show_signature: false
      separate_signature: false

<!-- Anchors -->

[1]: https://www.pyinvoke.org/
[2]: {{ cookiecutter.__scm_link_url }}/blob/master/tasks.py
{%- if cookiecutter.__scm_platform_lc == 'gitlab' %}
[3]: {{ cookiecutter.__scm_link_url }}/merge_requests/new?issuable_template=Internal%2520Improvements
{%- else %}
[3]: {{ cookiecutter.__scm_link_url }}/pulls/compare?template=internal_improvements.md
{%- endif %}
