{% raw -%}
---
tags:
  - Development Guides
  - Workflows
---

{% endraw -%}
# Preparing to Contribute
{%- if cookiecutter.__scm_platform_group == 'glab-paid' %}
<!-- This section is also described in project and group CONTRIBUTING.md guides
  [project]: ../../../../CONTRIBUTING.md#preparing-to-contribute
  [group]: {{ cookiecutter.__contributing_prefix }}#preparing-to-contribute

  REMEMBER TO INCORPORATE CHANGES FROM BOTH GUIDES WHEN UPDATING THIS FILE
-->
{%- else %}
<!-- This section is also described in CONTRIBUTING.md
  [link]: ../../../../CONTRIBUTING.md#preparing-to-contribute

  REMEMBER TO MIRROR ANY CHANGES ON BOTH FILES
-->
{%- endif %}

## Choosing What to Contribute
{%- if cookiecutter.__scm_platform_group == 'glab-paid' %}
<!-- This section is also described in project and group CONTRIBUTING.md guides
  [project]: ../../../../CONTRIBUTING.md#choosing-what-to-contribute
  [group]: {{ cookiecutter.__contributing_prefix }}#choosing-what-to-contribute

  REMEMBER TO INCORPORATE CHANGES FROM BOTH GUIDES WHEN UPDATING THIS FILE
-->
{%- else %}
<!-- This section is also described in CONTRIBUTING.md
  [link]: ../../../../CONTRIBUTING.md#choosing-what-to-contribute

  REMEMBER TO MIRROR ANY CHANGES ON BOTH FILES
-->
{%- endif %}

[![Needs Triage][1]][2]

Everyone benefits
if contributors focus on changes
that are useful,
clear,
easy to evaluate,
and already pass basic checks.

Sometimes,
a contributor will already have
a particular new change or fix
in mind.
If seeking ideas,
consult the list of [starter assignments][3].

Before proceeding,
contributors should evaluate
if the proposed change
is likely to be
relevant,
new
and actionable:

- Is it clear
  that code or configuration files
  must change?
  Proposing a {{ cookiecutter.__mr_term }} is appropriate
  only when a clear problem
  or beneficial change
  has been identified.
  If simply having trouble using {{ cookiecutter.project_name }},
  go through the [`README`][4] file and links directing
  to support content first,
  rather than consider filing an issue
  or proposing an {{ cookiecutter.__mr_acronym }}.
  When in doubt,
  email [`{{ cookiecutter.email }}`][5] first
  about the possible change;
{%- if cookiecutter.__scm_platform_lc == 'gitlab' %}
- Search the [Issue Tracker][6]
{%- else %}
- Search the [Issue Tracker][6],
  [Discussions page][6a]
{%- endif %}
  and [past {{ cookiecutter.__mr_term }}s][7]
  for related discussions.
  Often,
  the problem has been discussed before,
  with a resolution
  that doesn't require a code or configuration change,
  or recording what kinds of changes
  will not be accepted as a resolution;
- Otherwise,
  if a logically similar issue or {{ cookiecutter.__mr_acronym }} already exists,
  then contribute to the discussion first,
  instead of creating a new one;
- Is the scope of the change
  matched to the contributor's level of experience?
  Anyone is qualified
  to suggest a typo fix,
  but refactoring core scheduling logic
  requires much more understanding
  of the underlying tool/code.
  Some changes require building up experience first.

{% if cookiecutter.app_type != 'bare_repo' -%}
It's worth emphasizing that
changes to CLI commands
{%- if cookiecutter.__app_group == 'tui' %}
and interface elements
{%- endif %}
available for users in {{ cookiecutter.project_name }}
are more complex to implement
as it requires
a potential overhaul of the public API.
They will be subjected
to more scrutiny,
and held to a higher standard of review
than changes
to less fundamental building blocks.

