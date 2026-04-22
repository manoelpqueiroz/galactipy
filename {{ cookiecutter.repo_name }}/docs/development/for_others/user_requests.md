{% raw -%}
---
tags:
  - For Your Information
  - Workflows
---

{% endraw -%}
# Contributing through User Requests
{%- if cookiecutter.__scm_platform_group == 'glab-paid' %}
<!-- This section is also described in project and group CONTRIBUTING.md guides
  [project]: ../../../../CONTRIBUTING.md#contributing-through-user-requests
  [group]: {{ cookiecutter.__contributing_prefix }}#contributing-through-user-requests

  REMEMBER TO INCORPORATE CHANGES FROM BOTH GUIDES WHEN UPDATING THIS FILE
-->
{%- else %}
<!-- This section is also described in CONTRIBUTING.md
  [link]: ../../../../CONTRIBUTING.md#contributing-through-user-requests

  REMEMBER TO MIRROR ANY CHANGES ON BOTH FILES
-->
{%- endif %}

If you are simply
having trouble using {{ cookiecutter.project_name }},
go through the [`README`][1] file and links
directing to support content first,
as well as this documentation,
rather than filing a request.

{{ cookiecutter.project_name }} implements
three types of requests for users
{%- if cookiecutter.__scm_platform_lc == 'gitlab' %}
through [Issue Templates][2]:
{%- else %}
through [Issue][2]
and [Discussion][2a] templates:
{%- endif %}

- **Requests for Correction**;
- **Requests for Improvement**;
- **Requests for Support**.

All three templates
provide a brief summary
explaining their purpose,
as well as a handy information
on where to best use them.
They contain structured sections
{%- if cookiecutter.__scm_platform_lc == 'gitlab' %}
with HTML comments
{%- endif %}
to guide you further
with opening your request correctly,
please follow them
as closely as possible.
If any instruction is not clear,
please raise your concern
so we can help
and improve them
if applicable.

!!! note

    Two additional templates,
    **Internal Work Item**
    and **Starter Assignment Treatment**,
    are available to contributors
    for specific cases
    regarding project development.
    These should not be used
    if you do not have Developer status.

**Always use one of the templates for opening requests!**
By taking a single look
at its type
and the structured sections
filled by the author,
we can provide faster feedback
on your request.
We will kindly ask you
to edit the work item
with the appropriate template
if one is not used
or used incorrectly.

Here are a few general tips
when opening any kind of request
to enhance your chances
of a quick response:

- Follow the template sections
  so team members can view
  your structured line of thought
  and actions leading up
  to your request;
- Provide **context**:
  explaining the conditions
  which led you to open your request
  facilitates our comprehension
  of your perspective
  and helps creating empathy
  with your case;
- **Avoid duplication**
  by making a real effort to determine
  whether your request
  has not been already made by another user
{%- if cookiecutter.__scm_platform_lc == 'gitlab' %}
  before using the [Search][3] feature
  for all items in the Issue Tracker;
{%- else %}
  before using the Search feature
  for all items in the [Issue Tracker][3]
  and the [Discussions Page][3a];
{%- endif %}
- It is also important
  to avoid requests
  that describe too much.
  Each should be documented
  in its own request.
  It's often unavoidable
  that requests can be complex,
  especially with big feature requests.
  Adding a lot of detail to a request
  is great,
  but when a complex one
  can be separated into multiple requests,
  that makes them easier to resolve.
  **One request per request**;
- **Titles are important!**
  Keep your titles
  short and descriptive.
  Don't try to
  cram every bit of information
  in the title.
  More importantly,
  titles should also be **compelling**.
  When someone reads your request,
  they should want to work on it.
  The title sells the request.
  Don't sacrifice allure for brevity;
    - A good rule of thumb
      is that a title should be
      descriptive enough
      that someone looking back at it later
      will understand
      what the purpose of the issue was
      and how it fits
      into the larger context;
    - To make your request more descriptive,
      avoid vague titles like
      "update files" or "fix issue."
      Instead, specify
      what the request comprises;
- Properly format your messages.
  Help the reader focus on what matters
  and understand the structure of your message.
  [{{ cookiecutter.__scm_platform_base }} Flavoured Markdown][4] has a simple
  but effective syntax,
  consider taking a look
  before writing your request;
- **Good requests are also professional development.**
  Many companies have a remote-first style
  where most discussions happen asynchronously.
  We truly believe that
  approaching your request with this mindset
  can also help you
  further become a better developer
  down the line.

## Specific Guidelines for Requests for Support
{%- if cookiecutter.__scm_platform_group == 'glab-paid' %}
<!-- This section is also described in project and group CONTRIBUTING.md guides
  [project]: ../../../../CONTRIBUTING.md#specific-guidelines-for-requests-for-support
  [group]: {{ cookiecutter.__contributing_prefix }}#specific-guidelines-for-requests-for-support

  REMEMBER TO INCORPORATE CHANGES FROM BOTH GUIDES WHEN UPDATING THIS FILE
