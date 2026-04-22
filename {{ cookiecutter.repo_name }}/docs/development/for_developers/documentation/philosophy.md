{% raw -%}
---
tags:
  - Development Guides
  - Policies & Rules
---

{% endraw -%}
# Documentation Philosophy
{%- if cookiecutter.__scm_platform_group == 'glab-paid' %}
<!-- This section is also described in the group CONTRIBUTING.md guide
  [link]: {{ cookiecutter.__contributing_prefix }}#documentation-philosophy

  REMEMBER TO INCORPORATE CHANGES TO THIS FILE WHEN UPDATING THE GUIDE
-->
{%- else %}
<!-- This section is also described in CONTRIBUTING.md
  [link]: ../../../../CONTRIBUTING.md#documentation-philosophy

  REMEMBER TO MIRROR ANY CHANGES ON BOTH FILES
-->
{%- endif %}

> Adapted from the [Google Style Guides][1].

When dealing with any
of the content and files
which can be declared documentation,
contributors should follow these principles
on top of our [core values][2]
to achieve the best results possible.

## Minimum Viable Documentation
{%- if cookiecutter.__scm_platform_group == 'glab-paid' %}
<!-- This section is also described in the group CONTRIBUTING.md guide
  [link]: {{ cookiecutter.__contributing_prefix }}#minimum-viable-documentation

  REMEMBER TO INCORPORATE CHANGES TO THIS FILE WHEN UPDATING THE GUIDE
-->
{%- else %}
<!-- This section is also described in CONTRIBUTING.md
  [link]: ../../../../CONTRIBUTING.md#minimum-viable-documentation

  REMEMBER TO MIRROR ANY CHANGES ON BOTH FILES
-->
{%- endif %}

A small set of fresh and accurate docs
is better than
a large assembly of "documentation"
in various states of disrepair.

- Write short and useful documents;
- Cut out everything unnecessary,
  including out-of-date,
  incorrect,
  or redundant information;
- Make a habit
  of continually massaging
  and improving every doc
  to suit the changing needs
  of their audience.

<div align="center">

<i>Docs work best when they are alive but frequently trimmed, like a bonsai tree.</i>

</div>

## Update Docs with Code
{%- if cookiecutter.__scm_platform_group == 'glab-paid' %}
<!-- This section is also described in the group CONTRIBUTING.md guide
  [link]: {{ cookiecutter.__contributing_prefix }}#update-docs-with-code

  REMEMBER TO INCORPORATE CHANGES TO THIS FILE WHEN UPDATING THE GUIDE
-->
{%- else %}
<!-- This section is also described in CONTRIBUTING.md
  [link]: ../../../../CONTRIBUTING.md#update-docs-with-code

  REMEMBER TO MIRROR ANY CHANGES ON BOTH FILES
-->
{%- endif %}

Update your documentation
in the same [{{ cookiecutter.__mr_term }}][3]
as the code change.
This keeps your docs fresh,
and is also a good place
to explain to your reviewer
what you're doing.

A good reviewer can at least insist
that docstrings,
header files,
the `README` file
and any other docs get updated
alongside the proposed change.

## Delete Dead Documentation
{%- if cookiecutter.__scm_platform_group == 'glab-paid' %}
<!-- This section is also described in the group CONTRIBUTING.md guide
  [link]: {{ cookiecutter.__contributing_prefix }}#delete-dead-documentation

  REMEMBER TO INCORPORATE CHANGES TO THIS FILE WHEN UPDATING THE GUIDE
-->
{%- else %}
<!-- This section is also described in CONTRIBUTING.md
  [link]: ../../../../CONTRIBUTING.md#delete-dead-documentation

  REMEMBER TO MIRROR ANY CHANGES ON BOTH FILES
-->
{%- endif %}

Dead docs are bad.
They misinform,
they slow down,
they incite despair in users
and laziness in team members.
They set a precedent
for leaving behind messes
in the codebase.
If your home is clean,
most guests will be clean
without being asked.

Just like any big cleaning project,
it's easy to be overwhelmed.
If the docs are in bad shape:

- Take it slow,
  doc health is a gradual accumulation;
- First delete
  what you're certain is wrong,
  ignore what's unclear.
