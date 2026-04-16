{% raw -%}
---
tags:
  - Setup
  - Development Guides
---

{% endraw -%}
# Development Setup
{%- if cookiecutter.scm_platform == 'GitLab Premium/Ultimate' %}
<!-- This section is also described in project and group CONTRIBUTING.md guides
  [project]: ../../../../CONTRIBUTING.md#development-setup
  [group]: {{ cookiecutter.__contributing_prefix }}#development-setup

  REMEMBER TO INCORPORATE CHANGES FROM BOTH GUIDES WHEN UPDATING THIS FILE
-->
{%- else %}
<!-- This section is also described in CONTRIBUTING.md
  [link]: ../../../../CONTRIBUTING.md#development-setup

  REMEMBER TO MIRROR ANY CHANGES ON BOTH FILES
-->
{%- endif %}

To start contributing to {{ cookiecutter.project_name }},
you should start
by [forking][1] the upstream repository
to your own {{ cookiecutter.__scm_platform_base }} [group][2].
We manage contributions
from the community
through the [fork][3] system,
which helps us
monitor and appreciate continuous input
from individuals and organisations.
Contributors who can
demonstrate their competence
in further developing {{ cookiecutter.project_name }}
may be [promoted][4]
to upstream Developers or Maintainers.

After forking the upstream repository,
cloning it to your local environment
and accessing the root dir
via your IDE or the terminal:

1. Make sure
   you have Poetry [installed][5];
2. Create and activate
   your virtual environment:

```sh
poetry env use 3.14 # Or replace with your Python version
eval $(poetry env activate)
```

3. Install the project's dependencies:

```sh
poetry install # Or, preferably, `invoke install` if available
invoke hooks
```

{% if cookiecutter.version_schema == 'trunkver' -%}
!!! danger

    Installing the pre-commit hooks is crucial,
    as the CI pipelines depend on tasks run
    before pushing to the upstream repository
    to publish test coverage.

    ***Do not skip this step.***

{% endif -%}
4. Run the sweeping task
   with Invoke
   and check output:

```sh
invoke sweep
```

If everything passes,
you're good to go!
Otherwise,
something is not right
and there might be an opportunity
for a [first contribution][6].

<!-- Anchors -->
{%- if cookiecutter.__scm_platform_lc == 'gitlab' %}

[1]: {{ cookiecutter.__scm_link_url }}/forks/new
[2]: https://docs.gitlab.com/user/group/
[3]: https://docs.gitlab.com/user/project/repository/forking_workflow/
{%- else %}

[1]: {{ cookiecutter.__scm_link_url }}/fork
[2]: https://docs.github.com/en/organizations/collaborating-with-groups-in-organizations/about-organizations
[3]: https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo
{%- endif %}
[4]: ./policies/developing.md#contributor-promotion
[5]: https://python-poetry.org/docs/#installation
[6]: ./for_developers/workflow/index.md