-->
{%- else %}
<!-- This section is also described in CONTRIBUTING.md
  [link]: ../../../../CONTRIBUTING.md#specific-guidelines-for-requests-for-support

  REMEMBER TO MIRROR ANY CHANGES ON BOTH FILES
-->
{%- endif %}

If {{ cookiecutter.project_name }} is not working correctly for you,
most likely it is a simple configuration issue.
Try running {{ cookiecutter.project_name }} again
paying attention to the parameters
{%- if cookiecutter.__app_class == 'bare' %}
you have provided.
{%- else %}
you have provided,
or use a vanilla configuration
alternatively.
{%- endif %}

If you are still having difficulty
running {{ cookiecutter.project_name }} as desired,
open an [RFS][5],
{%- if cookiecutter.__app_class == 'bare' %}
and provide your
configuration and log files
{%- else %}
providing your `settings.toml`
and `report.log` files
{%- endif %}
if applicable.

Only open a Request for Correction
if you have clearly identified
an unexpected behaviour
that needs to be addressed.
Otherwise,
if details are not clear,
prefer sticking to the Request for Support
as the means to reach the team.

## Specific Guidelines for Requests for Improvement
{%- if cookiecutter.__scm_platform_group == 'glab-paid' %}
<!-- This section is also described in project and group CONTRIBUTING.md guides
  [project]: ../../../../CONTRIBUTING.md#specific-guidelines-for-requests-for-improvement
  [group]: {{ cookiecutter.__contributing_prefix }}#specific-guidelines-for-requests-for-improvement

  REMEMBER TO INCORPORATE CHANGES FROM BOTH GUIDES WHEN UPDATING THIS FILE
-->
{%- else %}
<!-- This section is also described in CONTRIBUTING.md
  [link]: ../../../../CONTRIBUTING.md#specific-guidelines-for-requests-for-improvement

  REMEMBER TO MIRROR ANY CHANGES ON BOTH FILES
-->
{%- endif %}

Requests for Improvement are used
when users feel a need for development
related to features provided by {{ cookiecutter.project_name }},
either existent
or yet-to-be-implemented.
They are much welcome,
as they help us engage with the community
on a more proactive level
and work to deliver a solution
of aggregated value
to our users.

Nevertheless,
before opening an [RFI][6],
take a moment to find out
whether your idea fits with the scope
and [aims][7] of the project.
It's up to _you_
to make a strong case
to convince the project's developers
of the merits of this feature.
Please provide
as much detail and context
as possible.

If you are requesting
an entirely new feature
to be added to the {{ cookiecutter.project_name }} toolset,
please consider answering
the following prospective questions
to make your case stronger:

- Is the feature or service
  majorly beneficial
  to user experience
  in general terms,
  as opposed to
  only addressing
  a niche use case?
- Could your desired feature
  be delivered by
  one of the components
  already provided by {{ cookiecutter.project_name }}?
- Is this feature clear enough
  to be adopted by users
  unfamiliar with its purpose?
- Is this feature
  easy to use
  once it is implemented?
- Does this feature require
  just additional configuration
  for {{ cookiecutter.project_name }}?
  Or does it require
  writing additional code?
  The less API changes needed
  for the feature to work
  the more chances it will have
  to be eventually added;
- What is the level of maintenance
  that will be needed
  once this feature is integrated
  into {{ cookiecutter.project_name }}?

Also,
why not take this opportunity
to [become a contributor][8]?
After all,
the most effective way
to make a contribution
is to make one [that comes from yourself][9].

## Specific Guidelines for Requests for Correction
{%- if cookiecutter.__scm_platform_group == 'glab-paid' %}
<!-- This section is also described in project and group CONTRIBUTING.md guides
  [project]: ../../../../CONTRIBUTING.md#specific-guidelines-for-requests-for-correction
  [group]: {{ cookiecutter.__contributing_prefix }}#specific-guidelines-for-requests-for-correction

  REMEMBER TO INCORPORATE CHANGES FROM BOTH GUIDES WHEN UPDATING THIS FILE
-->
{%- else %}
<!-- This section is also described in CONTRIBUTING.md
  [link]: ../../../../CONTRIBUTING.md#specific-guidelines-for-requests-for-correction

  REMEMBER TO MIRROR ANY CHANGES ON BOTH FILES
-->
{%- endif %}

[![RFCs][10]][11]

Requests for Correction are used
to track unexpected behaviour
from template generation,
namely bugs.

A bug is a **demonstrable** problem
that is caused by
the code in the repository.

Guidelines for [RFCs][12]:

- Use the [issue search][11]
  to check if a request
  has already been reported;
- Check if the issue has been fixed
  by trying to reproduce it
  using the latest version of {{ cookiecutter.project_name }};
- **Isolate the problem:**
  create a test case
  to demonstrate your issue.
  Provide either
  a repository,
  [gist][13]/[snippet][14]
  or code sample
  to demonstrate you problem.

We kindly ask applicants
to be available for follow-up questions
to clarify their reports
if more information is needed.
A good RFC should include
sufficient information
to help developers identify
the issue's underlying cause.
While the nature of errors
can be diverse
and thus challenging for users to report
with full context,
providing the information below
is much valuable
to accelerate the process:

