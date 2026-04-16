{% raw -%}
---
tags:
  - For Your Information
---

{% endraw -%}
# Contributing to Roadmap Maintenance
<!-- This section is also described in CONTRIBUTING.md
  [link]: ../../../../CONTRIBUTING.md#contributing-to-roadmap-maintenance

  REMEMBER TO MIRROR ANY CHANGES ON BOTH FILES
-->

[![Issues][1]][2]
{%- if cookiecutter.scm_platform == 'GitLab Free' %}
[![Tasks][2a]][2b]
{%- endif %}

The project roadmap is maintained
through [{{ cookiecutter.__scm_platform_base }} {{ cookiecutter.__roadmap_item.capitalize() }}s][3].
It provides an overview
of the medium and long-term priorities of {{ cookiecutter.project_name }}
as a project,
whether they impact end-users or not.

Contributors and maintainers
are responsible for managing the roadmap.
However,
anyone can support the project
by ensuring alignment with this roadmap,
identifying opportunities
that influence
the project's most impactful deliverables
and communicating them
to the development team:

- Getting familiar
  with our milestones
  and associated items,
  and then
  opening additional [**Requests for Improvement**][4]
  that pertain to existing {{ cookiecutter.__roadmap_item }}s;
- Commenting on [issues without associated {{ cookiecutter.__roadmap_item }}s][2]
  and suggesting what relevant developments
  could they be associated with
  for the development team to evaluate;
- Linking issues and {{ cookiecutter.__mr_term }}s
  that provide combined effort
  towards a single goal of the project.
  If two or more development streams
  can be delivered with the same solution,
  we can generate increased aggregated value;
- Becoming a [contributor][5]
  to act on existing {{ cookiecutter.__roadmap_item }}s,
  propose new developments not yet mapped
  or recommend [changes to the roadmap itself][6].

<!-- Anchors -->

[1]: https://img.shields.io/badge/issues_without_{{ cookiecutter.__roadmap_item }}-006272?style=for-the-badge
{%- if cookiecutter.scm_platform == 'GitLab Premium/Ultimate' %}
[2]: {{ cookiecutter.__scm_link_url }}/issues?state=opened&type%5B%5D=issue&parent_id=None
[3]: {{ cookiecutter.__gitlab_org }}/epics
{%- elif cookiecutter.scm_platform == 'GitLab Free' %}
[2]: {{ cookiecutter.__scm_link_url }}/issues?state=opened&type%5B%5D=issue&milestone_title=None
[2a]: https://img.shields.io/badge/{{ cookiecutter.__task_item }}s_with_{{ cookiecutter.__roadmap_item }}-08b1ab?style=for-the-badge
[2b]: {{ cookiecutter.__scm_link_url }}/issues?state=all&type%5B%5D=task&milestone_title=Any
[3]: {{ cookiecutter.__scm_link_url }}/milestones
{%- else %}
[2]: {{ cookiecutter.__scm_link_url }}/issues/?q=is%3Aissue%20state%3Aopen%20no%3Aproject
[3]: {{ cookiecutter.__scm_link_url }}/projects
{%- endif %}
{%- if cookiecutter.__scm_platform_lc == 'gitlab' %}
[4]: {{ cookiecutter.__scm_link_url }}/issues/new?description_template=Request%20for%20Improvement
{%- else %}
[4]: {{ cookiecutter.__scm_link_url }}/discussions/new?category=requests-for-improvement
{%- endif %}
[5]: ../for_developers/index.md
[6]: ../roadmap.md
