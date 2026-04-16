{% raw -%}
---
tags:
  - For Your Information
  - Workflows
---

{% endraw -%}
# Contributing by Reviewing Changes
{%- if cookiecutter.scm_platform == 'GitLab Premium/Ultimate' %}
<!-- This section is also described in project and group CONTRIBUTING.md guides
  [project]: ../../../../CONTRIBUTING.md#contributing-by-reviewing-changes
  [group]: {{ cookiecutter.__contributing_prefix }}#contributing-by-reviewing-changes

  REMEMBER TO INCORPORATE CHANGES FROM BOTH GUIDES WHEN UPDATING THIS FILE
-->
{%- else %}
<!-- This section is also described in CONTRIBUTING.md
  [link]: ../../../../CONTRIBUTING.md#contributing-by-reviewing-changes

  REMEMBER TO MIRROR ANY CHANGES ON BOTH FILES
-->
{%- endif %}

Changes to {{ cookiecutter.project_name }} source code are
proposed,
reviewed
and committed
via [{{ cookiecutter.__scm_platform_base }} {{ cookiecutter.__mr_term }}s][1].
Anyone can view and comment
on active changes here.
Participating in code reviews
helps you understand our processes
and explore different domains of the project.
Contribute by reviewing proposed changes
and identifying potential improvements
– as simple as typos
or styling inconsistencies.

As a reviewer,
your job is not
to make sure that
the code is what you would have written
– **because it will not be**.
Your job as a reviewer of a change
is to make sure that
the change as written by its submitter
is correct.

Try to think of edge cases
when testing or evaluating the code,
double check the test coverage.
However,
do not frown
if you merged the {{ cookiecutter.__mr_term }}
and something broke after all.
This is the learning path
to avoiding this mistake
on the next attempt.
Not doing a review
in the first place
will not move you forward either.

To get you quickstarted
on reviewing {{ cookiecutter.__mr_acronym }}s for {{ cookiecutter.project_name }},
here are a few tips
that may help
overcoming the paralysis
of [taking action][2]:

- Verify that
  the appropriate tests
  have been added.
  When testing a feature or change,
  check out the code tests
  at least the happy paths
  according to the specification
  of the {{ cookiecutter.__mr_acronym }};
- See if documentation has been added
  for the change in question.
  Smaller documentation changes
  should be added
  along with the core changes
  of the proposal;
- Changes should be **readable**,
  that is,
  you as a reviewer
  should be able
  to understand the nature of the changes
  without additional explanations
  outside the changes;
  however,
  if something is not clear,
  we encourage you
  to ask for clarification
  as it might indicate
  the need for further changes
  for full compliance
  before a maintainer
  can complete the {{ cookiecutter.__mr_acronym }};
- You should not rush
  through a code review,
  but also,
  you need to do it promptly.
  Your colleagues are waiting for you.

We strongly encourage you
to take further readings on
the [Review Process][3],
the [Responsibilities of the Reviewer][4]
and [general communication guidelines][5]
to get more detail
on how to make
the most out of your contributions
as a reviewer.
We appreciate your commitment beforehand!

<!-- Anchors -->
{%- if cookiecutter.__scm_platform_lc == 'gitlab' %}

[1]: {{ cookiecutter.__scm_link_url }}/merge_requests
{%- else %}

[1]: {{ cookiecutter.__scm_link_url }}/pulls
{%- endif %}
[2]: ../philosophy.md#operate-with-a-bias-for-action
[3]: ../for_developers/review.md
[4]: ../for_developers/roles.md#the-responsibility-of-the-reviewer
[5]: ../for_developers/behave.md
