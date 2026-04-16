{% raw -%}
---
tags:
  - Section Intros
  - For Your Information
---

{% endraw -%}
# Other Ways to Contribute
<!-- This section is also described in CONTRIBUTING.md
  [link]: ../../../../CONTRIBUTING.md#reminder_ribbon-other-ways-to-contribute

  REMEMBER TO MIRROR ANY CHANGES ON BOTH FILES
-->

You can contribute to {{ cookiecutter.project_name }}
in additional ways,
one does not need
to know the inner workings of the project
to improve it!
This section provides an overview
on how users outside the project development
can aid the development team,
as well as how to behave and communicate
to improve efficiency
among the team
and between the team and the community.

Since running an open source project
can get exceptionally busy,
any new incoming contact
from outside the development team
can require a contributor's attention
to be redirected
from ongoing work for hours or days.

For this reason,
we kindly ask users
to make a conscious effort
to evaluate the causes
for reaching the team
and focus on matters that are
useful,
clear,
easy to evaluate
and have already been refined
to be brought to attention.
This way
everyone benefits from
faster communication and resolution.

## Contributing by Promoting {{ cookiecutter.project_name }}
<!-- This section is also described in CONTRIBUTING.md
  [link]: ../../../../CONTRIBUTING.md#contributing-by-promoting-{{ cookiecutter.project_name.lower().split() | join('-') }}

  REMEMBER TO MIRROR ANY CHANGES ON BOTH FILES
-->

Promoting {{ cookiecutter.project_name }}
helps us reach a larger audience
and receive more feedback
to continuously improve the project,
your endorsement and recommendation
of our project
is of a **huge** value to us!
Thank you in advance for your interest
and use of {{ cookiecutter.project_name }},
we are really proud of this project
and we couldn't keep advancing with it
without your support!

Here's how you can promote {{ cookiecutter.project_name }}:

{% if cookiecutter.__scm_platform_lc == 'gitlab' -%}
- Set the [Notification level][1] to **"Watch"**
  on the [{{ cookiecutter.scm_namespace.capitalize() }} organisation][2]
{%- else %}
- Set the [Notification level][1] to **"Watch"**
  on the [{{ cookiecutter.project_name }} repository][2]
{%- endif %}
  and receive updates
  on most of our activity;
- Star the project;
- Share the project with your colleagues;
- Write a short article
  on how you are using {{ cookiecutter.project_name }}
  in your day-to-day life;
- Share your
  best practices
  and workflows
  for leveraging {{ cookiecutter.project_name }} usefulness
  with us,
  we love getting inspired
  to add new functionality
  and value to our application!

Thank you
for your interest
in {{ cookiecutter.project_name }}!
Your engagement
and contributions
reassure us that
what we are doing matters!
:beers:

<!-- Anchors -->
{%- if cookiecutter.__scm_platform_lc == 'gitlab' %}

[1]: https://docs.gitlab.com/user/profile/notifications/#notification-levels
[2]: https://{{ cookiecutter.__scm_platform_lc }}.com/{{ cookiecutter.scm_namespace }}
{%- else %}

[1]: https://docs.github.com/en/subscriptions-and-notifications/get-started/configuring-notifications#about-participating-and-watching-notifications
[2]: {{ cookiecutter.__scm_base_url }}
{%- endif %}
