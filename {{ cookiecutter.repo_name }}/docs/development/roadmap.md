# Roadmap

<!-- RECORD your project mission, in tandem with the "Purpose & Function" section on README.md -->

Our roadmap serves to make
the overall trajectory of the project
transparent to our users
and to help us
prioritise high-value items
to work on.
Rather than promising concrete dates,
we prefer to make our work visible
so you can track progress
and position yourself on long-term plans
should you wish to contribute
with their discussion.

Most roadmap items are gathered
from the community
or include a feedback loop
with the community.
For complete details,
including discussion history
and delivered items,
{%- if cookiecutter.scm_platform == 'GitLab Premium/Ultimate' %}
please refer to the [GitLab Epics][1]
{%- elif cookiecutter.scm_platform == 'GitLab Free' %}
please refer to the [GitLab Milestones][1]
{%- else %}
please refer to the [GitHub Projects][1]
{%- endif %}
at our repository.

!!! info

    The items on this roadmap
    do not have a strict ordering
    or implied dates of completion.

## Development Stages and Features

![Project stage][2]

{{ cookiecutter.project_name }} is currently in the
**Planning** stage,
seeking contributors
to help refine
its foundational features
while laying out the thresholds
for each stage of development.

<!-- RECORD relevant information to divulge to the community -->

### :lucide-line-squiggle: Pre-Alpha Stage

<!-- RECORD the features and capabilities the library will offer at the pre-alpha stage -->

### :lucide-bean: Alpha Stage

<!-- RECORD the features and capabilities the library will offer at the alpha stage -->

### :lucide-sprout: Beta Stage

<!-- RECORD the features and capabilities the library will offer at the beta stage -->

### :lucide-tree-pine: Stable Release

<!-- RECORD the features and capabilities the library will offer for it to be considered stable -->

### :lucide-infinity: Project Maturation

<!-- RECORD the features and capabilities that will lead the project's capabilities beyond what is currently expected for a stable release -->

<!-- Anchors -->

{% if cookiecutter.scm_platform == 'GitLab Premium/Ultimate' -%}
[1]: {{ cookiecutter.__gitlab_org }}/epics
{% elif cookiecutter.scm_platform == 'GitLab Free' -%}
[1]: {{ cookiecutter.__scm_link_url }}/milestones
{% else -%}
[1]: {{ cookiecutter.__scm_link_url }}/projects
{% endif -%}
[2]: https://img.shields.io/pypi/status/{{ cookiecutter.repo_name }}?style=for-the-badge&logo=theplanetarysociety&label=stage
