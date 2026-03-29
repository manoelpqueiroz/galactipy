# Development Setup

To start contributing to {{ cookiecutter.project_name }},
you should start
by [forking][1] the upstream repository
to your own {{ cookiecutter.__scm_platform_base }} [group][2].
We manage contributions
{%- if cookiecutter.licence != 'nos' %}
from the community
{%- endif %}
through the [fork][3] system,
which helps us
monitor and appreciate continuous input
from individuals and organisations.
{%- if cookiecutter.licence != 'nos' %}
Contributors who can
demonstrate their competence
in further developing {{ cookiecutter.project_name }}
may be [promoted][3a]
to upstream Developers or Maintainers.
{%- endif %}

After forking the upstream repository,
cloning it to your local environment
and accessing the root dir
via your IDE or the terminal:

1. Make sure
   you have Poetry [installed][4];
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
for a [first contribution][5].

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
{%- if cookiecutter.licence != 'nos' %}
[3a]: #contributor-promotion
{%- endif %}
[4]: https://python-poetry.org/docs/#installation
[5]: #development-workflow
