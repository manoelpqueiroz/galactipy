{% raw -%}
---
tags:
  - Community Content
---

{% endraw -%}
# Community Tutorials

This is a curated list of guides for {{ cookiecutter.project_name }}
written by the community
that might be useful to you.

It covers users with content
ranging from beginner
to advanced topics.

!!! question

    {{ cookiecutter.project_name }} is yet to get a community tutorial.
    Why not be the first to [contribute][1]
    and help {{ cookiecutter.project_name }}
    be easier to use?

<!-- Anchors -->
{%- if cookiecutter.__scm_platform_lc == 'gitlab' %}

[1]: {{ cookiecutter.__scm_link_url }}/issues/new?description_template=Request%20for%20Improvement
{%- else %}

[1]: {{ cookiecutter.__scm_link_url }}/discussions/new?category=requests-for-improvement
{%- endif %}
