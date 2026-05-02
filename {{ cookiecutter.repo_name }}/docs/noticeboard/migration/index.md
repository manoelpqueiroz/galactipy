{% raw -%}
---
tags:
  - Section Intros
  - User Guides
---

{% endraw -%}
# Migration Guides

This section provides users
with migration guides
for when {{ cookiecutter.project_name }} implements breaking changes.

If by any chance
you still have problems
after following through the guides
listed here,
please open a [Request for Support][1]
{%- if cookiecutter.__scm_platform_lc == 'gitlab' %}
in the Issue Tracker.
{%- else %}
in the Discussions page.
{%- endif %}

<!-- RECORD one subpage for each breaking change requiring migration guides -->

<!-- Anchors -->
{%- if cookiecutter.__scm_platform_lc == 'gitlab' %}

[1]: {{ cookiecutter.__scm_repo_latch }}/issues/new?description_template=Request%20for%20Support
{%- else %}

[1]: {{ cookiecutter.__scm_repo_latch }}/discussions/new?category=requests-for-improvement
{%- endif %}
