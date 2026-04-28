{% raw -%}
---
tags:
  - For Your Information
  - Living Docs
---

{% endraw -%}
# Roadmap
<!-- This section is also described in ROADMAP.md with a different presentation
  [link]: ../../../../ROADMAP.md#project-mission

  REMEMBER TO MIRROR ANY CHANGES ON BOTH FILES, ADAPTING TO THE RESPECTIVE MEDIUM
-->

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
{%- if cookiecutter.__scm_platform_group == 'glab-paid' %}
please refer to the [GitLab Epics][1]
{%- elif cookiecutter.__scm_platform_group == 'glab-free' %}
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
<!-- This section is also described in ROADMAP.md
  [link]: ../../../../ROADMAP.md#development-stages

  REMEMBER TO MIRROR ANY CHANGES ON BOTH FILES
-->

![Project stage][2]

{{ cookiecutter.project_name }} is currently in the
**Planning** stage,
seeking contributors
to help refine
its foundational features
while laying out the thresholds
for each stage of development.

<!-- RECORD relevant information to divulge to the community

### :lucide-line-squiggle: Pre-Alpha Stage
<!-- This section is also described in ROADMAP.md
  [link]: ../../../../ROADMAP.md#pre-alpha-stage

  REMEMBER TO MIRROR ANY CHANGES ON BOTH FILES

<!-- RECORD the features and capabilities the library will offer at the pre-alpha stage

### :lucide-bean: Alpha Stage
<!-- This section is also described in ROADMAP.md
  [link]: ../../../../ROADMAP.md#alpha-stage

  REMEMBER TO MIRROR ANY CHANGES ON BOTH FILES

<!-- RECORD the features and capabilities the library will offer at the alpha stage

### :lucide-sprout: Beta Stage
<!-- This section is also described in ROADMAP.md
  [link]: ../../../../ROADMAP.md#beta-stage

  REMEMBER TO MIRROR ANY CHANGES ON BOTH FILES

<!-- RECORD the features and capabilities the library will offer at the beta stage

### :lucide-tree-pine: Stable Release
<!-- This section is also described in ROADMAP.md
  [link]: ../../../../ROADMAP.md#stable-release

  REMEMBER TO MIRROR ANY CHANGES ON BOTH FILES

<!-- RECORD the features and capabilities the library will offer for it to be considered stable

### :lucide-infinity: Project Maturation
<!-- This section is also described in ROADMAP.md
  [link]: ../../../../ROADMAP.md#project-maturation

  REMEMBER TO MIRROR ANY CHANGES ON BOTH FILES

<!-- RECORD the features and capabilities that will lead the project's capabilities beyond what is currently expected for a stable release
-->

<!-- Anchors -->

{% if cookiecutter.__scm_platform_group == 'glab-paid' -%}
[1]: {{ cookiecutter.__gitlab_org_latch }}/epics
{% elif cookiecutter.__scm_platform_group == 'glab-free' -%}
[1]: {{ cookiecutter.__scm_repo_latch }}/milestones
{% else -%}
[1]: {{ cookiecutter.__scm_repo_latch }}/projects
{% endif -%}
[2]: https://img.shields.io/pypi/status/{{ cookiecutter.repo_name }}?style=for-the-badge&logo=theplanetarysociety&label=stage
