{% raw -%}
---
tags:
  - Section Intros
  - For Your Information
---

{% endraw -%}
# Comparison with other Tools

{{ cookiecutter.project_name }} can be used
as an alternative to the tools listed here.

The pages in this section focus on
providing users of these tools
with a quick reference to translate
their common concepts and operations
to the standards applied by {{ cookiecutter.project_name }}.

!!! info

    We don't have any alternatives to {{ cookiecutter.project_name }}
    listed yet.
    If you have found a software
    similar to ours,
    open a [Request for Improvement][1]
    to ask for the inclusion of a new comparison page
    to the development team.

<!-- Anchors -->
{%- if cookiecutter.__scm_platform_lc == 'gitlab' %}

[1]: {{ cookiecutter.__scm_repo_latch }}/issues/new?description_template=Request%20for%20Improvement
{%- else %}

[1]: {{ cookiecutter.__scm_repo_latch }}/discussions/new?category=requests-for-improvement
{%- endif %}
