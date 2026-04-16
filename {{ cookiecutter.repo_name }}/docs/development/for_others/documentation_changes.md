{% raw -%}
---
tags:
  - For Your Information
---

{% endraw -%}
# Contributing with Documentation Changes
<!-- This section is also described in CONTRIBUTING.md
  [link]: ../../../../CONTRIBUTING.md#contributing-with-documentation-changes

  REMEMBER TO MIRROR ANY CHANGES ON BOTH FILES
-->

Contributing to the documentation benefits
everyone who uses {{ cookiecutter.project_name }}.
We encourage you
to help us improve the documentation,
and you don't have to be an expert on {{ cookiecutter.project_name }}
to do so!
In fact,
there are sections of the docs
that are worse off
after being written by experts.

The main goal of any documentation
is to make usage of the library
easy for any user,
regardless of their level of experience
with it.
If something in the docs
doesn't make sense to you,
that means there is room for improvement
and disclosing it to the community at large
allows everyone to discuss
and figure out
what can be done.
This is a great way to ensure
changes will be made
so they help the next person.

If you have found an inconsistency
or have a suggestion
on how the {{ cookiecutter.project_name }} can improve,
don't hesitate in letting us know!
Open an [Request for Improvement][1]
and tell us what you would like
to see changed
in the docs.

You are also much welcome
to make modifications to the documentation
yourself
to help us
get ever closer
to providing
an outstanding reference
in the open source space!
See the [Documentation Guideline][2]
for instructions
on how to make changes
to our docs.

<!-- Anchors -->
{%- if cookiecutter.__scm_platform_lc == 'gitlab' %}

[1]: {{ cookiecutter.__scm_link_url }}/issues/new?description_template=Request%20for%20Improvement
{%- else %}

[1]: {{ cookiecutter.__scm_link_url }}/discussions/new?category=requests-for-improvement
{%- endif %}
[2]: ../for_developers/documentation/index.md
