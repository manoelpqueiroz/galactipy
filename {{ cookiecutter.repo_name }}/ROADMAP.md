# :{% if cookiecutter.__scm_platform_lc == 'github' %}world_{% endif %}map: {{ cookiecutter.project_name }} Roadmap

## About {{ cookiecutter.project_name }}

{{ cookiecutter.project_description }}.

### Project Mission
{%- if cookiecutter.create_docs %}
<!-- This section is also described in the formal documentation with a different structure
{%- if cookiecutter.licence != 'nos' %}
  [link]: ./docs/development/roadmap.md#roadmap
{%- else %}
  [link]: ./docs/noticeboard/roadmap.md#project-roadmap
{%- endif %}

  REMEMBER TO MIRROR ANY CHANGES ON BOTH FILES, ADAPTING TO THE RESPECTIVE MEDIUM
-->
{%- endif %}

<!-- DEFINE your project mission, in tandem with the "Purpose & Function" section on README.md -->

{% if cookiecutter.licence != 'nos' -%}
### How to Get Involved

This file is mainly used
for informational purposes.
If you wish to know
how to get involved with {{ cookiecutter.project_name }},
check out the [`CONTRIBUTING`][contributing] file,
where you can get acquainted
with the many ways
of helping the project.

{% endif -%}
## About this Document

This document provides
an overview on the project's major phases
and features users should expect
at each stage of development.
It also presents
{%- if cookiecutter.scm_platform == 'GitLab Premium/Ultimate' %}
a summary of the {{ cookiecutter.project_name }} [GitLab Epics][1]
{%- elif cookiecutter.scm_platform == 'GitLab Free' %}
a summary of the {{ cookiecutter.project_name }} [GitLab Milestones][1]
{%- else %}
a summary of the {{ cookiecutter.project_name }} [GitHub Projects][1]
{%- endif %}
that are in the project's release pipeline.
{%- if cookiecutter.licence != 'nos' %}
Most items are gathered
from the community
or include a feedback loop
with the community.
This should serve
as a reference point
for {{ cookiecutter.project_name }} users and contributors
to understand where the project is heading,
and help determine
if a contribution could be conflicting
with a longer term plan.

### How to Help
{%- else %}
### Management
{%- endif %}

Discussion on the roadmap takes place
via {{ cookiecutter.__mr_term }}s
and discussions on the project's repository
over {{ cookiecutter.__scm_platform_base }}.
Please check the sections
on [{{ cookiecutter.__mr_term }}s][2] and [Roadmap Maintenance][3]
of the `CONTRIBUTING` file
for further clarification
on how to proceed
if you believe a discussion
surrounding the project's direction
{%- if cookiecutter.licence != 'nos' %}
should take place,
whether you want
to provide suggestions
or just feedback to an item
in the roadmap.
{%- else %}
should take place.
{%- endif %}

Please review the roadmap
to avoid potential duplicated effort.

## Development Stages
{%- if cookiecutter.create_docs %}
<!-- This section is also described in the formal documentation
{%- if cookiecutter.licence != 'nos' %}
  [link]: ./docs/development/roadmap.md#development-stages
{%- else %}
  [link]: ./docs/noticeboard/roadmap.md#development-stages
{%- endif %}

  REMEMBER TO MIRROR ANY CHANGES ON BOTH FILES
-->
{%- endif %}

![Project stage][4]

{{ cookiecutter.project_name }} is currently in the
**Planning** stage,
seeking contributors
to help refine
its foundational features
while laying out the thresholds
for each stage of development.

<!-- UPDATEME when you have relevant information to divulge to the community

We envision that {{ cookiecutter.project_name }}
will evolve through the following phases:

### Pre-Alpha Stage
{%- if cookiecutter.create_docs %}
<!-- This section is also described in the formal documentation
{%- if cookiecutter.licence != 'nos' %}
  [link]: ./docs/development/roadmap.md#lucide-line-squiggle-pre-alpha-stage
{%- else %}
  [link]: ./docs/noticeboard/roadmap.md#lucide-line-squiggle-pre-alpha-stage
{%- endif %}

  REMEMBER TO MIRROR ANY CHANGES ON BOTH FILES
{%- endif %}

<!-- DEFINE the features and capabilities the library will offer at the pre-alpha stage

### Alpha Stage
{%- if cookiecutter.create_docs %}
<!-- This section is also described in the formal documentation
{%- if cookiecutter.licence != 'nos' %}
  [link]: ./docs/development/roadmap.md#lucide-bean-alpha-stage
{%- else %}
  [link]: ./docs/noticeboard/roadmap.md#lucide-bean-alpha-stage
{%- endif %}

  REMEMBER TO MIRROR ANY CHANGES ON BOTH FILES
{%- endif %}

<!-- DEFINE the features and capabilities the library will offer at the alpha stage

### Beta Stage
{%- if cookiecutter.create_docs %}
<!-- This section is also described in the formal documentation
{%- if cookiecutter.licence != 'nos' %}
  [link]: ./docs/development/roadmap.md#lucide-sprout-beta-stage
{%- else %}
  [link]: ./docs/noticeboard/roadmap.md#lucide-sprout-beta-stage
{%- endif %}

  REMEMBER TO MIRROR ANY CHANGES ON BOTH FILES
{%- endif %}

<!-- DEFINE the features and capabilities the library will offer at the beta stage

