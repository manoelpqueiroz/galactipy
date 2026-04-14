{% raw -%}
---
tags:
  - Community Content
---

{% endraw -%}
# Community FAQ

This is a curated list of common questions
that have been raised in the past
and compiled here
for general reference.
Think of this page as a list
of our own Stack Overflow questions
to help the community
with guidance on common hurdles
faced by {{ cookiecutter.project_name }} users.

Please look thoroughly this list
before opening a request
{%- if cookiecutter.__scm_platform_lc == 'gitlab' %}
on the Issue Tracker,
{%- else %}
on the Discussions page,
{%- endif %}
as your question might
already be listed here.

!!! question

    {{ cookiecutter.project_name }} is yet to get a community FAQ question.
    Why not be the first to [contribute][1]
    and help {{ cookiecutter.project_name }}
    be easier to use?

<!-- Anchors -->
{%- if cookiecutter.__scm_platform_lc == 'gitlab' %}

[1]: {{ cookiecutter.__scm_link_url }}/issues/new?description_template=Request%20for%20Improvement
{%- else %}

[1]: {{ cookiecutter.__scm_link_url }}/discussions/new?category=requests-for-improvement
{%- endif %}