{% endif -%}
## Opening Admissible {{ cookiecutter.__mr_term }}s
{%- if cookiecutter.__scm_platform_group == 'glab-paid' %}
<!-- This section is also described in the group CONTRIBUTING.md guide
  [link]: {{ cookiecutter.__contributing_prefix }}#opening-admissible-{{ cookiecutter.__mr_term_slug }}s

  REMEMBER TO INCORPORATE CHANGES TO THIS FILE WHEN UPDATING THE GUIDE
-->
{%- else %}
<!-- This section is also described in CONTRIBUTING.md
  [link]: ../../../../CONTRIBUTING.md#opening-admissible-{{ cookiecutter.__mr_term_slug }}s

  REMEMBER TO MIRROR ANY CHANGES ON BOTH FILES
-->
{%- endif %}

For developers and maintainers,
changes should not be approached
in a reactive way
as demands,
but as a proactive **proposals**.
If you are contributing in the {{ cookiecutter.project_name }} repository,
you are expected
to always act on
and provide proposals
to improve the state of the project.
This distinguishes developers
from {{ cookiecutter.project_name }} users who,
unfamiliar with the codebase
and project configuration,
are only able to _request_ changes
through the Issue Tracker{% if cookiecutter.__scm_platform_lc == 'github' %} and GitHub Discussions{% endif %}.

To work under
a proactive proposal mindset,
we always [start with a {{ cookiecutter.__mr_term }}][8].

It is best
to follow these best practices
when proposing changes:

- **Always** use one of the [{{ cookiecutter.__mr_term }} templates][9],
  applying the proper type
  to the change being proposed.
  Each template contains
  a brief summary detailing
  under which circumstances
  it is best employed.
  This helps coordinate discussions
  with the rest of the team
  and facilitates the reviewer's work;
- If the change is non-trivial,
  we encourage you
  to start a discussion
  with a maintainer
  or another member of the team.
  You can do this
  by tagging them in an {{ cookiecutter.__mr_acronym }}
  before submitting the code for review.
  Talking to team members
  can be helpful
  when making design decisions.
  Communicating the [intent][10] behind your changes
  can also help expedite {{ cookiecutter.__mr_term }} reviews;
- Follow our [commit customs][11],
  as consistent commit messages
  that follow these guidelines
  make the history more readable.

Also equally important
is the notion to
**keep {{ cookiecutter.__mr_acronym }}s simple**,
with the amount of changes in a single {{ cookiecutter.__mr_acronym }}
as small as possible.
If you want
to contribute a large feature,
think carefully about
what the minimum valuable change is.
Can you split the functionality
into two smaller {{ cookiecutter.__mr_acronym }}s?
Can you submit
only a fraction of the code?
Can you start
with a minimal proof-of-concept?
Can you do
just a part of the refactor?

<div align="center">

<i>Live by smaller iterations.</i>

</div>

Small {{ cookiecutter.__mr_acronym }}s
which are more easily reviewed
lead to higher code quality,
which is more important to {{ cookiecutter.project_name }}
than having a minimal commit log.
The smaller an {{ cookiecutter.__mr_acronym }} is,
the more likely it will be merged quickly.
After that
you can send more {{ cookiecutter.__mr_acronym }}s
to enhance and expand the feature.
The [_How to Get Faster PR Reviews_][12] guide
from the Kubernetes team
also has some great points regarding this.

## Review Criteria
{%- if cookiecutter.__scm_platform_group == 'glab-paid' %}
<!-- This section is also described in the group CONTRIBUTING.md guide
  [link]: {{ cookiecutter.__contributing_prefix }}#review-criteria

  REMEMBER TO INCORPORATE CHANGES TO THIS FILE WHEN UPDATING THE GUIDE
-->
{%- else %}
<!-- This section is also described in CONTRIBUTING.md
  [link]: ../../../../CONTRIBUTING.md#review-criteria

  REMEMBER TO MIRROR ANY CHANGES ON BOTH FILES
-->
{%- endif %}

