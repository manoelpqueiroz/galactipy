{% raw -%}
---
tags:
  - Development Guides
  - Policies & Rules
  - Workflows
---

{% endraw -%}
# Fostering an Inviting Community

As a {{ cookiecutter.project_name }} contributor, your responsibilities
are not supposed to be restricted to
code,
commits
and work items only.
Software development is an act of collaboration,
and collaboration is inherently human in nature.
Our desire is
to build an outstanding product,
but it will be even more successful
if it can be built
with an ever growing community of contributors.

However,
the hard part of
getting into open source for the first time
isn't the implementation of a feature,
but **figuring out how to actually contribute with changes**.
That's why
ensuring new contributors can get started
is as important as contributing itself.
Open source projects live and die
by their communities,
if we as contributors are not doing our job
of fostering communal interactions,
maintaining the project might prove much harder
in the future.

There are two separate areas of action
in which actions can be taken
to achieve this goal:

1. Preserve an orderly environment:
   - Keep the `CONTRIBUTING` file up to date
     and always reflective of
     the project's current policies and guidelines.
     Successful projects that reach larger audiences
     are able to do so
     through ease of access
     to knowledge surrounding them;
   - Make a conscious attempt
     to keep code and configuration [organised][1],
     with relevant implementation reasoning
     [documented][2] via the commit description;
   - Maintain and update Git hooks
     to check and enforce any project standards
     so people don't have the frustration
     of going back and forth on the {{ cookiecutter.__mr_term }};
   - Maintain and update CI jobs
     to automate further development tasks
     and allow contributors to focus
     on delivering new features;
   - Be conscious of the [energy vampires][3] perturbing development
     and either propose [actions][4]
     for eliminating them
     or seek discussion and feedback
     via an [**Internal Improvement**][5] {{ cookiecutter.__mr_acronym }};
   - Keep the {{ cookiecutter.__scm_platform_base }} repository efficient
     by properly labelling work items
     and associating them
     with the relevant project {{ cookiecutter.__roadmap_item }};
2. Become an advocate for new contributors:
   - Be overly conscious of [how to behave][6]
     when interacting with a user
     publishing their first request.
     The guidelines for [reviewers][7] also apply
     when communicating with {{ cookiecutter.project_name }} users
     in their requests;
   - Before jumping
     to resolve a request opened by a user,
     the best thing you can do
     is to open a sea of opportunities:
     **invite the author to solve the request together**
     and in the process
     grant them their first contribution
     to the project.
     You already know the drill,
     use the space
     to guide them
     on our ways and standards,
     empower them to understand how the project operates.
     You have [started small][8],
     so why not help someone else
     take this small first step?
   - Likewise,
     there are developments
     you could complete in less than 10 minutes.
     Why not turn them into [starter assignments][9]?

## About Starter Assignments

We refer to our "Good First Issue" work items
as **starter assignments**,
a term we believe better aligns
with our goal
of fostering a vibrant community
around {{ cookiecutter.project_name }}.
The term "good first issue"
often feels generic
and commoditised,
offering little incentive for newcomers
to engage deeply with the project.
In contrast,
"starter assignments" emphasise action
and significance,
providing value
for both new contributors
and developers
who create these opportunities.

Through stater assignments,
we aim to:

1. Offer a compelling resource
   that encourages developers
   to begin contributing to {{ cookiecutter.project_name }};
2. Enhance contributor onboarding
   by providing an alternative
   to simply pointing to documentation;
3. Encourage existing contributors
   to refine skills in
   technical writing,
   requirements specification,
   contextualisation
   and problem-solving organisation;
4. Elevate discussions
   around future developments
   by helping newcomers understand
   the project’s vision
   and enabling veterans
   to articulate ideas more clearly
   – ultimately leading to...
5. A broader pool of perspectives
   and proposals
   to amplify developments
   and help {{ cookiecutter.project_name }} thrive.

To achieve these goals,
it is essential
for current contributors
to identify opportunities
to turn ongoing work
into practical assignments
that new contributors can tackle
with ease.
Remember:
**designing starter assignments**
**is just as important**
**as developing new features**
– treat them
with the same care and dedication.

A few tips
to create high quality
starter assignments:

- Make them purpose-driven
  and connect them
  to greater goals of the project;
  good first issues exist
  solely for leaving a breadcrumb
  for the new contributor;
- Provide a clear path
  to the solution
  so someone else can implement it;
  you can leverage {{ cookiecutter.__scm_platform_base }}'s
  feed-like functionality
  and work item hierarchy
  to slice the solution
  in smaller chunks;
- Make it as easy as possible;
  say exactly where changes need to go,
  recommend a good approach
  and tie it in
  to project's goals
  and development standards.

For new contributors
who have picked up a starter assignment,
your mentor most likely
has made their best effort
to ensure the delivery steps
are as clear as possible.
However, if you ever feel stuck
or confused,
don't hesitate to seek help.
{%- if cookiecutter.__scm_platform_lc == 'gitlab' %}
Leverage [replies][9a]
{%- else %}
Leverage replies
{%- endif %}
and [reactions][10]
to direct your questions
and work together
with your mentor
so you can see your contribution delivered.

If you are not getting replies
from your mentor,
mention `@all`
in your starter assignment
and someone from the team
will reach out to you.

<!-- Anchors -->

[1]: https://gregorybeamer.wordpress.com/2020/11/12/why-code-organization-is-so-important-in-software/
[2]: ../philosophy.md#say-why-not-just-what
[3]: https://simonsinek.com/stories/the-right-way-to-stand-up-for-yourself-at-work/
[4]: ../philosophy.md#operate-with-a-bias-for-action
{%- if cookiecutter.__scm_platform_lc == 'gitlab' %}
[5]: {{ cookiecutter.__scm_link_url }}/merge_requests/new?issuable_template=Internal%2520Improvements
{%- else %}
[5]: {{ cookiecutter.__scm_link_url }}/pulls/compare?template=internal_improvements.md
{%- endif %}
[6]: ./behave.md
[7]: ./roles.md#the-responsibility-of-the-reviewer
[8]: https://firstpr.me/
[9]: ./foster.md#about-starter-assignments
{%- if cookiecutter.__scm_platform_lc == 'gitlab' %}
[9a]: https://docs.gitlab.com/user/discussions/
[10]: https://docs.gitlab.com/user/emoji_reactions/
{%- else %}
[10]: https://github.blog/news-insights/product-news/add-reactions-to-pull-requests-issues-and-comments/
{%- endif %}