- Get other team members involved;
  devote time
  to quickly scan every doc
  and make a simple decision:
  should we keep it
  or delete it?
- Default to delete
  or leave behind if migrating;
  stragglers can always be recovered.
- Iterate.

## Prefer Good over the Perfect
{%- if cookiecutter.__scm_platform_group == 'glab-paid' %}
<!-- This section is also described in the group CONTRIBUTING.md guide
  [link]: {{ cookiecutter.__contributing_prefix }}#prefer-good-over-the-perfect

  REMEMBER TO INCORPORATE CHANGES TO THIS FILE WHEN UPDATING THE GUIDE
-->
{%- else %}
<!-- This section is also described in CONTRIBUTING.md
  [link]: ../../../../CONTRIBUTING.md#prefer-good-over-the-perfect

  REMEMBER TO MIRROR ANY CHANGES ON BOTH FILES
-->
{%- endif %}

Documentation is an art.
There is no perfect document,
there are only proven methods
and prudent guidelines.

The standards
for an internal documentation review
are different
from the standards
for code reviews.
Reviewers should ask for improvements,
but in general,
the author should always be able
to invoke the _Better/Best Rule_.

Fast iteration is your friend.
To get long-term improvement,
authors must stay productive
when making short-term improvements.
Set lower standards for each {{ cookiecutter.__mr_term }},
so that more such {{ cookiecutter.__mr_acronym }}s can happen.

As a reviewer of a documentation {{ cookiecutter.__mr_acronym }}:

- When reasonable,
  clear the {{ cookiecutter.__mr_acronym }} immediately
  and trust that
  comments will be fixed appropriately;
- Prefer to suggest an alternative
  rather than leaving a vague comment;
- For substantial changes,
  start your own follow-up {{ cookiecutter.__mr_acronym }} instead;
  try especially to avoid comments
  of the form "You should also...";
- On rare occasions,
  hold up submission if the {{ cookiecutter.__mr_acronym }}
  actually makes the docs worse;
  it's okay to ask the author
  to revert.

As an author:

- Avoid wasting cycles
  with trivial argument;
  capitulate early and move on;
- Cite the _Better/Best Rule_
  as often as needed.

## Documentation is the Story of Our Code
{%- if cookiecutter.__scm_platform_group == 'glab-paid' %}
<!-- This section is also described in the group CONTRIBUTING.md guide
  [link]: {{ cookiecutter.__contributing_prefix }}#documentation-is-the-story-of-our-code

  REMEMBER TO INCORPORATE CHANGES TO THIS FILE WHEN UPDATING THE GUIDE
-->
{%- else %}
<!-- This section is also described in CONTRIBUTING.md
  [link]: ../../../../CONTRIBUTING.md#documentation-is-the-story-of-our-code

  REMEMBER TO MIRROR ANY CHANGES ON BOTH FILES
-->
{%- endif %}

Writing excellent code
doesn't end when your code compiles
or even if your test coverage reaches 100%.
It's easy to write something
a computer understands,
it's much harder to write something
both a human and a computer understand.
Your mission as a Code Health-conscious contributor
is to **write for humans first, computers second**.
Documentation is an important part
of this skill.

## Duplication is Evil
{%- if cookiecutter.__scm_platform_group == 'glab-paid' %}
<!-- This section is also described in the group CONTRIBUTING.md guide
  [link]: {{ cookiecutter.__contributing_prefix }}#duplication-is-evil

  REMEMBER TO INCORPORATE CHANGES TO THIS FILE WHEN UPDATING THE GUIDE
-->
{%- else %}
<!-- This section is also described in CONTRIBUTING.md
  [link]: ../../../../CONTRIBUTING.md#duplication-is-evil

  REMEMBER TO MIRROR ANY CHANGES ON BOTH FILES
-->
{%- endif %}

Do not write your own guide
to a common technology or process
– link to it instead.
If the guide doesn't exist
or it's badly out of date,
submit your own updates
directly to the upstream libraries.
Take ownership and don't be shy:
other teams will usually
welcome your contributions.

<!-- Anchors -->

[1]: https://google.github.io/styleguide/docguide/best_practices.html
[2]: ../../philosophy.md
[3]: ../../philosophy.md#start-with-a-{{ cookiecutter.__mr_term_slug }}