### Stable Release
{%- if cookiecutter.create_docs %}
<!-- This section is also described in the formal documentation
{%- if cookiecutter.licence != 'nos' %}
  [link]: ./docs/development/roadmap.md#lucide-tree-pine-stable-release
{%- else %}
  [link]: ./docs/noticeboard/roadmap.md#lucide-tree-pine-stable-release
{%- endif %}

  REMEMBER TO MIRROR ANY CHANGES ON BOTH FILES
{%- endif %}

<!-- DEFINE the features and capabilities the library will offer for it to be considered stable

### Project Maturation
{%- if cookiecutter.create_docs %}
<!-- This section is also described in the formal documentation
{%- if cookiecutter.licence != 'nos' %}
  [link]: ./docs/development/roadmap.md#lucide-infinity-project-maturation
{%- else %}
  [link]: ./docs/noticeboard/roadmap.md#lucide-infinity-project-maturation
{%- endif %}

  REMEMBER TO MIRROR ANY CHANGES ON BOTH FILES
{%- endif %}

<!-- DEFINE the features and capabilities that will lead the project's capabilities beyond what is currently expected for a stable release

## Roadmap History

The following table includes
the current roadmap for {{ cookiecutter.project_name }}
for summarisation
and discussion purposes only.
Dates provided here
are gross estimations
and might be outdated,
{%- if cookiecutter.scm_platform == 'GitLab Premium/Ultimate' %}
please refer to each epic
{%- elif cookiecutter.scm_platform == 'GitLab Free' %}
please refer to each milestone
{%- else %}
please refer to each project
{%- endif %}
for more accurate information.

{% if cookiecutter.licence != 'nos' -%}
Priorities and requirements change based on
community feedback,
roadblocks encountered,
community contributions
etc.
{% endif -%}
If you depend
on a specific item,
check if it is mapped for development
{%- if cookiecutter.scm_platform == 'GitLab Premium/Ultimate' %}
through the most appropriate epic.
{%- elif cookiecutter.scm_platform == 'GitLab Free' %}
through the most appropriate milestone.
{%- else %}
through the most appropriate project.
{%- endif %}
If not,
open a [**Request for Improvement**][5]
{%- if cookiecutter.__scm_platform_lc == 'gitlab' %}
through the Issue Tracker.
{%- else %}
through GitHub Discussions.
{%- endif %}

{% if cookiecutter.licence != 'nos' -%}
We will try our best
to bring updated status information.

{% endif -%}
{% if cookiecutter.scm_platform == 'GitLab Premium/Ultimate' -%}
| Epic | Description | Theme | Timeline |
{% elif cookiecutter.scm_platform == 'GitLab Free' -%}
| Milestone | Description | Theme | Timeline |
{% else -%}
| Project | Description | Theme | Timeline |
{% endif -%}
| --------- | ------------------------------------------------------------------------------------------------------------------------------------------------- | :----------------------------------: | :----------------------------------------------------: |
| Hyperlink to item | Short description of the development stream | A standardised category under which the development stream falls | Estimated delivery date or version through which the development stream has been delivered |
-->

{% if cookiecutter.licence != 'nos' -%}
You can also help us
deliver features
by contributing directly to {{ cookiecutter.project_name }},
we are always
looking for contributors
that will help us reduce
technical,
automation,
and documentation debt.
If you don't know where to start,
read the [guidelines][6] for developers
to situate yourself first
and get to know
how we work as a team.
If you still have any questions,
open a Request for Support
{%- if cookiecutter.__scm_platform_lc == 'gitlab' %}
via the [Issue Tracker][7]
{%- else %}
via [GitHub Discussions][7]
{%- endif %}
so the team can help
with clarifications.

[contributing]: {{ cookiecutter.__scm_link_url }}/blob/master/CONTRIBUTING.md

{% endif -%}
{%- if cookiecutter.scm_platform == 'GitLab Premium/Ultimate' %}
[1]: {{ cookiecutter.__gitlab_org }}/epics
{%- elif cookiecutter.scm_platform == 'GitLab Free' %}
[1]: {{ cookiecutter.__scm_link_url }}/milestones
{%- else %}
[1]: {{ cookiecutter.__scm_link_url }}/projects
{%- endif %}
[2]: {{ cookiecutter.__scm_link_url }}/blob/master/CONTRIBUTING.md#start-with-a-{{ cookiecutter.__mr_term_slug }}
[3]: {{ cookiecutter.__scm_link_url }}/blob/master/CONTRIBUTING.md#roadmap-management
[4]: https://img.shields.io/pypi/status/{{ cookiecutter.repo_name }}?style=for-the-badge&logo=theplanetarysociety&label=stage
{%- if cookiecutter.__scm_platform_lc == 'gitlab' %}
[5]: {{ cookiecutter.__scm_link_url }}/issues/new?description_template=Request%20for%20Improvement
{%- else %}
[5]: {{ cookiecutter.__scm_link_url }}/discussions/new?category=requests-for-improvement
{%- endif %}
{%- if cookiecutter.licence != 'nos' %}
[6]: {{ cookiecutter.__scm_link_url }}/blob/master/CONTRIBUTING.md#speaking_head-proposing-changes-as-a-developer
{%- if cookiecutter.__scm_platform_lc == 'gitlab' %}
[7]: {{ cookiecutter.__scm_link_url }}/issues/new?description_template=Request%20for%20Support
{%- else %}
[7]: {{ cookiecutter.__scm_link_url }}/discussions/new?category=requests-for-support
{%- endif %}
{%- endif %}