- What is your environment?
    - What OS are you using?
    - Which version of {{ cookiecutter.project_name }} are you using?
- What steps will reproduce the issue?
    - What are the parameters used
      during application runtime
      that reproduce the bug?
{%- if cookiecutter.__app_class != 'bare' %}
      You can provide those
      through the `settings.toml` file;
{%- endif %}
    - At which point specifically
      did your error occur
      during your journey?
- Can you provide
  error logs or tracebacks
  to further detail the issue?
{%- if cookiecutter.app_type == 'bare_repo' %}
  Tools like [`reprexpy`][15]
{%- else %}
  {{ cookiecutter.project_name }} provides
  a `report.log` file
  containing only the last executed run of the program
  to facilitate bug reporting;
  additionally,
  tools like [`reprexpy`][15]
{%- endif %}
  can assist you
  in providing more technical detail
  if you are not able to;
- Do you have
  any visual evidence
  to share for further investigation?

These details
will help people
to fix any potential issues.
It is important to note
that **all** reports are valuable,
even if they are not perfectly detailed.

!!! warning

    **Avoid overloading with extraneous details.**
    RFCs are the type of request
    that most need attention
    and careful examination
    by the development team,
    since a bug can turn {{ cookiecutter.project_name }}
    entirely unusable.
    Focus on objective facts
    directly related to the bug
    and kindly perform your due diligence
    as much as possible
    before bringing it to us,
    contextualising your research and findings
    to avoid rework
    by the development team.

<!-- Anchors -->

[1]: {{ cookiecutter.__scm_link_url }}/blob/master/README.md
{%- if cookiecutter.__scm_platform_lc == 'gitlab' %}
[2]: {{ cookiecutter.__scm_link_url }}/tree/master/.gitlab/issue_templates
[3]: {{ cookiecutter.__scm_link_url }}/issues?state=all&type%5B%5D=issue
[4]: https://docs.gitlab.com/user/markdown/
[5]: {{ cookiecutter.__scm_link_url }}/issues/new?description_template=Request%20for%20Support
[6]: {{ cookiecutter.__scm_link_url }}/issues/new?description_template=Request%20for%20Improvement
{%- else %}
[2]: {{ cookiecutter.__scm_link_url }}/tree/master/.github/ISSUE_TEMPLATE
[2a]: {{ cookiecutter.__scm_link_url }}/tree/master/.github/DISCUSSION_TEMPLATE
[3]: {{ cookiecutter.__scm_link_url }}/issues/?q=is%3Aissue
[3a]: {{ cookiecutter.__scm_link_url }}/discussions?discussions_q=
[4]: https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax
[5]: {{ cookiecutter.__scm_link_url }}/discussions/new?category=requests-for-support
[6]: {{ cookiecutter.__scm_link_url }}/discussions/new?category=requests-for-improvement
{%- endif %}
{%- if cookiecutter.__scm_platform_group == 'glab-paid' %}
[7]: {{ cookiecutter.__gitlab_org }}/epics
{%- elif cookiecutter.__scm_platform_group == 'glab-free' %}
[7]: {{ cookiecutter.__scm_link_url }}/milestones
{%- else %}
[7]: {{ cookiecutter.__scm_link_url }}/projects
{%- endif %}
[8]: ../philosophy.md#operate-with-a-bias-for-action
[9]: ../philosophy.md#there-are-no-good-first-issues
[10]: https://img.shields.io/badge/requests_for_correction-dc143c?style=for-the-badge
{%- if cookiecutter.__scm_platform_group == 'glab-paid' %}
[11]: {{ cookiecutter.__scm_link_url }}/issues?state=opened&label_name%5B%5D=request%3A%3Acorrection&type%5B%5D=issue
{%- elif cookiecutter.__scm_platform_group == 'glab-free' %}
[11]: {{ cookiecutter.__scm_link_url }}/issues?state=opened&label_name%5B%5D=rfc&type%5B%5D=issue
{%- else %}
[11]: {{ cookiecutter.__scm_link_url }}/issues/?q=is%3Aissue%20state%3Aopen%20label%3Arfc
{%- endif %}
{%- if cookiecutter.__scm_platform_lc == 'gitlab' %}
[12]: {{ cookiecutter.__scm_link_url }}/issues/new?description_template=Request%20for%20Correction
[13]: https://docs.github.com/en/get-started/writing-on-github/editing-and-sharing-content-with-gists/creating-gists
[14]: https://docs.gitlab.com/user/snippets/
[15]: https://reprexpy.readthedocs.io/en/latest/
{%- else %}
[12]: {{ cookiecutter.__scm_link_url }}/issues/new?template=request_for_correction.yml
[13]: https://docs.github.com/en/get-started/writing-on-github/editing-and-sharing-content-with-gists/creating-gists
[14]: https://docs.gitlab.com/user/snippets/
[15]: https://reprexpy.readthedocs.io/en/latest/
{%- endif %}