Before considering how to contribute,
it's useful to understand
how contributions are reviewed,
and why changes may be rejected.
See the detailed [guide][13] for code reviewers
from Google's Engineering Practices documentation.
Simply put,
changes that have many or large positives,
and few negative effects or risks,
are much more likely
to be merged,
and merged quickly.
Risky and less valuable changes
are unlikely to be merged,
and may be rejected outright
rather than receive iterations of review.

Below is a non-exhaustive list
of traits
a contribution might have
that either enhances or hinders
its probability of being merged:

- **Positives:**
    - Fixes the root cause of a bug
      in existing functionality;
    - Adds functionality
      or fixes a problem
      needed by a large number of users;
    - Simple,
      targeted;
    - Maintains or improves
      template consistency;
    - Easily tested;
      has tests;
    - Reduces complexity,
      lines of code
      and configuration;
    - Change has already been discussed
      and is known
      to committers;
- **Negatives, risks:**
    - Band-aids
      a symptom of a bug only
      without addressing its root cause;
    - Introduces complex new functionality,
      especially an API
      that needs to be supported;
    - Adds complexity
      that only helps
      a niche use case;
    - Changes a public API
      or semantics
      (rarely allowed);
    - Adds large dependencies;
    - Changes versions
      of existing dependencies
      without proper testing;
    - Adds a large amount of code;
    - Makes lots of modifications
      in one "big bang" change.

<!-- Anchors -->

[1]: https://img.shields.io/badge/needs_triage-4285f4?style=for-the-badge
{% if cookiecutter.__scm_platform_group == 'glab-paid' -%}
[2]: {{ cookiecutter.__scm_link_url }}/issues?state=opened&status=Needs%20Triage&type%5B%5D=issue
[3]: {{ cookiecutter.__scm_link_url }}/issues?state=opened&label_name%5B%5D=starter-assignment%3A%3A%2A&type%5B%5D=issue
{% elif cookiecutter.__scm_platform_group == 'glab-free' -%}
[2]: {{ cookiecutter.__scm_link_url }}/issues?state=opened&label_name%5B%5D=sts-needs-triage&type%5B%5D=issue
[3]: {{ cookiecutter.__scm_link_url }}/issues?state=opened&label_name%5B%5D=starter-assignment&type%5B%5D=issue
{% else -%}
[2]: {{ cookiecutter.__scm_link_url }}/issues/?q=is%3Aissue%20state%3Aopen%20label%3Asts-needs-triage
[3]: {{ cookiecutter.__scm_link_url }}/issues/?q=is%3Aissue%20state%3Aopen%20label%3Astarter-assignment
{% endif -%}
[4]: {{ cookiecutter.__scm_link_url }}/blob/master/README.md
[5]: mailto:{{ cookiecutter.email }}
[6]: {{ cookiecutter.__scm_link_url }}/issues
{% if cookiecutter.__scm_platform_lc == 'gitlab' -%}
[7]: {{ cookiecutter.__scm_link_url }}/merge_requests
{% else -%}
[6a]: {{ cookiecutter.__scm_link_url }}/discussions
[7]: {{ cookiecutter.__scm_link_url }}/pulls
{%- endif %}
[8]: ../philosophy.md#start-with-a-{{ cookiecutter.__mr_term_slug }}
{% if cookiecutter.__scm_platform_lc == 'gitlab' -%}
[9]: {{ cookiecutter.__scm_link_url }}/tree/master/.gitlab/merge_request_templates
{% else -%}
[9]: {{ cookiecutter.__scm_link_url }}/tree/master/.github/MERGE_REQUEST_TEMPLATE
{% endif -%}
[10]: ../philosophy.md#say-why-not-just-what
[11]: ../policies/committing.md
[12]: https://github.com/kubernetes/kubernetes/blob/release-1.5/docs/devel/faster_reviews.md
[13]: https://google.github.io/eng-practices/review/
