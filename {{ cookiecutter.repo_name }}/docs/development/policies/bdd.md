{% raw -%}
---
tags:
  - Development Guides
  - Design Definitions
  - Workflows
  - Policies & Rules
---

{% endraw -%}
# Behaviour-Driven Development
{%- if cookiecutter.scm_platform == 'GitLab Premium/Ultimate' %}
<!-- This section is also described in the group CONTRIBUTING.md guide
  [link]: {{ cookiecutter.__contributing_prefix }}#behaviour-driven-development

  REMEMBER TO INCORPORATE CHANGES TO THIS FILE WHEN UPDATING THE GUIDE
-->
{%- else %}
<!-- This section is also described in CONTRIBUTING.md
  [link]: ../../../../CONTRIBUTING.md#behaviour-driven-development

  REMEMBER TO MIRROR ANY CHANGES ON BOTH FILES
-->
{%- endif %}

At {{ cookiecutter.project_name }},
we believe building software
goes beyond just coding
its implementation.
More often than not,
open source projects
face extreme hurdles
to effectively
deliver aggregated value
to their users
due to a lenient _laissez-faire_ approach
to project development.
This leaves users frustrated
when desired features
go unlaunched
and can eventually signal a project's doom,
as users migrate
to alternative solutions which,
while not perfect,
address the singular pivotal element
that guarantee their adoption:
**making the user feel like they matter**.

We have adopted a mission
to turn our project development
more structured
and better prepared
to handle scaling adequately
with the community's expectations
on the development team's capabilities.
We believe the best practice
we could embrace
towards this vision
is to leverage
[Behaviour-Driven Development][1]
for our development cycle.

We expect all contributors
to understand
and adopt BDD best practices
during development,
striving to formulate unclear specifications,
engaging with other contributors
to debate different implementation choices
and safeguarding [institutional knowledge][2].

We understand that
adopting BDD might seem like
an additional step
that slows down
our development process
at first glance.
However,
we are committed to BDD
because it aligns with {{ cookiecutter.project_name }}'s [core values][3] of
collaboration,
transparency
and continuous improvement.

By focusing on
{%- if cookiecutter.app_type == 'bare_repo' %}
the behaviour of our library
{%- else %}
the behaviour of our application
{%- endif %}
from the end-user's perspective
through BDD,
we ensure that everyone
— developers, testers, and users —
shares a clear understanding
of what we aim to achieve.
This approach promotes upfront clarity,
reducing misunderstandings and misalignments
down the line.
It also encourages us
to articulate requirements
in plain language,
fostering better communication
and collaboration among team members.

While there may be
an initial learning curve
for those unfamiliar
with the paradigm,
the long-term benefits are substantial.
It results in
more sustainable and maintainable code,
ultimately accelerating our development cycle
and ensuring we deliver value consistently.
It also reinforces
our commitment
to creating an environment
where contributions are
diverse
— involving not only the work of
software developers,
but also
product managers,
designers,
researchers
_and_ users
—
contributors are valued
and everyone feels empowered to grow and succeed.

## References for BDD
{%- if cookiecutter.scm_platform == 'GitLab Premium/Ultimate' %}
<!-- This section is also described in the group CONTRIBUTING.md guide
  [link]: {{ cookiecutter.__contributing_prefix }}#references-for-bdd

  REMEMBER TO INCORPORATE CHANGES TO THIS FILE WHEN UPDATING THE GUIDE
-->
{%- else %}
<!-- This section is also described in CONTRIBUTING.md
  [link]: ../../../../CONTRIBUTING.md#references-for-bdd

  REMEMBER TO MIRROR ANY CHANGES ON BOTH FILES
-->
{%- endif %}

The structured approach BDD offers
will help us maintain
the high standards we strive for,
ensuring that every contribution
aligns with our shared vision and goals.

To help contributors
to get more familiar
with BDD practices,
we provide a suggested list of references below:

- [The Cucumber documentation][1],
  especially their [article on BDD][4];
- The [Modern Software Engineering channel BDD playlist][5],
  with special consideration to
  the following videos:
    - [_3 Reasons why BDD Is Failing You_][6];
    - [_The Truth about Cucumber & BDD_][7];
- The [`pytest-bdd` documentation][8],
  as {{ cookiecutter.project_name }} uses this library
  to parse the feature files
  with test scenarios;
- Automation Panda's [BDD Guide][9];
- [_Behaviour-Driven Development: A Data Scientist Perspective_][10].

<!-- Anchors -->

[1]: https://cucumber.io/docs/
[2]: https://www.teachfloor.com/elearning-glossary/institutional-knowledge
[3]: ../philosophy.md
[4]: https://cucumber.io/docs/bdd/
[5]: https://youtube.com/playlist?list=PLwLLcwQlnXByKR1Fo7UnE6gQAbx-JfYJZ
[6]: https://youtu.be/LuCqnxGxIPE
[7]: https://youtu.be/YUkk2lGLxjA
[8]: https://pytest-bdd.readthedocs.io/en/latest/
[9]: https://automationpanda.com/bdd/
[10]: https://data-ai.theodo.com/en/technical-blog/behavior-driven-development-data-scientist-perspective
