{% raw -%}
---
tags:
  - Development Guides
  - Workflows
---

{% endraw -%}
# Continuous Integration
<!-- This section is also described in CONTRIBUTING.md
  [link]: ../../../../CONTRIBUTING.md#continuous-integration

  REMEMBER TO MIRROR ANY CHANGES ON BOTH FILES
-->

Besides being hosted in {{ cookiecutter.__scm_platform_base }},
{%- if cookiecutter.__scm_platform_lc == 'gitlab' %}
{{ cookiecutter.project_name }} uses [GitLab CI][1]
{%- else %}
{{ cookiecutter.project_name }} uses [GitHub Actions][1]
{%- endif %}
to automate the following development streams:

- Testing;
- Test coverage reporting;
{%- if cookiecutter.__coverage_lc == 'codacy' %}
- Code quality analysis;
{%- endif %}
- Releases.

{{ cookiecutter.__mr_term }}s can not be completed
unless its CI pipeline passes.
The project's CI configuration
runs under more strict rules
and no jobs are allowed to fail.
{%- if cookiecutter.__coverage_lc == 'codacy' %}
This includes the external job
provided by [Codacy][1a],
which is used for code quality assurance.
Take a look at the [Pull Requests][1b] page for {{ cookiecutter.project_name }}
for further information
on reasons
why a PR Quality Review job
might have failed.
{%- endif %}

Developers should be familiar
{%- if cookiecutter.__scm_platform_lc == 'gitlab' %}
with the [GitLab CI syntax][2]
{%- else %}
with the [GitHub Actions syntax][2]
{%- endif %}
to effectively contribute
with further automation
of the development cycle.

<!-- Anchors -->
{%- if cookiecutter.__scm_platform_lc == 'gitlab' %}

[1]: https://docs.gitlab.com/topics/build_your_application/
{%- else %}

[1]: https://docs.github.com/en/actions/how-tos/deploy/configure-and-manage-deployments/control-deployments
{%- endif %}
{%- if cookiecutter.__coverage_lc == 'codacy' %}
[1a]: https://app.codacy.com/{{ cookiecutter.__scm_platform_redux }}/{{ cookiecutter.scm_namespace }}/{{ cookiecutter.repo_name }}
[1b]: https://app.codacy.com/{{ cookiecutter.__scm_platform_redux }}/{{ cookiecutter.scm_namespace }}/{{ cookiecutter.repo_name }}/pull-requests/open
{%- endif %}
{%- if cookiecutter.__scm_platform_lc == 'gitlab' %}
[2]: https://docs.gitlab.com/ci/yaml/
{%- else %}
[2]: https://docs.github.com/en/actions/how-tos/write-workflows/choose-when-workflows-run/trigger-a-workflow
{%- endif %}
