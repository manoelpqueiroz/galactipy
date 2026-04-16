{% raw -%}
---
tags:
  - Development Guides
  - Policies & Rules
---

{% endraw -%}
# Branch Organization
{%- if cookiecutter.scm_platform == 'GitLab Premium/Ultimate' %}
<!-- This section is also described in the group CONTRIBUTING.md guide
  [link]: {{ cookiecutter.__contributing_prefix }}#branch-organization

  REMEMBER TO INCORPORATE CHANGES TO THIS FILE WHEN UPDATING THE GUIDE
-->
{%- else %}
<!-- This section is also described in CONTRIBUTING.md
  [link]: ../../../../CONTRIBUTING.md#branch-organization

  REMEMBER TO MIRROR ANY CHANGES ON BOTH FILES
-->
{%- endif %}

We apply the [{{ cookiecutter.project_name }} Philosophy][1]
for conducting new development,
which means
that all changes
revolve around open {{ cookiecutter.__mr_term }}s,
and {{ cookiecutter.__mr_term }}s are
the central space
for discussing design,
implementation
and monitoring development health
{%- if cookiecutter.__scm_platform_lc == 'gitlab' %}
with [CI pipelines][2].
{%- else %}
with [GitHub Actions][2].
{%- endif %}

Creation of new branches
without subsequent attachment
to a new {{ cookiecutter.__mr_acronym }}
is strongly discouraged.
If the work is still in progress
but needs to be uploaded
to the repository,
name the branch
with the `test-`
or `wip-` prefixes
so the CI will ignore it.

## Branch Naming Standards
{%- if cookiecutter.scm_platform == 'GitLab Premium/Ultimate' %}
<!-- This section is also described in the group CONTRIBUTING.md guide
  [link]: {{ cookiecutter.__contributing_prefix }}#branch-naming-standards

  REMEMBER TO INCORPORATE CHANGES TO THIS FILE WHEN UPDATING THE GUIDE
-->
{%- else %}
<!-- This section is also described in CONTRIBUTING.md
  [link]: ../../../../CONTRIBUTING.md#branch-naming-standards

  REMEMBER TO MIRROR ANY CHANGES ON BOTH FILES
-->
{%- endif %}

While standard branch naming
is not strictly required,
we offer some suggestions
to enhance communication
during {{ cookiecutter.__mr_term }} reviews:

- Use the [imperative mood][3]
  with concise language
  for your branch names;
  this helps reviewers
  quickly gain insight
  into the changes
  your branch applies;
- For small changes,
  consider naming the branch
  with either the `flash-` or `fl-` prefixes
  to inform reviewers
  of their nature.

!!! note

    Flash branches are not the same
    as `quick-win` labelled issues:

    - **`quick-win` issues**
      mark planned developments
      that are easy to deliver
      and are used
      to track such initiatives;
    - **Flash branches**
      indicate changes
      that are intended
      to be created
      and merged quickly,
      often representing unplanned work
      that doesn't require an associated issue
      or extensive {{ cookiecutter.__mr_term }} details.

    While flash branches can sometimes
    be linked to `quick-win` issues,
    they primarily serve
    as a signal
    for short-lived changes
    without the need
    for prior planning
    or detailed documentation.

<!-- Anchors -->

[1]: ../philosophy.md
[2]: ../policies/ci.md
[3]: ../policies/developing.md#issue-titles-should-be-framed-in-imperative-mood
