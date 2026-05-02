{% raw -%}
---
tags:
  - Development Guides
  - Workflows
---

{% endraw -%}
# Checks & Hooks
<!-- This section is also described in CONTRIBUTING.md
  [link]: ../../../../CONTRIBUTING.md#checks--hooks

  REMEMBER TO MIRROR ANY CHANGES ON BOTH FILES
-->

Before pushing local changes
to the repository,
developers should run
content integrity
through two possible routes:

- Locally running tests,
  checking codestyle
  and static typing
  using [Invoke tasks][1]
  – especially the `invoke sweep` command –
  before committing;
  this is manually run
  by the developer;
- Pass all validations
  set up in our [Pre-Commit configuration][2]
  before committing
  or pushing the changes;
  this is automatically run
  once the hooks are installed
  after setting the [development environment][3].

The pre-commit hooks are configured
to expect the following:

- All files must comply to the [POSIX][4] standard,
  except licence-related files;
- Syntax for TOML, YAML and JSON files
  must contain no errors;
- Pure JSON files must have an indentation of `2` spaces;
- JSON files for
{%- if cookiecutter.__scm_platform_lc == 'gitlab' %}
  GitLab CI
{%- else %}
  GitHub Issue templates,
  issue configuration,
  GitHub Actions workflows
  and Dependabot configuration
{%- endif %}
  must adhere to
  their respective JSON schema;
- There must be no merge conflict identifiers
  in the files
  (e.g.,
  `<<<<<<< HEAD`,
  `=======`,
  etc.);
{%- if cookiecutter.version_schema == 'trunkver' %}
- All unit tests must pass;
- Test coverage must be above the threshold
  defined in `pyproject.toml`;
- No security issues should be found
  by running [Bandit][4a];
{%- endif %}
- Type checking must not find any inconsistencies
  in type annotations;
- Code files must comply with
  both the Ruff linter
  and formatter;
- Code files must be properly marked
  with a copyright notice;
{%- if cookiecutter.commit_convention == 'conventional' %}
- Commit messages must comply
  with the [Conventional Commits][4x] convention;
{%- elif cookiecutter.commit_convention == 'conventional-gitmoji' %}
- Commit messages must comply
  with the [Conventional Gitmoji][4x] convention;
{%- endif %}
- The `pyproject.toml` must have no inconsistencies;
- The `poetry.lock` file must be updated;
- The pre-commit hooks themselves
  must be configured
  to use their latest available version.

Any updates that do not comply
with these rules will be blocked.

<!-- Anchors -->

[1]: ../for_developers/workflow/invoke.md
[2]: {{ cookiecutter.__scm_repo_latch }}/blob/master/.pre-commit-config.yaml
[3]: ../development_setup.md
[4]: https://pubs.opengroup.org/onlinepubs/9699919799/basedefs/V1_chap03.html#tag_03_206
{%- if cookiecutter.version_schema == 'trunkver' %}
[4a]: https://bandit.readthedocs.io/en/latest/
{%- endif %}
{%- if cookiecutter.commit_convention == 'conventional' %}
[4x]: ./committing.md#conventional-commits
{%- elif cookiecutter.commit_convention == 'conventional-gitmoji' %}
[4x]: ./committing.md#conventional-gitmoji
{%- endif %}
